"""Available Indices Standard Model."""

<<<<<<< HEAD

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from typing import Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class AvailableIndicesQueryParams(QueryParams):
    """Available Indices Query."""


class AvailableIndicesData(Data):
    """Available Indices Data.

    Returns the list of available indices from a provider.
    """

    name: Optional[str] = Field(default=None, description="Name of the index.")
    currency: Optional[str] = Field(
        default=None, description="Currency the index is traded in."
    )
