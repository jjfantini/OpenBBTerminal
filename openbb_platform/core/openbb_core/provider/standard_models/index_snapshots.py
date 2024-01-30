"""Index Snapshots Standard Model."""

<<<<<<< HEAD
from typing import Literal, Optional
=======
from typing import Optional
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS


class IndexSnapshotsQueryParams(QueryParams):
    """Index Snapshots Query."""

<<<<<<< HEAD
    region: Optional[Literal["US", "EU"]] = Field(
        description="The region to return. Currently supports US and EU.", default="US"
=======
    region: Optional[str] = Field(
        default=None, description="The region to return data for - i.e. 'us' or 'eu'."
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class IndexSnapshotsData(Data):
    """Index Snapshots Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: Optional[str] = Field(default=None, description="Name of the index.")
    currency: Optional[str] = Field(default=None, description="Currency of the index.")
    price: Optional[float] = Field(
        default=None, description="Current price of the index."
    )
    open: Optional[float] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("open", "")
    )
    high: Optional[float] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("high", "")
    )
    low: Optional[float] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("low", "")
    )
    close: Optional[float] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("close", "")
    )
<<<<<<< HEAD
    prev_close: Optional[float] = Field(
        default=None, description="Previous closing price of the index."
    )
    change: Optional[float] = Field(default=None, description="Change of the index.")
    change_percent: Optional[float] = Field(
        default=None, description="Change percent of the index."
=======
    volume: Optional[int] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    prev_close: Optional[float] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("prev_close", "")
    )
    change: Optional[float] = Field(
        default=None, description="Change in value of the index."
    )
    change_percent: Optional[float] = Field(
        default=None,
        description="Change, in normalized percentage points, of the index.",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )
