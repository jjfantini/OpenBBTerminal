"""ETF Holdings Standard Model."""

from typing import Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class EtfHoldingsQueryParams(QueryParams):
    """ETF Holdings Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")


class EtfHoldingsData(Data):
    """ETF Holdings Data."""

    symbol: Optional[str] = Field(
<<<<<<< HEAD
        description=DATA_DESCRIPTIONS.get("symbol", "") + " (ETF)"
    )
    name: Optional[str] = Field(description="Name of the ETF holding.")
=======
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "") + " (ETF)"
    )
    name: Optional[str] = Field(
        default=None,
        description="Name of the ETF holding.",
    )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
