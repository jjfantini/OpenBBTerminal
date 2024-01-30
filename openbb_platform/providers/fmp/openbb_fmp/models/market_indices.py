"""FMP Market Indices Model."""

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.market_indices import (
    MarketIndicesData,
    MarketIndicesQueryParams,
)
<<<<<<< HEAD
=======
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.utils.helpers import get_querystring
from openbb_fmp.utils.helpers import get_data_many
from pydantic import Field, NonNegativeInt


class FMPMarketIndicesQueryParams(MarketIndicesQueryParams):
    """FMP Market Indices Query.

    Source: https://site.financialmodelingprep.com/developer/docs/historical-index-price-api/
    """

    __alias_dict__ = {"start_date": "from", "end_date": "to"}

    timeseries: Optional[NonNegativeInt] = Field(
        default=None, description="Number of days to look back."
    )
<<<<<<< HEAD
    interval: Literal[
        "1min", "5min", "15min", "30min", "1hour", "4hour", "1day"
    ] = Field(default="1day", description="Data granularity.")
=======
    interval: Literal["1min", "5min", "15min", "30min", "1hour", "4hour", "1day"] = (
        Field(default="1day", description="Data granularity.")
    )
    sort: Literal["asc", "desc"] = Field(
        default="desc", description="Sort the data in ascending or descending order."
    )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class FMPMarketIndicesData(MarketIndicesData):
    """FMP Market Indices Data."""

    adj_close: Optional[float] = Field(
<<<<<<< HEAD
        description="Adjusted Close Price of the symbol.",
=======
        description=DATA_DESCRIPTIONS.get("adj_close", ""),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        default=None,
    )
    unadjusted_volume: Optional[float] = Field(
        description="Unadjusted volume of the symbol.",
        default=None,
    )
    change: Optional[float] = Field(
        description="Change in the price of the symbol from the previous day.",
        default=None,
    )
    change_percent: Optional[float] = Field(
        description="Change % in the price of the symbol.",
        default=None,
    )
    label: Optional[str] = Field(
        description="Human readable format of the date.", default=None
    )
    change_over_time: Optional[float] = Field(
        description="Change % in the price of the symbol over a period of time.",
        default=None,
    )


class FMPMarketIndicesFetcher(
    Fetcher[
        FMPMarketIndicesQueryParams,
        List[FMPMarketIndicesData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPMarketIndicesQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

<<<<<<< HEAD
        return FMPMarketIndicesQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
=======
        return FMPMarketIndicesQueryParams.model_validate(transformed_params)

    @staticmethod
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPMarketIndicesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"
<<<<<<< HEAD
        query_str = get_querystring(query.model_dump(), ["symbol", "interval"])
=======
        query_str = get_querystring(query.model_dump(), ["symbol", "interval", "sort"])
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        url_params = f"{query.symbol}?{query_str}&apikey={api_key}"
        url = f"{base_url}/historical-chart/{query.interval}/{url_params}"

<<<<<<< HEAD
        if query.interval == "1day":
            url = f"{base_url}/historical-chart/1day/{query.symbol}?apikey={api_key}"

        return get_data_many(url, "historical", **kwargs)
=======
        return await get_data_many(url, "historical", **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPMarketIndicesQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPMarketIndicesData]:
        """Return the transformed data."""
<<<<<<< HEAD
=======
        if query.sort == "asc":
            data = sorted(data, key=lambda x: x["date"], reverse=True)

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return [FMPMarketIndicesData.model_validate(d) for d in data]
