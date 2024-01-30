"""Equity Historical Price Standard Model."""

<<<<<<< HEAD

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import (
    date as dateType,
    datetime,
)
from typing import List, Optional, Set, Union

from dateutil import parser
<<<<<<< HEAD
from pydantic import Field, PositiveFloat, field_validator
=======
from pydantic import Field, field_validator
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class EquityHistoricalQueryParams(QueryParams):
    """Equity Historical Price Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    interval: Optional[str] = Field(
        default="1d",
        description=QUERY_DESCRIPTIONS.get("interval", ""),
    )
    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EquityHistoricalData(Data):
    """Equity Historical Price Data."""

<<<<<<< HEAD
    date: datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: Union[float, int] = Field(description=DATA_DESCRIPTIONS.get("volume", ""))
    vwap: Optional[PositiveFloat] = Field(
=======
    date: Union[dateType, datetime] = Field(
        description=DATA_DESCRIPTIONS.get("date", "")
    )
    open: float = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: float = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: float = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: float = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: Optional[Union[float, int]] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    vwap: Optional[float] = Field(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        default=None, description=DATA_DESCRIPTIONS.get("vwap", "")
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
<<<<<<< HEAD
        return parser.isoparse(str(v))
=======
        v = parser.isoparse(str(v))
        if v.hour == 0 and v.minute == 0:
            return v.date()
        return v
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
