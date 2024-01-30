<<<<<<< HEAD
"""CBOE Options Chains Model."""
=======
"""Cboe Options Chains Model."""

# pylint: disable=invalid-name, unused-argument
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from datetime import datetime
from typing import Any, Dict, List, Optional

<<<<<<< HEAD
import pandas as pd
from openbb_cboe.utils.helpers import (
    TICKER_EXCEPTIONS,
    get_cboe_directory,
    get_cboe_index_directory,
=======
from openbb_cboe.utils.helpers import (
    TICKER_EXCEPTIONS,
    get_company_directory,
    get_index_directory,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
)
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.options_chains import (
    OptionsChainsData,
    OptionsChainsQueryParams,
)
<<<<<<< HEAD
from openbb_core.provider.utils.helpers import make_request
from pydantic import Field, field_validator
=======
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import amake_request
from pandas import DataFrame, DatetimeIndex, Series, to_datetime
from pydantic import Field
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class CboeOptionsChainsQueryParams(OptionsChainsQueryParams):
    """CBOE Options Chains Query.

    Source: https://www.cboe.com/
    """

<<<<<<< HEAD
=======
    use_cache: bool = Field(
        default=True,
        description="When True, the company directories will be cached for"
        + "24 hours and are used to validate symbols."
        + " The results of the function are not cached. Set as False to bypass.",
    )

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class CboeOptionsChainsData(OptionsChainsData):
    """CBOE Options Chains Data."""

<<<<<<< HEAD
    bid_size: int = Field(description="Bid size for the option.")
    ask_size: int = Field(description="Ask size for the option.")
    theoretical: float = Field(description="Theoretical value of the option.")
    open: float = Field(description="Opening price of the option.")
    high: float = Field(description="High price of the option.")
    low: float = Field(description="Low price of the option.")
    last_trade_price: Optional[float] = Field(
        description="Last trade price of the option.", default=None
    )
    tick: Optional[str] = Field(
        description="Whether the last tick was up or down in price.", default=None
    )
    prev_close: float = Field(description="Previous closing price of the option.")
    change: float = Field(description="Change in  price of the option.")
    change_percent: float = Field(description="Change, in percent, of the option.")
    implied_volatility: float = Field(description="Implied volatility of the option.")
    delta: float = Field(description="Delta of the option.")
    gamma: float = Field(description="Gamma of the option.")
    vega: float = Field(description="Vega of the option.")
    theta: float = Field(description="Theta of the option.")
    rho: float = Field(description="Rho of the option.")
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    last_trade_timestamp: Optional[datetime] = Field(
        description="Last trade timestamp of the option.", default=None
    )
    dte: int = Field(description="Days to expiration for the option.")

<<<<<<< HEAD
    @field_validator("expiration", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime object from the date string"""
        return datetime.strptime(v, "%Y-%m-%d")

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class CboeOptionsChainsFetcher(
    Fetcher[
        CboeOptionsChainsQueryParams,
        List[CboeOptionsChainsData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CboeOptionsChainsQueryParams:
        """Transform the query."""
        return CboeOptionsChainsQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: CboeOptionsChainsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
<<<<<<< HEAD
        """Return the raw data from the CBOE endpoint"""
        symbol = query.symbol.upper()

        INDEXES = get_cboe_index_directory()
        SYMBOLS = get_cboe_directory()

        if symbol not in SYMBOLS.index:
            raise RuntimeError(f"{symbol} was not found in the CBOE directory.")
=======
        """Return the raw data from the Cboe endpoint"""

        symbol = query.symbol.replace("^", "").split(",")[0]
        INDEXES = await get_index_directory(use_cache=query.use_cache)
        SYMBOLS = await get_company_directory(use_cache=query.use_cache)
        INDEXES = INDEXES.set_index("index_symbol")

        if symbol not in SYMBOLS.index:
            raise RuntimeError(f"{symbol} was not found in the Cboe options directory.")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        quotes_url = (
            f"https://cdn.cboe.com/api/global/delayed_quotes/options/_{symbol}.json"
            if symbol in TICKER_EXCEPTIONS or symbol in INDEXES.index
            else f"https://cdn.cboe.com/api/global/delayed_quotes/options/{symbol}.json"
        )

<<<<<<< HEAD
        r = make_request(quotes_url)
        if r.status_code != 200:
            raise RuntimeError(f"No options data found for the symbol, {symbol}.")

        r_json = r.json()
        options_df = pd.DataFrame.from_records(r_json["data"]["options"])
=======
        return await amake_request(quotes_url)

    @staticmethod
    def transform_data(
        query: CboeOptionsChainsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[CboeOptionsChainsData]:
        """Transform the data to the standard format"""

        if not data:
            raise EmptyDataError()

        options_df = DataFrame.from_records(data["data"]["options"])
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        options_df = options_df.rename(
            columns={
                "option": "contract_symbol",
                "iv": "implied_volatility",
<<<<<<< HEAD
                "theo": "theoretical",
                "last_trade_price": "last_trade_price",
                "last_trade_time": "last_trade_timestamp",
                "percent_change": "change_percent",
                "prev_day_close": "prev_close",
=======
                "theo": "theoretical_price",
                "percent_change": "change_percent",
                "prev_day_close": "prev_close",
                "last_trade_time": "last_trade_timestamp",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        )

        # Parses the option symbols into columns for expiration, strike, and option_type

        option_df_index = options_df["contract_symbol"].str.extractall(
            r"^(?P<Ticker>\D*)(?P<expiration>\d*)(?P<option_type>\D*)(?P<strike>\d*)"
        )
        option_df_index = option_df_index.reset_index().drop(
            columns=["match", "level_0"]
        )
        option_df_index.option_type = option_df_index.option_type.str.replace(
            "C", "call"
        ).str.replace("P", "put")
        option_df_index.strike = [ele.lstrip("0") for ele in option_df_index.strike]
<<<<<<< HEAD
        option_df_index.strike = pd.Series(option_df_index.strike).astype(float)
=======
        option_df_index.strike = Series(option_df_index.strike).astype(float)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        option_df_index.strike = option_df_index.strike * (1 / 1000)
        option_df_index.strike = option_df_index.strike.to_list()
        option_df_index.expiration = [
            ele.lstrip("1") for ele in option_df_index.expiration
        ]
<<<<<<< HEAD
        option_df_index.expiration = pd.DatetimeIndex(
=======
        option_df_index.expiration = DatetimeIndex(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            option_df_index.expiration, yearfirst=True
        ).astype(str)
        option_df_index = option_df_index.drop(columns=["Ticker"])

        # Joins the parsed symbol into the dataframe.

        quotes = option_df_index.join(options_df)

        now = datetime.now()
<<<<<<< HEAD
        temp = pd.DatetimeIndex(quotes.expiration)
=======
        temp = DatetimeIndex(quotes.expiration)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        temp_ = (temp - now).days + 1
        quotes["dte"] = temp_

        quotes["last_trade_timestamp"] = (
<<<<<<< HEAD
            pd.to_datetime(quotes["last_trade_timestamp"], format="%Y-%m-%dT%H:%M:%S")
=======
            to_datetime(quotes["last_trade_timestamp"], format="%Y-%m-%dT%H:%M:%S")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            .fillna(value="-")
            .replace("-", None)
        )
        quotes = quotes.set_index(
            keys=["expiration", "strike", "option_type"]
        ).sort_index()
        quotes["open_interest"] = quotes["open_interest"].astype("int64")
        quotes["volume"] = quotes["volume"].astype("int64")
        quotes["bid_size"] = quotes["bid_size"].astype("int64")
        quotes["ask_size"] = quotes["ask_size"].astype("int64")
        quotes["prev_close"] = round(quotes["prev_close"], 2)
<<<<<<< HEAD
        quotes["change_percent"] = round(quotes["change_percent"], 2)

        return quotes.reset_index().to_dict("records")

    @staticmethod
    def transform_data(
        query: CboeOptionsChainsQueryParams,
        data: dict,
        **kwargs: Any,
    ) -> List[CboeOptionsChainsData]:
        """Transform the data to the standard format"""
        return [CboeOptionsChainsData.model_validate(d) for d in data]
=======
        quotes["change_percent"] = round(quotes["change_percent"] / 100, 4)

        return [
            CboeOptionsChainsData.model_validate(d)
            for d in quotes.reset_index().to_dict("records")
        ]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
