"""FMP Historical Dividends Model."""

<<<<<<< HEAD
from datetime import date as dateType
from typing import Any, Dict, List, Optional

=======
from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Dict, List, Optional

from dateutil import parser
from dateutil.relativedelta import relativedelta
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.historical_dividends import (
    HistoricalDividendsData,
    HistoricalDividendsQueryParams,
)
from openbb_fmp.utils.helpers import create_url, get_data_many
from pydantic import Field, field_validator


class FMPHistoricalDividendsQueryParams(HistoricalDividendsQueryParams):
    """FMP Historical Dividends Query.

    Source: https://site.financialmodelingprep.com/developer/docs/#Historical-Dividends
    """


class FMPHistoricalDividendsData(HistoricalDividendsData):
    """FMP Historical Dividends Data."""

    label: str = Field(description="Label of the historical dividends.")
    adj_dividend: float = Field(
        description="Adjusted dividend of the historical dividends."
    )
    record_date: Optional[dateType] = Field(
        default=None,
        description="Record date of the historical dividends.",
    )
    payment_date: Optional[dateType] = Field(
        default=None,
        description="Payment date of the historical dividends.",
    )
    declaration_date: Optional[dateType] = Field(
        default=None,
        description="Declaration date of the historical dividends.",
    )

    @field_validator(
        "declaration_date",
        "record_date",
        "payment_date",
        mode="before",
        check_fields=False,
    )
    @classmethod
    def date_validate(cls, v: str):  # pylint: disable=E0213
        """Validate dates."""
        if not isinstance(v, str):
            return v
        return dateType.fromisoformat(v) if v else None


class FMPHistoricalDividendsFetcher(
    Fetcher[
        FMPHistoricalDividendsQueryParams,
        List[FMPHistoricalDividendsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPHistoricalDividendsQueryParams:
        """Transform the query params."""
<<<<<<< HEAD
        return FMPHistoricalDividendsQueryParams(**params)

    @staticmethod
    def extract_data(
=======
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(year=1)
        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return FMPHistoricalDividendsQueryParams(**params)

    @staticmethod
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPHistoricalDividendsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(
            3, f"historical-price-full/stock_dividend/{query.symbol}", api_key
        )
<<<<<<< HEAD
        return get_data_many(url, "historical", **kwargs)
=======
        return await get_data_many(url, "historical", **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPHistoricalDividendsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPHistoricalDividendsData]:
        """Return the transformed data."""
<<<<<<< HEAD
        return [FMPHistoricalDividendsData.model_validate(d) for d in data]
=======
        result = []
        for d in data:
            if "date" in d:
                dt = parser.parse(str(d["date"])).date()

                if query.start_date <= dt <= query.end_date:
                    result.append(FMPHistoricalDividendsData(**d))
            else:
                result.append(FMPHistoricalDividendsData(**d))
        return result
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
