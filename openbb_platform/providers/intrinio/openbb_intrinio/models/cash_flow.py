"""Intrinio Cash Flow Statement Model."""

<<<<<<< HEAD

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from typing import Any, Dict, List, Optional
=======
# pylint: disable=unused-argument
import warnings
from typing import Any, Dict, List, Literal, Optional
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cash_flow import (
    CashFlowStatementData,
    CashFlowStatementQueryParams,
)
<<<<<<< HEAD
from openbb_intrinio.utils.helpers import get_data_one
from pydantic import Field
=======
from openbb_core.provider.utils.helpers import ClientResponse, amake_requests
from openbb_intrinio.utils.helpers import get_data_one
from pydantic import Field, field_validator, model_validator

_warn = warnings.warn
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class IntrinioCashFlowStatementQueryParams(CashFlowStatementQueryParams):
    """Intrinio Cash Flow Statement Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_company_fundamentals_v2
    Source: https://docs.intrinio.com/documentation/web_api/get_fundamental_standardized_financials_v2
    """

<<<<<<< HEAD
=======
    period: Literal["annual", "quarter", "ttm", "ytd"] = Field(default="annual")
    fiscal_year: Optional[int] = Field(
        default=None,
        description="The specific fiscal year.  Reports do not go beyond 2008.",
    )

    @field_validator("symbol", mode="after", check_fields=False)
    @classmethod
    def handle_symbol(cls, v) -> str:
        """Handle symbols with a dash and replace it with a dot for Intrinio."""
        return v.replace("-", ".")

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class IntrinioCashFlowStatementData(CashFlowStatementData):
    """Intrinio Cash Flow Statement Data."""

    __alias_dict__ = {
<<<<<<< HEAD
        "net_income": "netincome",
        "depreciation_and_amortization": "depreciationexpense",
        "other_non_cash_items": "noncashadjustmentstonetincome",
        "accounts_receivables": "IncreaseDecreaseInAccountsReceivable",
        "inventory": "IncreaseDecreaseInInventories",
        "vendor_non_trade_receivables": "IncreaseDecreaseInOtherReceivables",
        "other_current_and_non_current_assets": "IncreaseDecreaseInOtherOperatingAssets",
        "accounts_payables": "IncreaseDecreaseInAccountsPayable",
        "deferred_revenue": "IncreaseDecreaseInContractWithCustomerLiability",
        "other_current_and_non_current_liabilities": "IncreaseDecreaseInOtherOperatingLiabilities",
        "net_cash_flow_from_operating_activities": "netcashfromoperatingactivities",
        "purchases_of_marketable_securities": "purchaseofinvestments",
        "sales_from_maturities_of_investments": "saleofinvestments",
        "investments_in_property_plant_and_equipment": "purchaseofplantpropertyandequipment",
        "payments_from_acquisitions": "acquisitions",
        "other_investing_activities": "otherinvestingactivitiesnet",
        "net_cash_flow_from_investing_activities": "netcashfrominvestingactivities",
        "dividends_paid": "paymentofdividends",
        "common_stock_repurchased": "repurchaseofcommonequity",
        "debt_proceeds": "issuanceofdebt",
        "debt_repayment": "repaymentofdebt",
        "other_financing_activities": "otherfinancingactivitiesnet",
        "net_cash_flow_from_financing_activities": "netcashfromfinancingactivities",
        "net_change_in_cash": "netchangeincash",
    }

    changes_in_operating_assets_and_liabilities: Optional[float] = Field(
        None,
        alias="increasedecreaseinoperatingcapital",
        description="Changes in operating assets and liabilities.",
    )

    net_income_continuing: Optional[float] = Field(
        default=None,
        alias="netincomecontinuing",
        description="Net income from continuing operations.",
    )
    net_cash_from_continuing_operating_activities: Optional[float] = Field(
        default=None,
        alias="netcashfromcontinuingoperatingactivities",
        description="Net cash from continuing operating activities.",
    )
    net_cash_from_continuing_investing_activities: Optional[float] = Field(
        default=None,
        alias="netcashfromcontinuinginvestingactivities",
        description="Net cash from continuing investing activities.",
    )
    net_cash_from_continuing_financing_activities: Optional[float] = Field(
        default=None,
        alias="netcashfromcontinuingfinancingactivities",
        description="Net cash from continuing financing activities.",
    )
    cash_interest_paid: Optional[float] = Field(
        default=None, alias="cashinterestpaid", description="Cash paid for interest."
    )
    cash_income_taxes_paid: Optional[float] = Field(
        default=None,
        alias="cashincometaxespaid",
        description="Cash paid for income taxes.",
    )
    issuance_of_common_equity: Optional[float] = Field(
        default=None,
        alias="issuanceofcommonequity",
        description="Issuance of common equity.",
    )

=======
        "cash_and_equivalents": "cashandequivalents",
        "acquisitions": "acquisitions",
        "amortization_expense": "amortizationexpense",
        "cash_income_taxes_paid": "cashincometaxespaid",
        "cash_interest_paid": "cashinterestpaid",
        "cash_interest_received": "cashinterestreceived",
        "depreciation_expense": "depreciationexpense",
        "divestitures": "divestitures",
        "effect_of_exchange_rate_changes": "effectofexchangeratechanges",
        "changes_in_operating_assets_and_liabilities": "increasedecreaseinoperatingcapital",
        "issuance_of_common_equity": "issuanceofcommonequity",
        "issuance_of_debt": "issuanceofdebt",
        "issuance_of_preferred_equity": "issuanceofpreferredequity",
        "loans_held_for_sale": "loansheldforsalenet",
        "net_cash_from_continuing_financing_activities": "netcashfromcontinuingfinancingactivities",
        "net_cash_from_continuing_investing_activities": "netcashfromcontinuinginvestingactivities",
        "net_cash_from_continuing_operating_activities": "netcashfromcontinuingoperatingactivities",
        "net_cash_from_discontinued_financing_activities": "netcashfromdiscontinuedfinancingactivities",
        "net_cash_from_discontinued_investing_activities": "netcashfromdiscontinuedinvestingactivities",
        "net_cash_from_discontinued_operating_activities": "netcashfromdiscontinuedoperatingactivities",
        "net_cash_from_financing_activities": "netcashfromfinancingactivities",
        "net_cash_from_investing_activities": "netcashfrominvestingactivities",
        "net_cash_from_operating_activities": "netcashfromoperatingactivities",
        "net_change_in_cash_and_equivalents": "netchangeincash",
        "net_change_in_deposits": "netchangeindeposits",
        "net_income": "netincome",
        "net_income_continuing_operations": "netincomecontinuing",
        "net_income_discontinued_operations": "netincomediscontinued",
        "net_increase_in_fed_funds_sold": "netincreaseinfedfundssold",
        "non_cash_adjustments_to_reconcile_net_income": "noncashadjustmentstonetincome",
        "other_financing_activities": "otherfinancingactivitiesnet",
        "other_investing_activities": "otherinvestingactivitiesnet",
        "other_net_changes_in_cash": "othernetchangesincash",
        "payment_of_dividends": "paymentofdividends",
        "provision_for_loan_losses": "provisionforloanlosses",
        "purchase_of_investments": "purchaseofinvestments",
        "purchase_of_investment_securities": "purchaseofinvestments",
        "purchase_of_property_plant_and_equipment": "purchaseofplantpropertyandequipment",
        "repayment_of_debt": "repaymentofdebt",
        "repurchase_of_common_equity": "repurchaseofcommonequity",
        "repurchase_of_preferred_equity": "repurchaseofpreferredequity",
        "sale_and_maturity_of_investments": "saleofinvestments",
        "sale_of_property_plant_and_equipment": "saleofplantpropertyandequipment",
    }

    reported_currency: Optional[str] = Field(
        description="The currency in which the balance sheet is reported.",
        default=None,
    )
    net_income: Optional[float] = Field(
        default=None, description="Consolidated Net Income."
    )
    provision_for_loan_losses: Optional[float] = Field(
        default=None, description="Provision for Loan Losses"
    )
    provision_for_credit_losses: Optional[float] = Field(
        default=None, description="Provision for credit losses"
    )
    depreciation_expense: Optional[float] = Field(
        default=None, description="Depreciation Expense."
    )
    amortization_expense: Optional[float] = Field(
        default=None, description="Amortization Expense."
    )
    share_based_compensation: Optional[float] = Field(
        default=None, description="Share-based compensation."
    )
    non_cash_adjustments_to_reconcile_net_income: Optional[float] = Field(
        default=None, description="Non-Cash Adjustments to Reconcile Net Income."
    )
    changes_in_operating_assets_and_liabilities: Optional[float] = Field(
        default=None, description="Changes in Operating Assets and Liabilities (Net)"
    )
    net_cash_from_continuing_operating_activities: Optional[float] = Field(
        default=None, description="Net Cash from Continuing Operating Activities"
    )
    net_cash_from_discontinued_operating_activities: Optional[float] = Field(
        default=None, description="Net Cash from Discontinued Operating Activities"
    )
    net_income_continuing_operations: Optional[float] = Field(
        default=None, description="Net Income (Continuing Operations)"
    )
    net_income_discontinued_operations: Optional[float] = Field(
        default=None, description="Net Income (Discontinued Operations)"
    )
    net_cash_from_operating_activities: Optional[float] = Field(
        default=None, description="Net Cash from Operating Activities"
    )
    divestitures: Optional[float] = Field(default=None, description="Divestitures")
    sale_of_property_plant_and_equipment: Optional[float] = Field(
        default=None, description="Sale of Property, Plant, and Equipment"
    )
    acquisitions: Optional[float] = Field(default=None, description="Acquisitions")
    purchase_of_investments: Optional[float] = Field(
        default=None, description="Purchase of Investments"
    )
    purchase_of_investment_securities: Optional[float] = Field(
        default=None, description="Purchase of Investment Securities"
    )
    sale_and_maturity_of_investments: Optional[float] = Field(
        default=None, description="Sale and Maturity of Investments"
    )
    loans_held_for_sale: Optional[float] = Field(
        default=None, description="Loans Held for Sale (Net)"
    )
    purchase_of_property_plant_and_equipment: Optional[float] = Field(
        default=None, description="Purchase of Property, Plant, and Equipment"
    )
    other_investing_activities: Optional[float] = Field(
        default=None, description="Other Investing Activities (Net)"
    )
    net_cash_from_continuing_investing_activities: Optional[float] = Field(
        default=None, description="Net Cash from Continuing Investing Activities"
    )
    net_cash_from_discontinued_investing_activities: Optional[float] = Field(
        default=None, description="Net Cash from Discontinued Investing Activities"
    )
    net_cash_from_investing_activities: Optional[float] = Field(
        default=None, description="Net Cash from Investing Activities"
    )
    payment_of_dividends: Optional[float] = Field(
        default=None, description="Payment of Dividends"
    )
    repurchase_of_common_equity: Optional[float] = Field(
        default=None, description="Repurchase of Common Equity"
    )
    repurchase_of_preferred_equity: Optional[float] = Field(
        default=None, description="Repurchase of Preferred Equity"
    )
    issuance_of_common_equity: Optional[float] = Field(
        default=None, description="Issuance of Common Equity"
    )
    issuance_of_preferred_equity: Optional[float] = Field(
        default=None, description="Issuance of Preferred Equity"
    )
    issuance_of_debt: Optional[float] = Field(
        default=None, description="Issuance of Debt"
    )
    repayment_of_debt: Optional[float] = Field(
        default=None, description="Repayment of Debt"
    )
    other_financing_activities: Optional[float] = Field(
        default=None, description="Other Financing Activities (Net)"
    )
    cash_interest_received: Optional[float] = Field(
        default=None, description="Cash Interest Received"
    )
    net_change_in_deposits: Optional[float] = Field(
        default=None, description="Net Change in Deposits"
    )
    net_increase_in_fed_funds_sold: Optional[float] = Field(
        default=None, description="Net Increase in Fed Funds Sold"
    )
    net_cash_from_continuing_financing_activities: Optional[float] = Field(
        default=None, description="Net Cash from Continuing Financing Activities"
    )
    net_cash_from_discontinued_financing_activities: Optional[float] = Field(
        default=None, description="Net Cash from Discontinued Financing Activities"
    )
    net_cash_from_financing_activities: Optional[float] = Field(
        default=None, description="Net Cash from Financing Activities"
    )
    effect_of_exchange_rate_changes: Optional[float] = Field(
        default=None, description="Effect of Exchange Rate Changes"
    )
    other_net_changes_in_cash: Optional[float] = Field(
        default=None, description="Other Net Changes in Cash"
    )
    net_change_in_cash_and_equivalents: Optional[float] = Field(
        default=None, description="Net Change in Cash and Equivalents"
    )
    cash_income_taxes_paid: Optional[float] = Field(
        default=None, description="Cash Income Taxes Paid"
    )
    cash_interest_paid: Optional[float] = Field(
        default=None, description="Cash Interest Paid"
    )

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return {k: None if v == 0 else v for k, v in values.items()}

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class IntrinioCashFlowStatementFetcher(
    Fetcher[
        IntrinioCashFlowStatementQueryParams,
        List[IntrinioCashFlowStatementData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioCashFlowStatementQueryParams:
        """Transform the query params."""
        return IntrinioCashFlowStatementQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: IntrinioCashFlowStatementQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
<<<<<<< HEAD
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        statement_code = "cash_flow_statement"
        period_type = "FY" if query.period == "annual" else "QTR"

        fundamentals_data: Dict = {}
        data: List[Dict] = []

        base_url = "https://api-v2.intrinio.com"
        fundamentals_url_params = f"statement_code={statement_code}&type={period_type}"
        fundamentals_url = (
            f"{base_url}/companies/{query.symbol}/fundamentals?"
            f"{fundamentals_url_params}&api_key={api_key}"
        )

        fundamentals_data = get_data_one(fundamentals_url, **kwargs).get(
            "fundamentals", []
        )
=======

        api_key = credentials.get("intrinio_api_key") if credentials else ""
        statement_code = "cash_flow_statement"
        if query.period in ["quarter", "annual"]:
            period_type = "FY" if query.period == "annual" else "QTR"
        if query.period in ["ttm", "ytd"]:
            period_type = query.period.upper()

        base_url = "https://api-v2.intrinio.com"
        fundamentals_url = (
            f"{base_url}/companies/{query.symbol}/fundamentals?"
            f"statement_code={statement_code}&type={period_type}"
        )
        if query.fiscal_year is not None:
            if query.fiscal_year < 2008:
                _warn("Financials data is only available from 2008 and later.")
                query.fiscal_year = 2008
            fundamentals_url = fundamentals_url + f"&fiscal_year={query.fiscal_year}"
        fundamentals_url = fundamentals_url + f"&api_key={api_key}"
        fundamentals_data = (await get_data_one(fundamentals_url, **kwargs)).get(
            "fundamentals", []
        )

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        fiscal_periods = [
            f"{item['fiscal_year']}-{item['fiscal_period']}"
            for item in fundamentals_data
        ]
        fiscal_periods = fiscal_periods[: query.limit]

<<<<<<< HEAD
        def get_financial_statement_data(period: str, data: List[Dict]) -> None:
            statement_data: Dict = {}

            intrinio_id = f"{query.symbol}-{statement_code}-{period}"
            statement_url = f"{base_url}/fundamentals/{intrinio_id}/standardized_financials?api_key={api_key}"
            statement_data = get_data_one(statement_url, **kwargs)

            data.append(
                {
                    "date": statement_data["fundamental"]["end_date"],
                    "period": statement_data["fundamental"]["fiscal_period"],
                    "financials": statement_data["standardized_financials"],
                }
            )

        with ThreadPoolExecutor() as executor:
            executor.map(get_financial_statement_data, fiscal_periods, repeat(data))

        return data
=======
        async def callback(response: ClientResponse, _: Any) -> Dict:
            """Return the response."""
            statement_data = await response.json()
            return {
                "period_ending": statement_data["fundamental"]["end_date"],
                "fiscal_period": statement_data["fundamental"]["fiscal_period"],
                "fiscal_year": statement_data["fundamental"]["fiscal_year"],
                "financials": statement_data["standardized_financials"],
            }

        intrinio_id = f"{query.symbol}-{statement_code}"
        urls = [
            f"{base_url}/fundamentals/{intrinio_id}-{period}/standardized_financials?api_key={api_key}"
            for period in fiscal_periods
        ]

        return await amake_requests(urls, callback, **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: IntrinioCashFlowStatementQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[IntrinioCashFlowStatementData]:
        """Return the transformed data."""
        transformed_data: List[IntrinioCashFlowStatementData] = []
<<<<<<< HEAD

=======
        units = []
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        for item in data:
            sub_dict: Dict[str, Any] = {}

            for sub_item in item["financials"]:
<<<<<<< HEAD
                field_name = sub_item["data_tag"]["tag"]
                sub_dict[field_name] = float(sub_item["value"])

            sub_dict["date"] = item["date"]
            sub_dict["period"] = item["period"]

            # Intrinio does not return Q4 data but FY data instead
            if query.period == "quarter" and item["period"] == "FY":
                sub_dict["period"] = "Q4"
=======
                unit = sub_item["data_tag"].get("unit", "")
                if unit and "share" not in unit:
                    units.append(unit)
                field_name = sub_item["data_tag"]["tag"]
                sub_dict[field_name] = (
                    float(sub_item["value"])
                    if sub_item["value"] and sub_item["value"] != 0
                    else None
                )

            sub_dict["period_ending"] = item["period_ending"]
            sub_dict["fiscal_year"] = item["fiscal_year"]
            sub_dict["fiscal_period"] = item["fiscal_period"]
            sub_dict["reported_currency"] = list(set(units))[0]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

            transformed_data.append(IntrinioCashFlowStatementData(**sub_dict))

        return transformed_data
