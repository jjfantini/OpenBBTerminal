"""FMP Currency Historical Price Model."""

<<<<<<< HEAD

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.currency_historical import (
    CurrencyHistoricalData,
    CurrencyHistoricalQueryParams,
)
<<<<<<< HEAD
=======
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_fmp.utils.helpers import get_data_many, get_querystring
from pydantic import Field


class FMPCurrencyHistoricalQueryParams(CurrencyHistoricalQueryParams):
    """FMP Currency Historical Price Query.

    Source: https://site.financialmodelingprep.com/developer/docs/#Historical-Forex-Price
    """

<<<<<<< HEAD
    interval: Literal[
        "1min", "5min", "15min", "30min", "1hour", "4hour", "1day"
    ] = Field(default="1day", description="Data granularity.")
=======
    __alias_dict__ = {"start_date": "from", "end_date": "to"}

    interval: Literal["1min", "5min", "15min", "30min", "1hour", "4hour", "1day"] = (
        Field(default="1day", description="Data granularity.")
    )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class FMPCurrencyHistoricalData(CurrencyHistoricalData):
    """FMP Currency Historical Price Data."""

    adj_close: Optional[float] = Field(
<<<<<<< HEAD
        default=None, description="Adjusted Close Price of the symbol."
=======
        default=None, description=DATA_DESCRIPTIONS.get("adj_close", "")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )
    unadjusted_volume: Optional[float] = Field(
        default=None, description="Unadjusted volume of the symbol."
    )
    change: Optional[float] = Field(
        default=None,
        description="Change in the price of the symbol from the previous day.",
    )
    change_percent: Optional[float] = Field(
        default=None, description="Change % in the price of the symbol."
    )
    label: Optional[str] = Field(
        default=None, description="Human readable format of the date."
    )
    change_over_time: Optional[float] = Field(
        default=None,
        description="Change % in the price of the symbol over a period of time.",
    )


class FMPCurrencyHistoricalFetcher(
    Fetcher[
        FMPCurrencyHistoricalQueryParams,
        List[FMPCurrencyHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCurrencyHistoricalQueryParams:
        """Transform the query params. Start and end dates are set to a 1 year interval."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return FMPCurrencyHistoricalQueryParams(**transformed_params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPCurrencyHistoricalQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"
<<<<<<< HEAD
        query_str = (
            get_querystring(query.model_dump(), ["symbol"])
            .replace("start_date", "from")
            .replace("end_date", "to")
        )
=======
        query_str = get_querystring(query.model_dump(), ["symbol"])
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        url_params = f"{query.symbol}?{query_str}&apikey={api_key}"
        url = f"{base_url}/historical-chart/{query.interval}/{url_params}"

        if query.interval == "1day":
            url = f"{base_url}/historical-price-full/forex/{url_params}"

<<<<<<< HEAD
        return get_data_many(url, "historical", **kwargs)
=======
        return await get_data_many(url, "historical", **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPCurrencyHistoricalQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPCurrencyHistoricalData]:
        """Return the transformed data."""
<<<<<<< HEAD
=======
        # pylint: disable=unused-argument
        data = [
            d
            for d in data
            if d.get("vwap") != 0
            and d.get("change") != 0
            and d.get("changeOverTime") != 0
        ]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return [FMPCurrencyHistoricalData.model_validate(d) for d in data]
