"""Euro Area Yield Curve Standard Model."""

<<<<<<< HEAD

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import date as dateType
from typing import Literal, Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS


class EUYieldCurveQueryParams(QueryParams):
    """Euro Area Yield Curve Query."""

    date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("date", "")
    )
<<<<<<< HEAD
    yield_curve_type: Literal[
        "spot_rate", "instantaneous_forward", "par_yield"
    ] = Field(
        default="spot_rate",
        description="The yield curve type.",
=======
    yield_curve_type: Literal["spot_rate", "instantaneous_forward", "par_yield"] = (
        Field(
            default="spot_rate",
            description="The yield curve type.",
        )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class EUYieldCurveData(Data):
    """Euro Area Yield Curve Data."""

    maturity: str = Field(description="Yield curve rate maturity.")
    rate: Optional[float] = Field(description="Yield curve rate.", default=None)
