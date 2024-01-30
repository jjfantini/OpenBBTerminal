"""FMP Equity Quote Model."""

<<<<<<< HEAD
from datetime import datetime
from typing import Any, Dict, List, Optional
=======
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.provider.abstract.data import ForceInt
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_quote import (
    EquityQuoteData,
    EquityQuoteQueryParams,
)
<<<<<<< HEAD
from openbb_fmp.utils.helpers import get_data_many, get_querystring
=======
from openbb_core.provider.utils.helpers import amake_requests
from openbb_fmp.utils.helpers import get_querystring
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from pydantic import Field, field_validator


class FMPEquityQuoteQueryParams(EquityQuoteQueryParams):
    """FMP Equity Quote Query.

    Source: https://financialmodelingprep.com/developer/docs/#Stock-Historical-Price
    """


class FMPEquityQuoteData(EquityQuoteData):
    """FMP Equity Quote Data."""

    __alias_dict__ = {
        "price_avg50": "priceAvg50",
        "price_avg200": "priceAvg200",
<<<<<<< HEAD
        "date": "timestamp",
    }

    symbol: Optional[str] = Field(default=None, description="Symbol of the company.")
    name: Optional[str] = Field(default=None, description="Name of the company.")
    price: Optional[float] = Field(
        default=None, description="Current trading price of the equity."
    )
    changes_percentage: Optional[float] = Field(
        default=None, description="Change percentage of the equity price."
    )
    change: Optional[float] = Field(
        default=None, description="Change in the equity price."
    )
    year_high: Optional[float] = Field(
        default=None, description="Highest price of the equity in the last 52 weeks."
    )
    year_low: Optional[float] = Field(
        default=None, description="Lowest price of the equity in the last 52 weeks."
    )
    market_cap: Optional[float] = Field(
        default=None, description="Market cap of the company."
    )
    price_avg50: Optional[float] = Field(
        default=None, description="50 days average price of the equity."
    )
    price_avg200: Optional[float] = Field(
        default=None, description="200 days average price of the equity."
    )
    volume: Optional[ForceInt] = Field(
        default=None,
        description="Volume of the equity in the current trading day.",
    )
    avg_volume: Optional[ForceInt] = Field(
        default=None,
        description="Average volume of the equity in the last 10 trading days.",
    )
    exchange: Optional[str] = Field(
        default=None, description="Exchange the equity is traded on."
    )
    open: Optional[float] = Field(
        default=None,
        description="Opening price of the equity in the current trading day.",
    )
    previous_close: Optional[float] = Field(
        default=None, description="Previous closing price of the equity."
    )
    eps: Optional[float] = Field(
        default=None, description="Earnings per share of the equity."
    )
    pe: Optional[float] = Field(
        default=None, description="Price earnings ratio of the equity."
    )
    earnings_announcement: Optional[str] = Field(
        default=None, description="Earnings announcement date of the equity."
    )
    shares_outstanding: Optional[ForceInt] = Field(
        default=None, description="Number of shares outstanding of the equity."
    )

    @field_validator("timestamp", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d")
=======
        "last_timestamp": "timestamp",
        "high": "dayHigh",
        "low": "dayLow",
        "last_price": "price",
        "change_percent": "changesPercentage",
        "prev_close": "previousClose",
    }
    price_avg50: Optional[float] = Field(
        default=None, description="50 day moving average price."
    )
    price_avg200: Optional[float] = Field(
        default=None, description="200 day moving average price."
    )
    avg_volume: Optional[ForceInt] = Field(
        default=None,
        description="Average volume over the last 10 trading days.",
    )
    market_cap: Optional[float] = Field(
        default=None, description="Market cap of the company."
    )
    shares_outstanding: Optional[ForceInt] = Field(
        default=None, description="Number of shares outstanding."
    )
    eps: Optional[float] = Field(default=None, description="Earnings per share.")
    pe: Optional[float] = Field(default=None, description="Price earnings ratio.")
    earnings_announcement: Optional[Union[datetime, str]] = Field(
        default=None, description="Upcoming earnings announcement date."
    )

    @field_validator("last_timestamp", mode="before", check_fields=False)
    @classmethod
    def validate_last_timestamp(cls, v):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        v = int(v) if isinstance(v, str) else v
        return datetime.utcfromtimestamp(int(v)).replace(tzinfo=timezone.utc)

    @field_validator("earnings_announcement", mode="before", check_fields=False)
    @classmethod
    def timestamp_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime string as a datetime object."""
        if v:
            dt = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f%z")
            dt = dt.replace(microsecond=0)
            timestamp = dt.timestamp()
            return datetime.fromtimestamp(timestamp, tz=timezone.utc)
        return None

    @field_validator("change_percent", mode="after", check_fields=False)
    @classmethod
    def normalize_percent(cls, v):  # pylint: disable=E0213
        """Return the percent value as a normalized value."""
        return float(v) / 100 if v else None
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class FMPEquityQuoteFetcher(
    Fetcher[
        FMPEquityQuoteQueryParams,
        List[FMPEquityQuoteData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPEquityQuoteQueryParams:
        """Transform the query params."""
        return FMPEquityQuoteQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPEquityQuoteQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"
        query_str = get_querystring(query.model_dump(), ["symbol"])
<<<<<<< HEAD
        url = f"{base_url}/quote/{query.symbol}?{query_str}&apikey={api_key}"

        return get_data_many(url, **kwargs)
=======

        symbols = query.symbol.split(",")
        symbols_split = [
            ",".join(symbols[i : i + 10]) for i in range(0, len(symbols), 10)
        ]

        urls = [
            f"{base_url}/quote/{symbol}?{query_str}&apikey={api_key}"
            for symbol in symbols_split
        ]

        return await amake_requests(urls, **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPEquityQuoteQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPEquityQuoteData]:
        """Return the transformed data."""
        return [FMPEquityQuoteData.model_validate(d) for d in data]
