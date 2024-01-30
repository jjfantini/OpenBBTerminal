"""CBOE Index Snapshots Model."""

from datetime import datetime
<<<<<<< HEAD
from typing import Any, Dict, List, Optional

import pandas as pd
from openbb_cboe.utils.helpers import (
    EUR_INDEX_COLUMNS,
    US_INDEX_COLUMNS,
    Europe,
    get_cboe_directory,
    get_cboe_index_directory,
)
=======
from typing import Any, Dict, List, Literal, Optional

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.index_snapshots import (
    IndexSnapshotsData,
    IndexSnapshotsQueryParams,
)
<<<<<<< HEAD
from openbb_core.provider.utils.helpers import make_request
from pydantic import Field
=======
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import amake_request
from pandas import DataFrame
from pydantic import Field, field_validator
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class CboeIndexSnapshotsQueryParams(IndexSnapshotsQueryParams):
    """CBOE Index Snapshots Query.

    Source: https://www.cboe.com/
    """

<<<<<<< HEAD
=======
    region: Literal[None, "us", "eu"] = Field(
        default="us",
    )

    @field_validator("region", mode="after", check_fields=False)
    @classmethod
    def validate_region(cls, v: str):
        """Validate region."""
        return "us" if v is None else v

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class CboeIndexSnapshotsData(IndexSnapshotsData):
    """CBOE Index Snapshots Data."""

<<<<<<< HEAD
    isin: Optional[str] = Field(
        default=None,
        description="ISIN code for the index. Valid only for European indices.",
    )
    last_trade_timestamp: Optional[datetime] = Field(
        default=None, description="Last trade timestamp for the index."
=======
    __alias_dict__ = {
        "prev_close": "prev_day_close",
        "change": "price_change",
        "change_percent": "price_change_percent",
        "price": "current_price",
    }
    bid: Optional[float] = Field(default=None, description="Current bid price.")
    ask: Optional[float] = Field(default=None, description="Current ask price.")
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
    volume: Optional[int] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    prev_close: Optional[float] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("prev_close", "")
    )
    change: Optional[float] = Field(default=None, description="Change in price.")
    change_percent: Optional[float] = Field(
        default=None, description="Change in price as a normalized percentage."
    )
    last_trade_time: Optional[datetime] = Field(
        default=None, description="Last trade timestamp for the symbol."
    )
    status: Optional[str] = Field(
        default=None, description="Status of the market, open or closed."
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class CboeIndexSnapshotsFetcher(
    Fetcher[
        CboeIndexSnapshotsQueryParams,
        List[CboeIndexSnapshotsData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints"""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CboeIndexSnapshotsQueryParams:
        """Transform the query."""
        return CboeIndexSnapshotsQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: CboeIndexSnapshotsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
<<<<<<< HEAD
        """Return the raw data from the CBOE endpoint"""
        data = pd.DataFrame()

        if query.region == "US":
            r = make_request(
                "https://cdn.cboe.com/api/global/delayed_quotes/quotes/all_us_indices.json"
            )

            if r.status_code != 200:
                raise RuntimeError(r.status_code)

            INDEXES = pd.concat(
                [get_cboe_index_directory(), get_cboe_directory()], axis=0
            )
            data = pd.DataFrame.from_records(r.json()["data"])

            data.rename(columns=US_INDEX_COLUMNS, inplace=True)
            data["symbol"] = data["symbol"].str.replace("^", "")
            data["name"] = ""
            data = data.set_index("symbol")
            for i in data.index:
                if i in INDEXES.index:
                    data.at[i, "name"] = INDEXES.at[i, "name"]

            data["name"] = data["name"].astype(str)
            data["currency"] = "USD"
            data = data[
                [
                    "name",
                    "price",
                    "prev_close",
                    "change",
                    "change_percent",
                    "open",
                    "high",
                    "low",
                    "close",
                    "currency",
                    "last_trade_timestamp",
                ]
            ]

        if query.region == "EU":
            r = make_request(
                "https://cdn.cboe.com/api/global/european_indices/index_quotes/all-indices.json"
            )

            if r.status_code != 200:
                raise RuntimeError(r.status_code)

            data = (
                pd.DataFrame.from_records(r.json()["data"])
                .drop(columns=["symbol"])
                .rename(columns={"index": "symbol"})
                .set_index("symbol")
                .round(2)
            )

            INDEXES = pd.DataFrame(Europe.list_indices()).set_index("symbol")

            for i in data.index:
                data.loc[i, ("isin")] = INDEXES.at[i, "isin"]
                data.loc[i, ("name")] = INDEXES.at[i, "name"]
                data.loc[i, ("currency")] = INDEXES.at[i, "currency"]

            data = data[list(EUR_INDEX_COLUMNS.keys())]
            data.columns = list(EUR_INDEX_COLUMNS.values())

        data["change_percent"] = data["change_percent"].fillna(0.0)

        return data.reset_index().to_dict("records")
=======
        """Return the raw data from the Cboe endpoint"""

        if query.region == "us":
            url = "https://cdn.cboe.com/api/global/delayed_quotes/quotes/all_us_indices.json"
        if query.region == "eu":
            url = "https://cdn.cboe.com/api/global/european_indices/index_quotes/all-indices.json"

        data = await amake_request(url, **kwargs)
        return data.get("data")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: CboeIndexSnapshotsQueryParams, data: dict, **kwargs: Any
    ) -> List[CboeIndexSnapshotsData]:
        """Transform the data to the standard format"""
<<<<<<< HEAD
        for item in data:
            item["name"] = item["name"].replace("/", "-")

        return [CboeIndexSnapshotsData.model_validate(d) for d in data]
=======
        if not data:
            raise EmptyDataError()
        data = DataFrame(data)
        percent_cols = [
            "price_change_percent",
            "iv30",
            "iv30_change",
            "iv30_change_percent",
        ]
        for col in percent_cols:
            if col in data.columns:
                data[col] = round(data[col] / 100, 6)
        data = (
            data.replace(0, None)
            .replace("", None)
            .dropna(how="all", axis=1)
            .fillna("N/A")
            .replace("N/A", None)
        )
        drop_cols = [
            "exchange_id",
            "seqno",
            "index",
            "security_type",
            "ask_size",
            "bid_size",
        ]
        for col in drop_cols:
            if col in data.columns:
                data = data.drop(columns=col)
        return [
            CboeIndexSnapshotsData.model_validate(d)
            for d in data.to_dict(orient="records")
        ]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
