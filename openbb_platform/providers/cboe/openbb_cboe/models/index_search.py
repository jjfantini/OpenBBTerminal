"""CBOE Index Search Model."""

from datetime import time
from typing import Any, Dict, List, Optional

<<<<<<< HEAD
import pandas as pd
from openbb_cboe.utils.helpers import Europe, get_cboe_index_directory
=======
from openbb_cboe.utils.helpers import get_index_directory
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_search import (
    IndexSearchData,
    IndexSearchQueryParams,
)
from pydantic import Field


class CboeIndexSearchQueryParams(IndexSearchQueryParams):
    """CBOE Index Search Query.

    Source: https://www.cboe.com/
    """

<<<<<<< HEAD
    europe: bool = Field(
        description="Filter for European indices. False for US indices.", default=False
=======
    use_cache: bool = Field(
        default=True,
        description="When True, the Cboe Index directory will be cached for 24 hours."
        + " Set as False to bypass.",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class CboeIndexSearchData(IndexSearchData):
    """CBOE Index Search Data."""

<<<<<<< HEAD
    isin: Optional[str] = Field(
        description="ISIN code for the index. Valid only for European indices.",
        default=None,
    )
    region: Optional[str] = Field(
        description="Region for the index. Valid only for European indices",
        default=None,
    )
=======
    __alias_dict__ = {
        "symbol": "index_symbol",
        "data_delay": "mkt_data_delay",
        "open_time": "calc_start_time",
        "close_time": "calc_end_time",
    }

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    description: Optional[str] = Field(
        description="Description for the index.", default=None
    )
    data_delay: Optional[int] = Field(
        description="Data delay for the index. Valid only for US indices.", default=None
    )
    currency: Optional[str] = Field(description="Currency for the index.", default=None)
    time_zone: Optional[str] = Field(
        description="Time zone for the index. Valid only for US indices.", default=None
    )
    open_time: Optional[time] = Field(
        description="Opening time for the index. Valid only for US indices.",
        default=None,
    )
    close_time: Optional[time] = Field(
        description="Closing time for the index. Valid only for US indices.",
        default=None,
    )
    tick_days: Optional[str] = Field(
        description="The trading days for the index. Valid only for US indices.",
        default=None,
    )
    tick_frequency: Optional[str] = Field(
        description="Tick frequency for the index. Valid only for US indices.",
        default=None,
    )
    tick_period: Optional[str] = Field(
        description="Tick period for the index. Valid only for US indices.",
        default=None,
    )


class CboeIndexSearchFetcher(
    Fetcher[
        CboeIndexSearchQueryParams,
        List[CboeIndexSearchData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CboeIndexSearchQueryParams:
        """Transform the query."""
        return CboeIndexSearchQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: CboeIndexSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the CBOE endpoint."""
<<<<<<< HEAD
        symbols = pd.DataFrame()
        if query.europe is True:
            symbols = pd.DataFrame(Europe.list_indices())
        if query.europe is False:
            symbols = get_cboe_index_directory().reset_index()

        target = "name" if not query.is_symbol else "symbol"
        idx = symbols[target].str.contains(query.query, case=False)
        result = symbols[idx]
=======

        symbols = await get_index_directory(use_cache=query.use_cache, **kwargs)
        symbols.drop(columns=["source"], inplace=True)
        if query.is_symbol is True:
            result = symbols[
                symbols["index_symbol"].str.contains(query.query, case=False)
            ]
        else:
            result = symbols[
                symbols["name"].str.contains(query.query, case=False)
                | symbols["index_symbol"].str.contains(query.query, case=False)
                | symbols["description"].str.contains(query.query, case=False)
            ]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        return result.to_dict("records")

    @staticmethod
    def transform_data(
        query: CboeIndexSearchQueryParams, data: dict, **kwargs: Any
    ) -> List[CboeIndexSearchData]:
        """Transform the data to the standard format."""
        return [CboeIndexSearchData.model_validate(d) for d in data]
