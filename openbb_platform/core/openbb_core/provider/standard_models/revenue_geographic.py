"""Revenue by Geographic Segments Standard Model."""

<<<<<<< HEAD

from datetime import date as dateType
from typing import Dict, List, Literal, Optional, Set, Union
=======
import warnings
from datetime import date as dateType
from typing import Dict, Literal, Optional
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data, ForceInt
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
<<<<<<< HEAD
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)

=======
    QUERY_DESCRIPTIONS,
)

_warn = warnings.warn

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class RevenueGeographicQueryParams(QueryParams):
    """Revenue by Geographic Segments Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    period: Literal["quarter", "annual"] = Field(
        default="annual", description=QUERY_DESCRIPTIONS.get("period", "")
    )
    structure: Literal["hierarchical", "flat"] = Field(
        default="flat", description="Structure of the returned data."
    )  # should always be flat

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
<<<<<<< HEAD
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])
=======
    def upper_symbol(cls, v: str):
        """Convert symbol to uppercase."""
        if "," in v:
            _warn(
                f"{QUERY_DESCRIPTIONS.get('symbol_list_warning', '')} {v.split(',')[0].upper()}"
            )
        return v.split(",")[0].upper() if "," in v else v.upper()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class RevenueGeographicData(Data):
    """Revenue by Geographic Segments Data."""

<<<<<<< HEAD
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    geographic_segment: Dict[str, ForceInt] = Field(
        description="Day level data containing the revenue of the geographic segment."
    )
    americas: Optional[ForceInt] = Field(
        default=None, description="Revenue from the the American segment."
    )
    europe: Optional[ForceInt] = Field(
        default=None, description="Revenue from the the European segment."
    )
    greater_china: Optional[ForceInt] = Field(
        default=None, description="Revenue from the the Greater China segment."
    )
    japan: Optional[ForceInt] = Field(
        default=None, description="Revenue from the the Japan segment."
    )
    rest_of_asia_pacific: Optional[ForceInt] = Field(
        default=None, description="Revenue from the the Rest of Asia Pacific segment."
=======
    period_ending: dateType = Field(description="The end date of the reporting period.")
    fiscal_period: Optional[str] = Field(
        default=None, description="The fiscal period of the reporting period."
    )
    fiscal_year: Optional[int] = Field(
        default=None, description="The fiscal year of the reporting period."
    )
    filing_date: Optional[dateType] = Field(
        default=None, description="The filing date of the report."
    )
    geographic_segment: Dict[str, ForceInt] = Field(
        description="Dictionary of the revenue by geographic segment."
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )
