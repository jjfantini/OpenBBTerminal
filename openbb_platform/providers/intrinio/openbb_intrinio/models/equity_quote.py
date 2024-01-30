"""Intrinio Equity Quote Model."""

<<<<<<< HEAD
from concurrent.futures import ThreadPoolExecutor
=======
# pylint: disable=unused-argument
import re
import warnings
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_quote import (
    EquityQuoteData,
    EquityQuoteQueryParams,
)
<<<<<<< HEAD
from openbb_intrinio.utils.helpers import get_data_one
from openbb_intrinio.utils.references import SOURCES
from pydantic import Field, field_validator

=======
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    amake_requests,
)
from openbb_intrinio.utils.references import SOURCES, VENUES, IntrinioSecurity
from pydantic import Field, field_validator

_warn = warnings.warn

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class IntrinioEquityQuoteQueryParams(EquityQuoteQueryParams):
    """Intrinio Equity Quote Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_security_realtime_price_v2
    """

    symbol: str = Field(
        description="A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)."
    )
    source: SOURCES = Field(default="iex", description="Source of the data.")


class IntrinioEquityQuoteData(EquityQuoteData):
    """Intrinio Equity Quote Data."""

    __alias_dict__ = {
<<<<<<< HEAD
        "day_low": "low_price",
        "day_high": "high_price",
        "date": "last_time",
    }

    last_price: float = Field(description="Price of the last trade.")
    last_time: datetime = Field(
        description="Date and Time when the last trade occurred.", alias="date"
    )
    last_size: Optional[int] = Field(description="Size of the last trade.")
    bid_price: float = Field(description="Price of the top bid order.")
    bid_size: int = Field(description="Size of the top bid order.")
    ask_price: float = Field(description="Price of the top ask order.")
    ask_size: int = Field(description="Size of the top ask order.")
    open_price: float = Field(description="Open price for the trading day.")
    close_price: Optional[float] = Field(
        default=None, description="Closing price for the trading day (IEX source only)."
    )
    high_price: float = Field(
        description="High Price for the trading day.", alias="day_high"
    )
    low_price: float = Field(
        description="Low Price for the trading day.", alias="day_low"
    )
    exchange_volume: Optional[int] = Field(
        default=None,
        description="Number of shares exchanged during the trading day on the exchange.",
    )
    market_volume: Optional[int] = Field(
        default=None,
        description="Number of shares exchanged during the trading day for the whole market.",
=======
        "exchange": "listing_venue",
        "market_center": "market_center_code",
        "bid": "bid_price",
        "ask": "ask_price",
        "open": "open_price",
        "close": "close_price",
        "low": "low_price",
        "high": "high_price",
        "last_timestamp": "last_time",
        "volume": "market_volume",
    }
    is_darkpool: Optional[bool] = Field(
        default=None, description="Whether or not the current trade is from a darkpool."
    )
    source: Optional[str] = Field(
        default=None, description="Source of the Intrinio data."
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )
    updated_on: datetime = Field(
        description="Date and Time when the data was last updated."
    )
<<<<<<< HEAD
    source: str = Field(description="Source of the data.")
    listing_venue: Optional[str] = Field(
        default=None,
        description="Listing venue where the trade took place (SIP source only).",
    )
    sales_conditions: Optional[str] = Field(
        default=None,
        description="Indicates any sales condition modifiers associated with the trade.",
    )
    quote_conditions: Optional[str] = Field(
        default=None,
        description="Indicates any quote condition modifiers associated with the trade.",
    )
    market_center_code: Optional[str] = Field(
        default=None, description="Market center character code."
    )
    is_darkpool: Optional[bool] = Field(
        default=None, description="Whether or not the current trade is from a darkpool."
    )
    messages: Optional[List[str]] = Field(
        default=None, description="Messages associated with the endpoint."
    )
    security: Optional[Dict[str, Any]] = Field(
=======
    security: Optional[IntrinioSecurity] = Field(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        default=None, description="Security details related to the quote."
    )

    @field_validator("last_time", "updated_on", mode="before", check_fields=False)
<<<<<<< HEAD
=======
    @classmethod
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return (
            datetime.fromisoformat(v.replace("Z", "+00:00"))
            if v.endswith(("Z", "+00:00"))
            else datetime.fromisoformat(v)
        )

<<<<<<< HEAD
=======
    @field_validator("sales_conditions", mode="before", check_fields=False)
    @classmethod
    def validate_sales_conditions(cls, v):
        """Validate sales conditions and remove empty strings."""
        if v:
            control_char_re = re.compile(r"[\x00-\x1f\x7f-\x9f]")
            v = control_char_re.sub("", v).strip()
            v = None if v == "" else v
        return v if v else None

    @field_validator("exchange", "market_center", mode="before", check_fields=False)
    @classmethod
    def validate_listing_venue(cls, v):
        """Validate listing venue and remove empty strings."""
        if v:
            return VENUES[v] if v in VENUES else v
        return None

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class IntrinioEquityQuoteFetcher(
    Fetcher[
        IntrinioEquityQuoteQueryParams,
        List[IntrinioEquityQuoteData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioEquityQuoteQueryParams:
        """Transform the query params."""
        return IntrinioEquityQuoteQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: IntrinioEquityQuoteQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
<<<<<<< HEAD
        results: List[Dict] = []

        def get_data(symbol):
            base_url = "https://api-v2.intrinio.com"
            url = f"{base_url}/securities/{symbol}/prices/realtime?source={query.source}&api_key={api_key}"
            data = get_data_one(url, **kwargs)
            data["symbol"] = symbol
            results.append(data)

        with ThreadPoolExecutor() as executor:
            executor.map(get_data, [s.strip() for s in query.symbol.split(",")])

        return results

    @staticmethod
    def transform_data(
        query: IntrinioEquityQuoteQueryParams, data: dict, **kwargs: Any
=======

        base_url = "https://api-v2.intrinio.com"

        async def callback(response: ClientResponse, _: Any) -> dict:
            """Return the response."""
            if response.status != 200:
                return {}

            response_data = await response.json()
            response_data["symbol"] = response_data["security"].get("ticker", None)  # type: ignore
            if "messages" in response_data and response_data.get("messages"):  # type: ignore
                _message = list(response_data.pop("messages"))  # type: ignore
                _warn(str(",".join(_message)))
            return response_data  # type: ignore

        urls = [
            f"{base_url}/securities/{s.strip()}/prices/realtime?source={query.source}&api_key={api_key}"
            for s in query.symbol.split(",")
        ]
        return await amake_requests(urls, callback, **kwargs)

    @staticmethod
    def transform_data(
        query: IntrinioEquityQuoteQueryParams, data: List[Dict], **kwargs: Any
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    ) -> List[IntrinioEquityQuoteData]:
        """Return the transformed data."""
        return [IntrinioEquityQuoteData.model_validate(d) for d in data]
