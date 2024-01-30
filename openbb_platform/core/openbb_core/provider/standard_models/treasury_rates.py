"""Treasury Rates Standard Model."""

<<<<<<< HEAD

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class TreasuryRatesQueryParams(QueryParams):
    """Treasury Rates Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class TreasuryRatesData(Data):
    """Treasury Rates Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
<<<<<<< HEAD
    month_1: float = Field(description="1 month treasury rate.")
    month_2: float = Field(description="2 month treasury rate.")
    month_3: float = Field(description="3 month treasury rate.")
    month_6: float = Field(description="6 month treasury rate.")
    year_1: float = Field(description="1 year treasury rate.")
    year_2: float = Field(description="2 year treasury rate.")
    year_3: float = Field(description="3 year treasury rate.")
    year_5: float = Field(description="5 year treasury rate.")
    year_7: float = Field(description="7 year treasury rate.")
    year_10: float = Field(description="10 year treasury rate.")
    year_20: float = Field(description="20 year treasury rate.")
    year_30: float = Field(description="30 year treasury rate.")
=======
    month_1: Optional[float] = Field(description="1 month treasury rate.", default=None)
    month_2: Optional[float] = Field(description="2 month treasury rate.", default=None)
    month_3: Optional[float] = Field(description="3 month treasury rate.", default=None)
    month_6: Optional[float] = Field(description="6 month treasury rate.", default=None)
    year_1: Optional[float] = Field(description="1 year treasury rate.", default=None)
    year_2: Optional[float] = Field(description="2 year treasury rate.", default=None)
    year_3: Optional[float] = Field(description="3 year treasury rate.", default=None)
    year_5: Optional[float] = Field(description="5 year treasury rate.", default=None)
    year_7: Optional[float] = Field(description="7 year treasury rate.", default=None)
    year_10: Optional[float] = Field(description="10 year treasury rate.", default=None)
    year_20: Optional[float] = Field(description="20 year treasury rate.", default=None)
    year_30: Optional[float] = Field(description="30 year treasury rate.", default=None)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
