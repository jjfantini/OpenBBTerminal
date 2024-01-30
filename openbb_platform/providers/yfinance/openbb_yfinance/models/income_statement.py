"""Yahoo Finance Income Statement Model."""

import json
from datetime import datetime
<<<<<<< HEAD
from typing import Any, Dict, List, Optional
=======
from typing import Any, Dict, List, Literal, Optional
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.income_statement import (
    IncomeStatementData,
    IncomeStatementQueryParams,
)
<<<<<<< HEAD
from pydantic import field_validator
=======
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import to_snake_case
from pydantic import Field, field_validator
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from yfinance import Ticker


class YFinanceIncomeStatementQueryParams(IncomeStatementQueryParams):
    """Yahoo Finance Income Statement Query.

    Source: https://finance.yahoo.com/
    """

<<<<<<< HEAD
=======
    period: Optional[Literal["annual", "quarter"]] = Field(default="annual")

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class YFinanceIncomeStatementData(IncomeStatementData):
    """Yahoo Finance Income Statement Data."""

<<<<<<< HEAD
    # TODO: Standardize the fields
    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
=======
    __alias_dict__ = {
        "selling_general_and_admin_expense": "selling_general_and_administration",
        "research_and_development_expense": "research_and_development",
        "total_pre_tax_income": "pretax_income",
        "net_income_attributable_to_common_shareholders": "net_income_common_stockholders",
        "weighted_average_basic_shares_outstanding": "basic_average_shares",
        "weighted_average_diluted_shares_outstanding": "diluted_average_shares",
        "basic_earnings_per_share": "basic_eps",
        "diluted_earnings_per_share": "diluted_eps",
    }

    @field_validator("period_ending", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Validate the date field."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S").date()
        return v


class YFinanceIncomeStatementFetcher(
    Fetcher[
        YFinanceIncomeStatementQueryParams,
        List[YFinanceIncomeStatementData],
    ]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFinanceIncomeStatementQueryParams:
<<<<<<< HEAD
=======
        """Transform the query parameters."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return YFinanceIncomeStatementQueryParams(**params)

    @staticmethod
    def extract_data(
<<<<<<< HEAD
=======
        # pylint: disable=unused-argument
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: YFinanceIncomeStatementQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[YFinanceIncomeStatementData]:
<<<<<<< HEAD
=======
        """Extract the data from the Yahoo Finance endpoints."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        period = "yearly" if query.period == "annual" else "quarterly"
        data = Ticker(query.symbol).get_income_stmt(
            as_dict=False, pretty=False, freq=period
        )
<<<<<<< HEAD
        data = data.convert_dtypes().fillna(0).to_dict()
        data = [{"date": str(key), **value} for key, value in data.items()]
        # To match standardization
        for d in data:
            d["Symbol"] = query.symbol
=======
        if data is None:
            raise EmptyDataError()
        data.index = [to_snake_case(i) for i in data.index]
        data = data.reset_index().sort_index(ascending=False).set_index("index")
        data = data.convert_dtypes().fillna(0).replace(0, None).to_dict()
        data = [{"period_ending": str(key), **value} for key, value in data.items()]

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        data = json.loads(json.dumps(data))

        return data

    @staticmethod
    def transform_data(
        query: YFinanceIncomeStatementQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[YFinanceIncomeStatementData]:
<<<<<<< HEAD
=======
        """Transform the data."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return [YFinanceIncomeStatementData.model_validate(d) for d in data]
