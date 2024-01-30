<<<<<<< HEAD
"""CBOE Available Indices Model."""
=======
"""Cboe Available Indices Model."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from datetime import time
from typing import Any, Dict, List, Optional

<<<<<<< HEAD
from openbb_cboe.utils.helpers import Europe, get_cboe_index_directory
=======
from openbb_cboe.utils.helpers import get_index_directory
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.available_indices import (
    AvailableIndicesData,
    AvailableIndicesQueryParams,
)
from pydantic import Field


class CboeAvailableIndicesQueryParams(AvailableIndicesQueryParams):
<<<<<<< HEAD
    """CBOE Available Indices Query.

    Source: https://www.cboe.com/europe/indices/
    """

    europe: bool = Field(
        description="Filter for European indices. False for US indices.", default=False
=======
    """Cboe Available Indices Query.

    Source: https://www.cboe.com/
    """

    use_cache: bool = Field(
        default=True,
        description="When True, the Cboe Index directory will be cached for 24 hours."
        + " Set as False to bypass.",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class CboeAvailableIndicesData(AvailableIndicesData):
<<<<<<< HEAD
    """CBOE Available Indices Data.

    Source: https://www.cboe.com/europe/indices/
    """

    isin: Optional[str] = Field(
        default=None,
        description="ISIN code for the index. Valid only for European indices.",
    )

    region: Optional[str] = Field(
        default=None,
        description="Region for the index. Valid only for European indices",
    )
=======
    """Cboe Available Indices Data.

    Source: https://www.cboe.com/
    """

    __alias_dict__ = {
        "symbol": "index_symbol",
        "data_delay": "mkt_data_delay",
        "open_time": "calc_start_time",
        "close_time": "calc_end_time",
    }
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    symbol: Optional[str] = Field(description="Symbol for the index.")

    description: Optional[str] = Field(
        default=None,
        description="Description for the index. Valid only for US indices.",
    )

    data_delay: Optional[int] = Field(
        default=None, description="Data delay for the index. Valid only for US indices."
    )

    open_time: Optional[time] = Field(
        default=None,
        description="Opening time for the index. Valid only for US indices.",
    )

    close_time: Optional[time] = Field(
        default=None,
        description="Closing time for the index. Valid only for US indices.",
    )

    time_zone: Optional[str] = Field(
        default=None, description="Time zone for the index. Valid only for US indices."
    )

    tick_days: Optional[str] = Field(
        default=None,
        description="The trading days for the index. Valid only for US indices.",
    )

    tick_frequency: Optional[str] = Field(
        default=None,
        description="The frequency of the index ticks. Valid only for US indices.",
    )

    tick_period: Optional[str] = Field(
        default=None,
        description="The period of the index ticks. Valid only for US indices.",
    )


class CboeAvailableIndicesFetcher(
    Fetcher[
        CboeAvailableIndicesQueryParams,
        List[CboeAvailableIndicesData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CboeAvailableIndicesQueryParams:
        """Transform the query params."""
        return CboeAvailableIndicesQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: CboeAvailableIndicesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the CBOE endpoint."""
<<<<<<< HEAD
        if query.europe is True:
            return Europe.list_indices()
        return get_cboe_index_directory().sort_index().reset_index().to_dict("records")
=======

        data = await get_index_directory(use_cache=query.use_cache, **kwargs)
        return data.to_dict("records")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: CboeAvailableIndicesQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[CboeAvailableIndicesData]:
        """Transform the data to the standard format."""
        return [CboeAvailableIndicesData.model_validate(d) for d in data]
