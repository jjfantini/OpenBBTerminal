"""Index Constituents Standard Model."""

<<<<<<< HEAD

from datetime import date
from typing import List, Literal, Optional, Set, Union
=======
from typing import List, Optional, Set, Union
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS


class IndexConstituentsQueryParams(QueryParams):
    """Index Constituents Query."""

<<<<<<< HEAD
    index: Literal["nasdaq", "sp500", "dowjones"] = Field(
        default="dowjones",
        description="Index for which we want to fetch the constituents.",
=======
    index: str = Field(
        description="Index to fetch the constituents of.",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class IndexConstituentsData(Data):
    """Index Constituents Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
<<<<<<< HEAD
    name: str = Field(description="Name of the constituent company in the index.")
    sector: str = Field(
        description="Sector the constituent company in the index belongs to."
    )
    sub_sector: Optional[str] = Field(
        default=None,
        description="Sub-sector the constituent company in the index belongs to.",
    )
    headquarter: Optional[str] = Field(
        default=None,
        description="Location of the headquarter of the constituent company in the index.",
    )
    date_first_added: Optional[Union[date, str]] = Field(
        default=None, description="Date the constituent company was added to the index."
    )
    cik: int = Field(
        description=DATA_DESCRIPTIONS.get("cik", ""),
    )
    founded: Optional[Union[date, str]] = Field(
        default=None,
        description="Founding year of the constituent company in the index.",
=======
    name: Optional[str] = Field(
        default=None, description="Name of the constituent company in the index."
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])
