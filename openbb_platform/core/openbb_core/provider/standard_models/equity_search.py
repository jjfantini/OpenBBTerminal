"""Equity Search Standard Model."""

<<<<<<< HEAD
from typing import List, Set, Union

from pydantic import Field, field_validator
=======
from typing import Optional

from pydantic import Field
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS


class EquitySearchQueryParams(QueryParams):
    """Equity Search Query."""

    query: str = Field(description="Search query.", default="")
    is_symbol: bool = Field(
        description="Whether to search by ticker symbol.", default=False
    )


class EquitySearchData(Data):
    """Equity Search Data."""

<<<<<<< HEAD
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="Name of the company.")

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])
=======
    symbol: Optional[str] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    name: str = Field(description="Name of the company.")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
