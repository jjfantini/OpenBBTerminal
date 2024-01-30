"""FMP Cash Flow Statement Model."""

<<<<<<< HEAD
=======
# pylint: disable=unused-argument
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Dict, List, Literal, Optional

<<<<<<< HEAD
from openbb_core.provider.abstract.data import ForceInt
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cash_flow import (
    CashFlowStatementData,
    CashFlowStatementQueryParams,
)
<<<<<<< HEAD
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_fmp.utils.helpers import create_url, get_data_many
from pydantic import Field, model_validator


class FMPCashFlowStatementQueryParams(CashFlowStatementQueryParams):
    """FMP Cash Flow Statement Query.

    Source: https://financialmodelingprep.com/developer/docs/#Cash-Flow-Statement
    """

<<<<<<< HEAD
    period: Optional[Literal["annual", "quarter"]] = Field(
        default="quarter",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )
    cik: Optional[str] = Field(
        default=None, description="Central Index Key (CIK) of the company."
    )

    @model_validator(mode="before")
    @classmethod
    def check_symbol_or_cik(cls, values):  # pylint: disable=no-self-argument
        """Validate that either a symbol or CIK is provided."""
        if values.get("symbol") is None and values.get("cik") is None:
            raise ValueError("symbol or cik must be provided")
        return values
=======
    period: Optional[Literal["annual", "quarter"]] = Field(default="annual")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class FMPCashFlowStatementData(CashFlowStatementData):
    """FMP Cash Flow Statement Data."""

    __alias_dict__ = {
<<<<<<< HEAD
        "reported_currency": "reportedCurrency",
        "net_cash_used_for_investing_activities": "netCashUsedForInvestingActivites",
        "other_financing_activities": "otherFinancingActivites",
        "net_cash_flow_from_operating_activities": "netCashProvidedByOperatingActivities",
        "purchases_of_marketable_securities": "purchasesOfInvestments",
        "sales_from_maturities_of_investments": "salesMaturitiesOfInvestments",
        "payments_from_acquisitions": "acquisitionsNet",
        "net_cash_flow_from_investing_activities": "netCashUsedForInvestingActivites",
        "net_cash_flow_from_financing_activities": "netCashUsedProvidedByFinancingActivities",
        "other_investing_activities": "otherInvestingActivites",
    }

    reported_currency: str = Field(description="Reported currency in the statement.")
    filling_date: dateType = Field(description="Filling date.")
    accepted_date: datetime = Field(description="Accepted date.")
    calendar_year: Optional[ForceInt] = Field(
        default=None, description="Calendar year."
    )

    change_in_working_capital: Optional[ForceInt] = Field(
        default=None, description="Change in working capital."
    )
    other_working_capital: Optional[ForceInt] = Field(
        default=None, description="Other working capital."
    )
    common_stock_issued: Optional[ForceInt] = Field(
        default=None, description="Common stock issued."
    )
    effect_of_forex_changes_on_cash: Optional[ForceInt] = Field(
        default=None, description="Effect of forex changes on cash."
    )

    cash_at_beginning_of_period: Optional[ForceInt] = Field(
        default=None, description="Cash at beginning of period."
    )
    cash_at_end_of_period: Optional[ForceInt] = Field(
        default=None,
        description="Cash, cash equivalents, and restricted cash at end of period",
    )
    operating_cash_flow: Optional[ForceInt] = Field(
        default=None, description="Operating cash flow."
    )
    capital_expenditure: Optional[ForceInt] = Field(
        default=None, description="Capital expenditure."
    )
    free_cash_flow: Optional[ForceInt] = Field(
        default=None, description="Free cash flow."
    )

    link: Optional[str] = Field(default=None, description="Link to the statement.")
    final_link: Optional[str] = Field(
        default=None, description="Link to the final statement."
=======
        "period_ending": "date",
        "fiscal_period": "period",
        "fiscal_year": "calendarYear",
        "filing_date": "fillingDate",
        "accepted_date": "acceptedDate",
        "reported_currency": "reportedCurrency",
        "net_income": "netIncome",
        "depreciation_and_amortization": "depreciationAndAmortization",
        "deferred_income_tax": "deferredIncomeTax",
        "stock_based_compensation": "stockBasedCompensation",
        "change_in_working_capital": "changeInWorkingCapital",
        "change_in_account_receivables": "accountsReceivables",
        "change_in_inventory": "inventory",
        "change_in_account_payable": "accountsPayables",
        "change_in_other_working_capital": "otherWorkingCapital",
        "change_in_other_non_cash_items": "otherNonCashItems",
        "net_cash_from_operating_activities": "netCashProvidedByOperatingActivities",
        "purchase_of_property_plant_and_equipment": "investmentsInPropertyPlantAndEquipment",
        "acquisitions": "acquisitionsNet",
        "purchase_of_investment_securities": "purchasesOfInvestments",
        "sale_and_maturity_of_investments": "salesMaturitiesOfInvestments",
        "other_investing_activities": "otherInvestingActivites",
        "net_cash_from_investing_activities": "netCashUsedForInvestingActivites",
        "repayment_of_debt": "debtRepayment",
        "issuance_of_common_equity": "commonStockIssued",
        "repurchase_of_common_equity": "commonStockRepurchased",
        "payment_of_dividends": "dividendsPaid",
        "other_financing_activities": "otherFinancingActivites",
        "net_cash_from_financing_activities": "netCashUsedProvidedByFinancingActivities",
        "effect_of_exchange_rate_changes_on_cash": "effectOfForexChangesOnCash",
        "net_change_in_cash_and_equivalents": "netChangeInCash",
        "cash_at_beginning_of_period": "cashAtBeginningOfPeriod",
        "cash_at_end_of_period": "cashAtEndOfPeriod",
        "operating_cash_flow": "operatingCashFlow",
        "capital_expenditure": "capitalExpenditure",
        "free_cash_flow": "freeCashFlow",
        "link": "link",
        "final_link": "finalLink",
    }

    fiscal_year: Optional[int] = Field(
        default=None,
        description="The fiscal year of the fiscal period.",
    )
    filing_date: Optional[dateType] = Field(
        default=None,
        description="The date of the filing.",
    )
    accepted_date: Optional[datetime] = Field(
        default=None, description="The date the filing was accepted."
    )
    reported_currency: Optional[str] = Field(
        default=None,
        description="The currency in which the cash flow statement was reported.",
    )
    net_income: Optional[float] = Field(
        default=None,
        description="Net income.",
    )
    depreciation_and_amortization: Optional[float] = Field(
        default=None,
        description="Depreciation and amortization.",
    )
    deferred_income_tax: Optional[float] = Field(
        default=None,
        description="Deferred income tax.",
    )
    stock_based_compensation: Optional[float] = Field(
        default=None,
        description="Stock-based compensation.",
    )
    change_in_working_capital: Optional[float] = Field(
        default=None,
        description="Change in working capital.",
    )
    change_in_account_receivables: Optional[float] = Field(
        default=None,
        description="Change in account receivables.",
    )
    change_in_inventory: Optional[float] = Field(
        default=None,
        description="Change in inventory.",
    )
    change_in_account_payable: Optional[float] = Field(
        default=None,
        description="Change in account payable.",
    )
    change_in_other_working_capital: Optional[float] = Field(
        default=None,
        description="Change in other working capital.",
    )
    change_in_other_non_cash_items: Optional[float] = Field(
        default=None,
        description="Change in other non-cash items.",
    )
    net_cash_from_operating_activities: Optional[float] = Field(
        default=None,
        description="Net cash from operating activities.",
    )
    purchase_of_property_plant_and_equipment: Optional[float] = Field(
        default=None,
        description="Purchase of property, plant and equipment.",
    )
    acquisitions: Optional[float] = Field(
        default=None,
        description="Acquisitions.",
    )
    purchase_of_investment_securities: Optional[float] = Field(
        default=None,
        description="Purchase of investment securities.",
    )
    sale_and_maturity_of_investments: Optional[float] = Field(
        default=None,
        description="Sale and maturity of investments.",
    )
    other_investing_activities: Optional[float] = Field(
        default=None,
        description="Other investing activities.",
    )
    net_cash_from_investing_activities: Optional[float] = Field(
        default=None,
        description="Net cash from investing activities.",
    )
    repayment_of_debt: Optional[float] = Field(
        default=None,
        description="Repayment of debt.",
    )
    issuance_of_common_equity: Optional[float] = Field(
        default=None,
        description="Issuance of common equity.",
    )
    repurchase_of_common_equity: Optional[float] = Field(
        default=None,
        description="Repurchase of common equity.",
    )
    payment_of_dividends: Optional[float] = Field(
        default=None,
        description="Payment of dividends.",
    )
    other_financing_activities: Optional[float] = Field(
        default=None,
        description="Other financing activities.",
    )
    net_cash_from_financing_activities: Optional[float] = Field(
        default=None,
        description="Net cash from financing activities.",
    )
    effect_of_exchange_rate_changes_on_cash: Optional[float] = Field(
        default=None,
        description="Effect of exchange rate changes on cash.",
    )
    net_change_in_cash_and_equivalents: Optional[float] = Field(
        default=None,
        description="Net change in cash and equivalents.",
    )
    cash_at_beginning_of_period: Optional[float] = Field(
        default=None,
        description="Cash at beginning of period.",
    )
    cash_at_end_of_period: Optional[float] = Field(
        default=None,
        description="Cash at end of period.",
    )
    operating_cash_flow: Optional[float] = Field(
        default=None,
        description="Operating cash flow.",
    )
    capital_expenditure: Optional[float] = Field(
        default=None,
        description="Capital expenditure.",
    )
    free_cash_flow: Optional[float] = Field(
        default=None,
    )
    link: Optional[str] = Field(
        default=None,
        description="Link to the filing.",
    )
    final_link: Optional[str] = Field(
        default=None,
        description="Link to the filing document.",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return {k: None if v == 0 else v for k, v in values.items()}


class FMPCashFlowStatementFetcher(
    Fetcher[
        FMPCashFlowStatementQueryParams,
        List[FMPCashFlowStatementData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCashFlowStatementQueryParams:
        """Transform the query params."""
        return FMPCashFlowStatementQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPCashFlowStatementQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(
            3, f"cash-flow-statement/{query.symbol}", api_key, query, ["symbol"]
        )

<<<<<<< HEAD
        return get_data_many(url, **kwargs)
=======
        return await get_data_many(url, **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPCashFlowStatementQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPCashFlowStatementData]:
        """Return the transformed data."""
<<<<<<< HEAD
=======
        for result in data:
            result.pop("symbol", None)
            result.pop("cik", None)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return [FMPCashFlowStatementData.model_validate(d) for d in data]
