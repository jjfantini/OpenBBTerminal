<<<<<<< HEAD
"""CBOE Helpers Module."""

from datetime import date, timedelta
from io import BytesIO, StringIO
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
import requests_cache
from openbb_core.app.utils import get_user_cache_directory
from openbb_core.provider.utils.helpers import to_snake_case

cache_dir = get_user_cache_directory()
cboe_session = requests_cache.CachedSession(
    f"{cache_dir}/http/cboe_directories", expire_after=timedelta(days=7)
)

TICKER_EXCEPTIONS = ["NDX", "RUT"]

US_INDEX_COLUMNS = {
    "symbol": "symbol",
    "name": "name",
    "current_price": "price",
    "open": "open",
    "high": "high",
    "low": "low",
    "close": "close",
    "prev_day_close": "prev_close",
    "price_change": "change",
    "price_change_percent": "change_percent",
    "last_trade_time": "last_trade_timestamp",
}

EUR_INDEX_COLUMNS = {
    "name": "name",
    "isin": "isin",
    "currency": "currency",
    "current_price": "price",
    "open": "open",
    "high": "high",
    "low": "low",
    "close": "close",
    "prev_day_close": "prev_close",
    "price_change": "change",
    "price_change_percent": "change_percent",
    "last_trade_time": "last_trade_timestamp",
}

EUR_INDEX_CONSTITUENTS_COLUMNS = {
    "symbol": "symbol",
    "current_price": "price",
    "open": "open",
    "high": "high",
    "low": "low",
    "close": "close",
    "volume": "volume",
    "seqno": "seqno",
    "prev_day_close": "prev_close",
    "price_change": "change",
    "price_change_percent": "change_percent",
    "last_trade_time": "last_trade_timestamp",
    "exchange_id": "exchange_id",
    "tick": "tick",
    "security_type": "type",
}


def get_cboe_directory(**kwargs) -> pd.DataFrame:
    """Get the US Listings Directory for the CBOE.

    Returns
    -------
    pd.DataFrame: CBOE_DIRECTORY
        DataFrame of the CBOE listings directory
    """

    r = cboe_session.get(
        "https://www.cboe.com/us/options/symboldir/equity_index_options/?download=csv",
        timeout=10,
    )

    if r.status_code != 200:
        raise RuntimeError(r.status_code)

    r_json = StringIO(r.text)

    CBOE_DIRECTORY = pd.read_csv(r_json)

    CBOE_DIRECTORY = CBOE_DIRECTORY.rename(
        columns={
            " Stock Symbol": "symbol",
            " DPM Name": "dpm_name",
            " Post/Station": "post_station",
            "Company Name": "name",
        }
    ).set_index("symbol")

    return CBOE_DIRECTORY.astype(str)


def get_cboe_index_directory(**kwargs) -> pd.DataFrame:
    """Get the US Listings Directory for the CBOE

    Returns
    -------
    pd.DataFrame: CBOE_INDEXES
    """

    r = cboe_session.get(
        "https://cdn.cboe.com/api/global/us_indices/definitions/all_indices.json",
        timeout=10,
    )

    if r.status_code != 200:
        raise requests.HTTPError(r.status_code)

    CBOE_INDEXES = pd.DataFrame(r.json())

    CBOE_INDEXES = CBOE_INDEXES.rename(
        columns={
            "calc_end_time": "close_time",
            "calc_start_time": "open_time",
            "index_symbol": "symbol",
            "mkt_data_delay": "data_delay",
        },
    )

    indices_order: List[str] = [
        "symbol",
        "name",
        "description",
        "currency",
        "open_time",
        "close_time",
        "tick_days",
        "tick_frequency",
        "tick_period",
        "time_zone",
        "data_delay",
    ]

    CBOE_INDEXES = pd.DataFrame(CBOE_INDEXES, columns=indices_order).set_index("symbol")

    idx = (
        (CBOE_INDEXES.time_zone.str.contains("America/Chicago"))
        & (CBOE_INDEXES.currency.str.contains("USD"))
        & (CBOE_INDEXES.description.str.contains("Daily Risk Control") == 0)
        & (CBOE_INDEXES.name.str.contains("OEX%-SML% INDEX") == 0)
        & (CBOE_INDEXES.name.str.contains("Defined Risk Volatility Income") == 0)
        & (CBOE_INDEXES.description.str.contains("is designed to track") == 0)
    )

    return CBOE_INDEXES[idx]


def get_ticker_info(symbol: str, **kwargs) -> Dict[str, Any]:
    symbol = symbol.upper()
    SYMBOLS = get_cboe_directory()
    INDEXES = get_cboe_index_directory()
    data: Dict[str, Any] = {}

    if symbol not in SYMBOLS.index and symbol not in INDEXES.index:
        raise RuntimeError(f"Data not found for: {symbol}")

    url = (
        f"https://cdn.cboe.com/api/global/delayed_quotes/quotes/_{symbol}.json"
        if symbol in INDEXES.index or symbol in TICKER_EXCEPTIONS
        else f"https://cdn.cboe.com/api/global/delayed_quotes/quotes/{symbol}.json"
    )

    r = requests.get(url, timeout=10)

    if r.status_code not in set([200, 403]):
        raise requests.HTTPError(r.status_code)

    if r.status_code == 403:
        raise RuntimeError(f"Data was not found for, {symbol}.")

    data = r.json()["data"]

    if symbol in SYMBOLS.index.to_list():
        data.update({"name": SYMBOLS.at[symbol, "name"]})
    if symbol in INDEXES.index.to_list():
        data.update({"name": INDEXES.at[symbol, "name"]})

    _data = pd.DataFrame.from_dict(data, orient="index").transpose()

    _data = _data.rename(
        columns={
            "current_price": "price",
            "prev_day_close": "prev_close",
            "price_change": "change",
            "price_change_percent": "change_percent",
            "last_trade_time": "last_trade_timestamp",
            "security_type": "type",
        }
    )

    return _data.transpose()[0].to_dict()


def get_ticker_iv(symbol: str, **kwargs) -> Dict[str, float]:
    """Get annualized high/low historical and implied volatility over 30/60/90 day windows.

    Parameters
    ----------
    symbol: str
        The loaded ticker

    Returns
    -------
    pd.DataFrame: ticker_iv
    """

    symbol = symbol.upper()

    INDEXES = get_cboe_index_directory().index.to_list()

    quotes_iv_url = (
        "https://cdn.cboe.com/api/global/delayed_quotes/historical_data/_"
        f"{symbol}"
        ".json"
        if symbol in TICKER_EXCEPTIONS or symbol in INDEXES
        else f"https://cdn.cboe.com/api/global/delayed_quotes/historical_data/{symbol}.json"
    )

    h_iv = requests.get(quotes_iv_url, timeout=10)

    if h_iv.status_code not in set([200, 403]):
        raise requests.HTTPError(h_iv.status_code)

    if h_iv.status_code == 403:
        raise RuntimeError(f"Data was not found for, {symbol}.")

    data = pd.DataFrame(h_iv.json())[2:-1]["data"].rename(f"{symbol}")

    return data.to_dict()


def list_futures(**kwargs) -> List[dict]:
=======
"""Cboe Helpers"""

# pylint: disable=expression-not-assigned, unused-argument

from datetime import date as dateType
from io import BytesIO, StringIO
from typing import Any, List, Literal, Optional

from aiohttp_client_cache import SQLiteBackend
from aiohttp_client_cache.session import CachedSession
from openbb_core.app.utils import get_user_cache_directory
from openbb_core.provider.utils.client import ClientResponse
from openbb_core.provider.utils.helpers import amake_request, to_snake_case
from pandas import DataFrame, read_csv

TICKER_EXCEPTIONS = ["NDX", "RUT"]

CONSTITUENTS_EU = Literal[  # pylint: disable=invalid-name
    "BAT20P",
    "BBE20P",
    "BCH20P",
    "BCHM30P",
    "BDE40P",
    "BDEM50P",
    "BDES50P",
    "BDK25P",
    "BEP50P",
    "BEPACP",
    "BEPBUS",
    "BEPCNC",
    "BEPCONC",
    "BEPCONS",
    "BEPENGY",
    "BEPFIN",
    "BEPHLTH",
    "BEPIND",
    "BEPNEM",
    "BEPTEC",
    "BEPTEL",
    "BEPUTL",
    "BEPXUKP",
    "BES35P",
    "BEZ50P",
    "BEZACP",
    "BFI25P",
    "BFR40P",
    "BFRM20P",
    "BIE20P",
    "BIT40P",
    "BNL25P",
    "BNLM25P",
    "BNO25G",
    "BNORD40P",
    "BPT20P",
    "BSE30P",
    "BUK100P",
    "BUK250P",
    "BUK350P",
    "BUKAC",
    "BUKBISP",
    "BUKBUS",
    "BUKCNC",
    "BUKCONC",
    "BUKCONS",
    "BUKENGY",
    "BUKFIN",
    "BUKHI50P",
    "BUKHLTH",
    "BUKIND",
    "BUKLO50P",
    "BUKMINP",
    "BUKNEM",
    "BUKSC",
    "BUKTEC",
    "BUKTEL",
    "BUKUTL",
]

cache_dir = get_user_cache_directory()
backend = SQLiteBackend(f"{cache_dir}/http/cboe_directories", expire_after=3600 * 24)


async def response_callback(response: ClientResponse, _: Any):
    """Callback for HTTP Client Response."""
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        return await response.json()
    if "text" in content_type:
        return await response.text()
    return await response.read()


async def get_cboe_data(url, use_cache: bool = True, **kwargs) -> Any:
    """Generic Cboe HTTP request."""
    if use_cache is True:
        async with CachedSession(cache=backend) as cached_session:
            try:
                response = await cached_session.get(url, timeout=10, **kwargs)
                data = await response_callback(response, None)
            finally:
                await cached_session.close()
    else:
        data = await amake_request(url, response_callback=response_callback)

    return data


async def get_company_directory(use_cache: bool = True, **kwargs) -> DataFrame:
    """
    Get the US Company Directory for Cboe options. If use_cache is True,
    the data will be cached for 24 hours.

    Returns
    -------
    DataFrame: Pandas DataFrame of the Cboe listings directory
    """

    url = "https://www.cboe.com/us/options/symboldir/equity_index_options/?download=csv"

    results = await get_cboe_data(url, use_cache)

    response = BytesIO(results)

    directory = read_csv(response)

    directory = directory.rename(
        columns={
            " Stock Symbol": "symbol",
            " DPM Name": "dpm_name",
            " Post/Station": "post_station",
            "Company Name": "name",
        }
    ).set_index("symbol")

    return directory.astype(str)


async def get_index_directory(use_cache: bool = True, **kwargs) -> DataFrame:
    """
    Get the Cboe Index Directory. If use_cache is True,
    the data will be cached for 24 hours.

    Returns
    --------
    List[Dict]: A list of dictionaries containing the index information.
    """

    url = "https://cdn.cboe.com/api/global/us_indices/definitions/all_indices.json"

    results = await get_cboe_data(url, use_cache=use_cache)

    [result.pop("featured") for result in results]
    [result.pop("featured_order") for result in results]
    [result.pop("display") for result in results]
    results = DataFrame(results)
    results = results[results["source"] != "morningstar"]

    return results


async def list_futures(**kwargs) -> List[dict]:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    """List of CBOE futures and their underlying symbols.

    Returns
    --------
    pd.DataFrame
        Pandas DataFrame with results.
    """

<<<<<<< HEAD
    r = requests.get(
        "https://cdn.cboe.com/api/global/delayed_quotes/symbol_book/futures-roots.json",
        timeout=10,
    )

    if r.status_code != 200:
        raise requests.HTTPError(r.status_code)

    return r.json()["data"]


def get_settlement_prices(
    settlement_date: Optional[date] = None,
=======
    r = await get_cboe_data(
        "https://cdn.cboe.com/api/global/delayed_quotes/symbol_book/futures-roots.json"
    )
    data = r.get("data")
    [d.pop("sort_order") for d in data]

    return data


async def get_settlement_prices(
    settlement_date: Optional[dateType] = None,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    options: bool = False,
    archives: bool = False,
    final_settlement: bool = False,
    **kwargs,
<<<<<<< HEAD
) -> pd.DataFrame:
=======
) -> DataFrame:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    """Gets the settlement prices of CBOE futures.

    Parameters
    -----------
    settlement_date: Optional[date]
        The settlement date. Only valid for active contracts. [YYYY-MM-DD]
    options: bool
        If true, returns options on futures.
    archives: bool
        Settlement price archives for select years and products.  Overridden by other parameters.
    final_settlement: bool
        Final settlement prices for expired contracts.  Overrides archives.

    Returns
    -------
<<<<<<< HEAD
    pd.DataFrame
        Pandas DataFrame with results.
    """
    url = ""
    if archives is True:
        url = "https://cdn.cboe.com/resources/futures/archive/volume-and-price/CFE_FinalSettlement_Archive.csv"

    if settlement_date is not None:
        url = f"https://www.cboe.com/us/futures/market_statistics/settlement/csv?dt={settlement_date}"
        if options is True:
            url = f"https://www.cboe.com/us/futures/market_statistics/settlement/csv?options=t&dt={settlement_date}"

=======
    DataFrame
        Pandas DataFrame with results.
    """
    url = ""
    if settlement_date is not None:
        url = (
            "https://www.cboe.com/us/futures/market_statistics"
            + f"/settlement/csv?dt={settlement_date}"
        )
        if options is True:
            url = (
                "https://www.cboe.com/us/futures/market_statistics/"
                + f"settlement/csv?options=t&dt={settlement_date}"
            )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    if settlement_date is None:
        url = "https://www.cboe.com/us/futures/market_statistics/settlement/csv"
        if options is True:
            url = "https://www.cboe.com/us/futures/market_statistics/settlement/csv?options=t"

    if final_settlement is True:
        url = "https://www.cboe.com/us/futures/market_statistics/final_settlement_prices/csv/"

<<<<<<< HEAD
    r = requests.get(url, timeout=10)

    if r.status_code != 200:
        raise RuntimeError(r.status_code)

    data = pd.read_csv(BytesIO(r.content), index_col=None, parse_dates=True)

    if data.empty:
        error_string = (
            f"No results found for, {settlement_date}."
            if settlement_date is not None
            else "No results found."
        )
        raise RuntimeError(error_string)
=======
    if archives is True:
        url = (
            "https://cdn.cboe.com/resources/futures/archive"
            + "/volume-and-price/CFE_FinalSettlement_Archive.csv"
        )

    response = await get_cboe_data(url, use_cache=False, **kwargs)

    data = read_csv(StringIO(response), index_col=None, parse_dates=True)

    if data.empty:
        return DataFrame()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    data.columns = [to_snake_case(c) for c in data.columns]
    data = data.rename(columns={"expiration_date": "expiration"})

    if len(data) > 0:
        return data

<<<<<<< HEAD
    return pd.DataFrame()


class Europe:
    """Class for European CBOE data."""

    @staticmethod
    def get_all_index_definitions(**kwargs) -> Dict[Any, Any]:
        """Get the full list of European index definitions.

        Returns
        -------
        Dict[Any, Any]
            Dictionary with results.
        """

        r = cboe_session.get(
            "https://cdn.cboe.com/api/global/european_indices/definitions/all-definitions.json",
            timeout=10,
        )

        if r.status_code != 200:
            raise requests.HTTPError(r.status_code)
        return r.json()["data"]

    @staticmethod
    def list_indices(**kwargs) -> List[Dict]:
        """Gets names, currencies, ISINs, regions, and symbols for European indices.

        Returns
        -------
        Dict[str, str]
            List of dictionaries with the results.
        """

        data = Europe.get_all_index_definitions()
        data = (
            pd.DataFrame.from_records(pd.DataFrame(data)["index"])
            .drop(columns=["short_name"])
            .rename(columns={"long_name": "name"})
        )
        return data.to_dict("records")

    @staticmethod
    def list_index_constituents(symbol: str, **kwargs) -> List[str]:
        """List symbols for constituents of a European index.

        Parameters
        ----------
        symbol: str
            The symbol of the index.

        Returns
        -------
        List[str]
            List of constituents as ticker symbols.
        """

        SYMBOLS = pd.DataFrame(Europe.list_indices())["symbol"].to_list()
        symbol = symbol.upper()

        if symbol not in SYMBOLS:
            raise RuntimeError(
                f"The symbol, {symbol}, was not found in the CBOE European Index directory.",
            )

        url = f"https://cdn.cboe.com/api/global/european_indices/definitions/{symbol}.json"
        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            raise requests.HTTPError(r.status_code)

        r_json = r.json()["constituents"]

        return [r_json[i]["constituent_symbol"] for i in range(0, len(r_json))]
=======
    return DataFrame()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
