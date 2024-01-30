"""Crypto Search Standard Model."""

from typing import Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS


class CryptoSearchQueryParams(QueryParams):
    """Crypto Search Query."""

<<<<<<< HEAD
    query: Optional[str] = Field(description="Search query.", default="")
=======
    query: Optional[str] = Field(description="Search query.", default=None)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class CryptoSearchData(Data):
    """Crypto Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + " (Crypto)")
    name: Optional[str] = Field(description="Name of the crypto.", default=None)
