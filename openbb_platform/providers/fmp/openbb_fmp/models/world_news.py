"""FMP World News Model."""

import math
from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.world_news import (
    WorldNewsData,
    WorldNewsQueryParams,
)
<<<<<<< HEAD
from openbb_fmp.utils.helpers import get_data_many
=======
from openbb_core.provider.utils.helpers import amake_requests
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from pydantic import Field, field_validator


class FMPWorldNewsQueryParams(WorldNewsQueryParams):
    """FMP World News Query.

    Source: https://site.financialmodelingprep.com/developer/docs/general-news-api/
    """


class FMPWorldNewsData(WorldNewsData):
    """FMP World News Data."""

    __alias_dict__ = {"date": "publishedDate", "images": "image"}

<<<<<<< HEAD
    site: str = Field(description="Site of the news.")
=======
    site: str = Field(description="News source.")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%fZ")


class FMPWorldNewsFetcher(
    Fetcher[
        FMPWorldNewsQueryParams,
        List[FMPWorldNewsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPWorldNewsQueryParams:
        """Transform the query params."""
        return FMPWorldNewsQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPWorldNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""
<<<<<<< HEAD

        base_url = "https://financialmodelingprep.com/api/v4"

        pages = math.ceil(query.limit / 20)
        data = []

        for page in range(pages):
            url = f"{base_url}/general_news?page={page}&apikey={api_key}"
            response = get_data_many(url, **kwargs)
            data.extend(response)

        data = sorted(data, key=lambda x: x["publishedDate"], reverse=True)
        data = data[: query.limit]

        return data
=======
        pages = math.ceil(query.limit / 20)

        base_url = "https://financialmodelingprep.com/api/v4"

        urls = [
            f"{base_url}/general_news?page={page}&apikey={api_key}"
            for page in range(pages)
        ]

        response = await amake_requests(urls, **kwargs)
        data = sorted(response, key=lambda x: x["publishedDate"], reverse=True)

        return data[: query.limit]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPWorldNewsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPWorldNewsData]:
        """Return the transformed data."""
        for d in data:
            if isinstance(d["image"], str):
                d["image"] = [{"url": d["image"]}]

        return [FMPWorldNewsData.model_validate(d) for d in data]
