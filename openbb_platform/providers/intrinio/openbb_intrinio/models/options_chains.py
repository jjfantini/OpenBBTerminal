"""Intrinio Options Chains Model."""

<<<<<<< HEAD
from concurrent.futures import ThreadPoolExecutor
=======
# pylint: disable=unused-argument
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import (
    date as dateType,
    datetime,
    timedelta,
)
<<<<<<< HEAD
from itertools import repeat
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from typing import Any, Dict, List, Optional

from dateutil import parser
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.options_chains import (
    OptionsChainsData,
    OptionsChainsQueryParams,
)
<<<<<<< HEAD
=======
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    amake_requests,
)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_intrinio.utils.helpers import get_data_many, get_weekday
from pydantic import Field, field_validator


class IntrinioOptionsChainsQueryParams(OptionsChainsQueryParams):
    """Intrinio Options Chains Query.

    source: https://docs.intrinio.com/documentation/web_api/get_options_chain_eod_v2
    """

    date: Optional[dateType] = Field(
<<<<<<< HEAD
        description="Date for which the options chains are returned."
=======
        default=None, description="The end-of-day date for options chains data."
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class IntrinioOptionsChainsData(OptionsChainsData):
    """Intrinio Options Chains Data."""

    __alias_dict__ = {
        "contract_symbol": "code",
        "symbol": "ticker",
        "eod_date": "date",
        "option_type": "type",
    }

<<<<<<< HEAD
    @field_validator("expiration", "date", mode="before", check_fields=False)
=======
    exercise_style: Optional[str] = Field(
        default=None,
        description="The exercise style of the option, American or European.",
    )

    @field_validator(
        "date",
        "close_time",
        "close_ask_time",
        "close_bid_time",
        mode="before",
        check_fields=False,
    )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime object from the date string."""
        # only pass it to the parser if it is not a datetime object
        if isinstance(v, str):
            return parser.parse(v)
<<<<<<< HEAD
=======
        return v
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class IntrinioOptionsChainsFetcher(
    Fetcher[IntrinioOptionsChainsQueryParams, List[IntrinioOptionsChainsData]]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioOptionsChainsQueryParams:
        """Transform the query."""
<<<<<<< HEAD
        transform_params = params

        now = datetime.now().date()
        if params.get("date") is None:
            transform_params["date"] = (now - timedelta(days=1)).strftime("%Y-%m-%d")
        elif isinstance(params["date"], dateType):
            transform_params["date"] = params["date"].strftime("%Y-%m-%d")
        else:
            transform_params["date"] = parser.parse(params["date"]).date()
=======
        transform_params = params.copy()
        if params.get("date") is not None:
            if isinstance(params["date"], dateType):
                transform_params["date"] = params["date"].strftime("%Y-%m-%d")
            else:
                transform_params["date"] = parser.parse(params["date"]).date()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        return IntrinioOptionsChainsQueryParams(**transform_params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: IntrinioOptionsChainsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""

<<<<<<< HEAD
        data: List = []
        base_url = "https://api-v2.intrinio.com/options"

        def get_options_chains(
            expiration: str, data: List[IntrinioOptionsChainsData]
        ) -> None:
            """Return the data for the given expiration."""
            url = (
                f"{base_url}/chain/{query.symbol}/{expiration}/eod?"
                f"date={query.date}&api_key={api_key}"
            )
            response = get_data_many(url, "chain", **kwargs)
            data.extend(response)

        def get_data(date: str) -> None:
            """Fetch data for a given date using ThreadPoolExecutor."""
=======
        base_url = "https://api-v2.intrinio.com/options"

        async def get_urls(date: str) -> List[str]:
            """Return the urls for the given date."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            url = (
                f"{base_url}/expirations/{query.symbol}/eod?"
                f"after={date}&api_key={api_key}"
            )
<<<<<<< HEAD
            expirations = get_data_many(url, "expirations", **kwargs)

            with ThreadPoolExecutor() as executor:
                executor.map(get_options_chains, expirations, repeat(data))

        date = get_weekday(query.date)
        get_data(date)

        if not data:
            date = get_weekday(query.date - timedelta(days=1))
            get_data(date)

        return data
=======
            expirations = await get_data_many(url, "expirations", **kwargs)

            def generate_url(expiration) -> str:
                url = f"{base_url}/chain/{query.symbol}/{expiration}/eod?date="
                if query.date is not None:
                    url += date
                return url + f"&api_key={api_key}"

            return [generate_url(expiration) for expiration in expirations]

        async def callback(response: ClientResponse, _: Any) -> list:
            """Return the response."""
            response_data = await response.json()
            return response_data.get("chain", [])

        date = datetime.now().date() if query.date is None else query.date
        date = get_weekday(date)

        results = await amake_requests(
            await get_urls(date.strftime("%Y-%m-%d")), callback, **kwargs
        )

        if not results:
            urls = await get_urls(
                get_weekday(date - timedelta(days=1)).strftime("%Y-%m-%d")
            )
            results = await amake_requests(urls, response_callback=callback, **kwargs)

        return results
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: IntrinioOptionsChainsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[IntrinioOptionsChainsData]:
        """Return the transformed data."""
        data = [{**item["option"], **item["prices"]} for item in data]
<<<<<<< HEAD
=======
        data = sorted(
            data, key=lambda x: (x["expiration"], x["strike"], x["type"]), reverse=False
        )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return [IntrinioOptionsChainsData.model_validate(d) for d in data]
