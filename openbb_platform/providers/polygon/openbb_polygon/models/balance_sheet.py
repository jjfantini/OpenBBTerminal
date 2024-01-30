"""Polygon Balance Sheet Statement Model."""

from datetime import date
from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.balance_sheet import (
    BalanceSheetData,
    BalanceSheetQueryParams,
)
from openbb_core.provider.utils.helpers import get_querystring
<<<<<<< HEAD
from openbb_polygon.utils.helpers import get_data
from pydantic import Field, field_validator
=======
from openbb_polygon.utils.helpers import get_data_many
from pydantic import Field
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class PolygonBalanceSheetQueryParams(BalanceSheetQueryParams):
    """Polygon Balance Sheet Statement Query.

    Source: https://polygon.io/docs/stocks#!/get_vx_reference_financials
    """

    __alias_dict__ = {"symbol": "ticker", "period": "timeframe"}

<<<<<<< HEAD
=======
    period: Literal["annual", "quarter", "ttm"] = Field(default="annual")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    filing_date: Optional[date] = Field(
        default=None, description="Filing date of the financial statement."
    )
    filing_date_lt: Optional[date] = Field(
        default=None, description="Filing date less than the given date."
    )
    filing_date_lte: Optional[date] = Field(
        default=None,
        description="Filing date less than or equal to the given date.",
    )
    filing_date_gt: Optional[date] = Field(
        default=None,
        description="Filing date greater than the given date.",
    )
    filing_date_gte: Optional[date] = Field(
        default=None,
        description="Filing date greater than or equal to the given date.",
    )
    period_of_report_date: Optional[date] = Field(
        default=None, description="Period of report date of the financial statement."
    )
    period_of_report_date_lt: Optional[date] = Field(
        default=None,
        description="Period of report date less than the given date.",
    )
    period_of_report_date_lte: Optional[date] = Field(
        default=None,
        description="Period of report date less than or equal to the given date.",
    )
    period_of_report_date_gt: Optional[date] = Field(
        default=None,
        description="Period of report date greater than the given date.",
    )
    period_of_report_date_gte: Optional[date] = Field(
        default=None,
        description="Period of report date greater than or equal to the given date.",
    )
<<<<<<< HEAD
    include_sources: Optional[bool] = Field(
        default=None,
=======
    include_sources: bool = Field(
        default=True,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        description="Whether to include the sources of the financial statement.",
    )
    order: Optional[Literal["asc", "desc"]] = Field(
        default=None, description="Order of the financial statement."
    )
    sort: Optional[Literal["filing_date", "period_of_report_date"]] = Field(
        default=None, description="Sort of the financial statement."
    )


class PolygonBalanceSheetData(BalanceSheetData):
    """Polygon Balance Sheet Statement Data."""

    __alias_dict__ = {
        "date": "start_date",
<<<<<<< HEAD
        "total_liabilities_and_stockholders_equity": "liabilities_and_equity",
=======
        "total_liabilities_and_stock_holders_equity": "liabilities_and_equity",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "minority_interest": "equity_attributable_to_noncontrolling_interest",
        "total_current_assets": "current_assets",
        "marketable_securities": "fixed_assets",
        "property_plant_equipment_net": "public_utilities_property_plant_and_equipment_net",
<<<<<<< HEAD
        "other_non_current_assets": "other_noncurrent_assets_of_regulated_entity",
        "total_non_current_assets": "noncurrent_assets",
        "total_assets": "assets",
        "total_current_liabilities": "current_liabilities",
        "other_non_current_liabilities": "other _noncurrent_liabilities_of_regulated_entity",
        "total_non_current_liabilities": "noncurrent_liabilities",
        "total_liabilities": "liabilities",
        "preferred_stock": "temporary_equity",
        "total_shareholder_equity": "temporary_equity_attributable_to_parent",
        "total_equity": "equity",
        "total_liabilities_and_shareholders_equity": "liabilities_and_equity",
    }

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def symbol_from_tickers(cls, v):
        """Return a list of symbols as a list."""
        if isinstance(v, list):
            return ",".join(v)
        return v
=======
        "other_non_current_assets": "other_noncurrent_assets",
        "total_non_current_assets": "noncurrent_assets",
        "total_assets": "assets",
        "total_current_liabilities": "current_liabilities",
        "other_non_current_liabilities": "other_noncurrent_liabilities",
        "total_non_current_liabilities": "noncurrent_liabilities",
        "total_liabilities": "liabilities",
        "total_stock_holders_equity": "equity_attributable_to_parent",
        "total_equity": "equity",
        "employee_wages": "wages",
        "redeemable_non_controlling_interest": "redeemable_noncontrolling_interest",
        "redeemable_non_controlling_interest_other": "redeemable_noncontrolling_interest_other",
    }

    accounts_receivable: Optional[int] = Field(
        description="Accounts receivable", default=None
    )
    marketable_securities: Optional[int] = Field(
        description="Marketable securities", default=None
    )
    prepaid_expenses: Optional[int] = Field(
        description="Prepaid expenses", default=None
    )
    other_current_assets: Optional[int] = Field(
        description="Other current assets", default=None
    )
    total_current_assets: Optional[int] = Field(
        description="Total current assets", default=None
    )
    property_plant_equipment_net: Optional[int] = Field(
        description="Property plant and equipment net", default=None
    )
    inventory: Optional[int] = Field(description="Inventory", default=None)
    other_non_current_assets: Optional[int] = Field(
        description="Other non-current assets", default=None
    )
    total_non_current_assets: Optional[int] = Field(
        description="Total non-current assets", default=None
    )
    intangible_assets: Optional[int] = Field(
        description="Intangible assets", default=None
    )
    total_assets: Optional[int] = Field(description="Total assets", default=None)
    accounts_payable: Optional[int] = Field(
        description="Accounts payable", default=None
    )
    employee_wages: Optional[int] = Field(description="Employee wages", default=None)
    other_current_liabilities: Optional[int] = Field(
        description="Other current liabilities", default=None
    )
    total_current_liabilities: Optional[int] = Field(
        description="Total current liabilities", default=None
    )
    other_non_current_liabilities: Optional[int] = Field(
        description="Other non-current liabilities", default=None
    )
    total_non_current_liabilities: Optional[int] = Field(
        description="Total non-current liabilities", default=None
    )
    long_term_debt: Optional[int] = Field(description="Long term debt", default=None)
    total_liabilities: Optional[int] = Field(
        description="Total liabilities", default=None
    )
    minority_interest: Optional[int] = Field(
        description="Minority interest", default=None
    )
    temporary_equity_attributable_to_parent: Optional[int] = Field(
        description="Temporary equity attributable to parent", default=None
    )
    equity_attributable_to_parent: Optional[int] = Field(
        description="Equity attributable to parent", default=None
    )
    temporary_equity: Optional[int] = Field(
        description="Temporary equity", default=None
    )
    preferred_stock: Optional[int] = Field(description="Preferred stock", default=None)
    redeemable_non_controlling_interest: Optional[int] = Field(
        description="Redeemable non-controlling interest", default=None
    )
    redeemable_non_controlling_interest_other: Optional[int] = Field(
        description="Redeemable non-controlling interest other", default=None
    )
    total_stock_holders_equity: Optional[int] = Field(
        description="Total stock holders equity", default=None
    )
    total_liabilities_and_stock_holders_equity: Optional[int] = Field(
        description="Total liabilities and stockholders equity", default=None
    )
    total_equity: Optional[int] = Field(description="Total equity", default=None)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class PolygonBalanceSheetFetcher(
    Fetcher[
        PolygonBalanceSheetQueryParams,
        List[PolygonBalanceSheetData],
    ]
):
    """Transform the query, extract and transform the data from the Polygon endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> PolygonBalanceSheetQueryParams:
        """Transform the query params."""
        return PolygonBalanceSheetQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
        query: PolygonBalanceSheetQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> dict:
=======
    async def aextract_data(
        query: PolygonBalanceSheetQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> Dict:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("polygon_api_key") if credentials else ""

        base_url = "https://api.polygon.io/vX/reference/financials"
        period = "quarterly" if query.period == "quarter" else query.period
        query_string = get_querystring(
<<<<<<< HEAD
            query.model_dump(by_alias=True), ["ticker", "period"]
        )

        if query.symbol.isdigit():
            query_string = f"cik={query.symbol}&period={period}&{query_string}"
        else:
            query_string = f"ticker={query.symbol}&period={period}&{query_string}"

        request_url = f"{base_url}?{query_string}&apiKey={api_key}"

        return get_data(request_url, **kwargs).get("results", [])
=======
            query.model_dump(by_alias=True), ["ticker", "timeframe"]
        )

        if query.symbol.isdigit():
            query_string = f"cik={query.symbol}&timeframe={period}&{query_string}"
        else:
            query_string = f"ticker={query.symbol}&timeframe={period}&{query_string}"

        request_url = f"{base_url}?{query_string}&apiKey={api_key}"

        return await get_data_many(request_url, "results", **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: PolygonBalanceSheetQueryParams,
<<<<<<< HEAD
        data: dict,
=======
        data: Dict,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        **kwargs: Any,
    ) -> List[PolygonBalanceSheetData]:
        """Return the transformed data."""
        transformed_data = []

        for item in data:
<<<<<<< HEAD
            sub_data = {
                key: value["value"]
                for key, value in item["financials"]["balance_sheet"].items()
            }
            sub_data["date"] = item["start_date"]
            sub_data["cik"] = item["cik"]
            sub_data["symbol"] = item["tickers"]
            sub_data["period"] = item["fiscal_period"]
            transformed_data.append(PolygonBalanceSheetData(**sub_data))
=======
            if "balance_sheet" in item["financials"]:
                sub_data = {
                    key: value["value"]
                    for key, value in item["financials"]["balance_sheet"].items()
                }
                sub_data["period_ending"] = item["end_date"]
                sub_data["fiscal_period"] = item["fiscal_period"]
                transformed_data.append(PolygonBalanceSheetData(**sub_data))
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        return transformed_data
