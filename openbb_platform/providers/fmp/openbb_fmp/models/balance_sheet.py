"""FMP Balance Sheet Model."""

<<<<<<< HEAD

from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.data import ForceInt
=======
# pylint: disable=unused-argument
from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Dict, List, Literal, Optional

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.balance_sheet import (
    BalanceSheetData,
    BalanceSheetQueryParams,
)
<<<<<<< HEAD
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_fmp.utils.helpers import create_url, get_data_many
from pydantic import Field, model_validator


class FMPBalanceSheetQueryParams(BalanceSheetQueryParams):
    """FMP Balance Sheet Query.

    Source: https://financialmodelingprep.com/developer/docs/#Balance-Sheet
    """

<<<<<<< HEAD
    period: Optional[Literal["annual", "quarter"]] = Field(
        default="quarter",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )
    cik: Optional[str] = Field(
        default=None,
        description="Central Index Key (CIK) of the company.",
    )

    @model_validator(mode="before")
    @classmethod
    def check_symbol_or_cik(cls, values):  # pylint: disable=no-self-argument
        """Check if symbol or cik is provided."""
        if values.get("symbol") is None and values.get("cik") is None:
            raise ValueError("symbol or cik must be provided")
        return values
=======
    period: Optional[Literal["annual", "quarter"]] = Field(default="annual")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class FMPBalanceSheetData(BalanceSheetData):
    """FMP Balance Sheet Data."""

    __alias_dict__ = {
<<<<<<< HEAD
        "currency": "reportedCurrency",
        "current_assets": "totalCurrentAssets",
        "non_current_assets": "totalNonCurrentAssets",
        "assets": "totalAssets",
        "current_liabilities": "totalCurrentLiabilities",
        "non_current_liabilities": "totalNonCurrentLiabilities",
        "liabilities": "totalLiabilities",
        "other_stockholder_equity": "othertotalStockholdersEquity",
        "filing_date": "fillingDate",
    }

    # Leftovers below
    calendar_year: Optional[ForceInt] = Field(default=None, description="Calendar Year")

    cash_and_short_term_investments: Optional[ForceInt] = Field(
        default=None, description="Cash and Short Term Investments"
    )
    goodwill_and_intangible_assets: Optional[ForceInt] = Field(
        default=None, description="Goodwill and Intangible Assets"
    )
    deferred_revenue_non_current: Optional[ForceInt] = Field(
        default=None, description="Deferred Revenue Non Current"
    )
    total_investments: Optional[ForceInt] = Field(
        default=None, description="Total Investments"
    )

    capital_lease_obligations: Optional[ForceInt] = Field(
        default=None, description="Capital Lease Obligations"
    )
    deferred_tax_liabilities_non_current: Optional[ForceInt] = Field(
        default=None, description="Deferred Tax Liabilities Non Current"
    )
    capital_lease_obligations: Optional[ForceInt] = Field(
        default=None, description="Capital lease obligations"
    )
    total_investments: Optional[ForceInt] = Field(
        default=None, description="Total investments"
    )
    total_debt: Optional[ForceInt] = Field(default=None, description="Total debt")
    net_debt: Optional[ForceInt] = Field(default=None, description="Net debt")

    total_debt: Optional[ForceInt] = Field(default=None, description="Total Debt")
    net_debt: Optional[ForceInt] = Field(default=None, description="Net Debt")

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
        "cash_and_cash_equivalents": "cashAndCashEquivalents",
        "short_term_investments": "shortTermInvestments",
        "cash_and_short_term_investments": "cashAndShortTermInvestments",
        "net_receivables": "netReceivables",
        "inventory": "inventories",
        "other_current_assets": "otherCurrentAssets",
        "total_current_assets": "totalCurrentAssets",
        "plant_property_equipment_net": "propertyPlantEquipmentNet",
        "goodwill": "goodwill",
        "intangible_assets": "intangibleAssets",
        "goodwill_and_intangible_assets": "goodwillAndIntangibleAssets",
        "long_term_investments": "longTermInvestments",
        "tax_assets": "taxAssets",
        "other_non_current_assets": "otherNonCurrentAssets",
        "non_current_assets": "totalNonCurrentAssets",
        "other_assets": "otherAssets",
        "total_assets": "totalAssets",
        "accounts_payable": "accountPayables",
        "short_term_debt": "shortTermDebt",
        "tax_payables": "taxPayables",
        "current_deferred_revenue": "deferredRevenue",
        "other_current_liabilities": "otherCurrentLiabilities",
        "total_current_liabilities": "totalCurrentLiabilities",
        "long_term_debt": "longTermDebt",
        "deferred_revenue_non_current": "deferredRevenueNonCurrent",
        "deferred_tax_liabilities_non_current": "deferredTaxLiabilitiesNonCurrent",
        "other_non_current_liabilities": "otherNonCurrentLiabilities",
        "total_non_current_liabilities": "totalNonCurrentLiabilities",
        "other_liabilities": "otherLiabilities",
        "capital_lease_obligations": "capitalLeaseObligations",
        "total_liabilities": "totalLiabilities",
        "preferred_stock": "preferredStock",
        "common_stock": "commonStock",
        "retained_earnings": "retainedEarnings",
        "accumulated_other_comprehensive_income": "accumulatedOtherComprehensiveIncomeLoss",
        "other_shareholders_equity": "otherStockholdersEquity",
        "other_total_shareholders_equity": "othertotalStockholdersEquity",
        "total_common_equity": "totalStockholdersEquity",
        "total_equity_non_controlling_interests": "totalEquity",
        "total_liabilities_and_shareholders_equity": "totalLiabilitiesAndStockholdersEquity",
        "minority_interest": "minorityInterest",
        "total_liabilities_and_total_equity": "totalLiabilitiesAndTotalEquity",
        "total_investments": "totalInvestments",
        "total_debt": "totalDebt",
        "net_debt": "netDebt",
        "link": "link",
        "final_link": "finalLink",
    }

    filing_date: Optional[dateType] = Field(
        default=None,
        description="The date when the filing was made.",
    )
    accepted_date: Optional[datetime] = Field(
        default=None,
        description="The date and time when the filing was accepted.",
    )
    reported_currency: Optional[str] = Field(
        default=None,
        description="The currency in which the balance sheet was reported.",
    )
    cash_and_cash_equivalents: Optional[float] = Field(
        default=None,
        description="Cash and cash equivalents.",
    )
    short_term_investments: Optional[float] = Field(
        default=None,
        description="Short term investments.",
    )
    cash_and_short_term_investments: Optional[float] = Field(
        default=None,
        description="Cash and short term investments.",
    )
    net_receivables: Optional[float] = Field(
        default=None,
        description="Net receivables.",
    )
    inventory: Optional[float] = Field(
        default=None,
        description="Inventory.",
    )
    other_current_assets: Optional[float] = Field(
        default=None,
        description="Other current assets.",
    )
    total_current_assets: Optional[float] = Field(
        default=None,
        description="Total current assets.",
    )
    plant_property_equipment_net: Optional[float] = Field(
        default=None,
        description="Plant property equipment net.",
    )
    goodwill: Optional[float] = Field(
        default=None,
        description="Goodwill.",
    )
    intangible_assets: Optional[float] = Field(
        default=None,
        description="Intangible assets.",
    )
    goodwill_and_intangible_assets: Optional[float] = Field(
        default=None,
        description="Goodwill and intangible assets.",
    )
    long_term_investments: Optional[float] = Field(
        default=None,
        description="Long term investments.",
    )
    tax_assets: Optional[float] = Field(
        default=None,
        description="Tax assets.",
    )
    other_non_current_assets: Optional[float] = Field(
        default=None,
        description="Other non current assets.",
    )
    non_current_assets: Optional[float] = Field(
        default=None,
        description="Total non current assets.",
    )
    other_assets: Optional[float] = Field(
        default=None,
        description="Other assets.",
    )
    total_assets: Optional[float] = Field(
        default=None,
        description="Total assets.",
    )
    accounts_payable: Optional[float] = Field(
        default=None,
        description="Accounts payable.",
    )
    short_term_debt: Optional[float] = Field(
        default=None,
        description="Short term debt.",
    )
    tax_payables: Optional[float] = Field(
        default=None,
        description="Tax payables.",
    )
    current_deferred_revenue: Optional[float] = Field(
        default=None,
        description="Current deferred revenue.",
    )
    other_current_liabilities: Optional[float] = Field(
        default=None,
        description="Other current liabilities.",
    )
    total_current_liabilities: Optional[float] = Field(
        default=None,
        description="Total current liabilities.",
    )
    long_term_debt: Optional[float] = Field(
        default=None,
        description="Long term debt.",
    )
    deferred_revenue_non_current: Optional[float] = Field(
        default=None,
        description="Non current deferred revenue.",
    )
    deferred_tax_liabilities_non_current: Optional[float] = Field(
        default=None,
        description="Deferred tax liabilities non current.",
    )
    other_non_current_liabilities: Optional[float] = Field(
        default=None,
        description="Other non current liabilities.",
    )
    total_non_current_liabilities: Optional[float] = Field(
        default=None,
        description="Total non current liabilities.",
    )
    other_liabilities: Optional[float] = Field(
        default=None,
        description="Other liabilities.",
    )
    capital_lease_obligations: Optional[float] = Field(
        default=None,
        description="Capital lease obligations.",
    )
    total_liabilities: Optional[float] = Field(
        default=None,
        description="Total liabilities.",
    )
    preferred_stock: Optional[float] = Field(
        default=None,
        description="Preferred stock.",
    )
    common_stock: Optional[float] = Field(
        default=None,
        description="Common stock.",
    )
    retained_earnings: Optional[float] = Field(
        default=None,
        description="Retained earnings.",
    )
    accumulated_other_comprehensive_income: Optional[float] = Field(
        default=None,
        description="Accumulated other comprehensive income (loss).",
    )
    other_shareholders_equity: Optional[float] = Field(
        default=None,
        description="Other shareholders equity.",
    )
    other_total_shareholders_equity: Optional[float] = Field(
        default=None,
        description="Other total shareholders equity.",
    )
    total_common_equity: Optional[float] = Field(
        default=None,
        description="Total common equity.",
    )
    total_equity_non_controlling_interests: Optional[float] = Field(
        default=None,
        description="Total equity non controlling interests.",
    )
    total_liabilities_and_shareholders_equity: Optional[float] = Field(
        default=None,
        description="Total liabilities and shareholders equity.",
    )
    minority_interest: Optional[float] = Field(
        default=None,
        description="Minority interest.",
    )
    total_liabilities_and_total_equity: Optional[float] = Field(
        default=None,
        description="Total liabilities and total equity.",
    )
    total_investments: Optional[float] = Field(
        default=None,
        description="Total investments.",
    )
    total_debt: Optional[float] = Field(
        default=None,
        description="Total debt.",
    )
    net_debt: Optional[float] = Field(
        default=None,
        description="Net debt.",
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


class FMPBalanceSheetFetcher(
    Fetcher[
        FMPBalanceSheetQueryParams,
        List[FMPBalanceSheetData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPBalanceSheetQueryParams:
        """Transform the query params."""
        return FMPBalanceSheetQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPBalanceSheetQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(
            3, f"balance-sheet-statement/{query.symbol}", api_key, query, ["symbol"]
        )

<<<<<<< HEAD
        return get_data_many(url, **kwargs)
=======
        return await get_data_many(url, **kwargs)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPBalanceSheetQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPBalanceSheetData]:
        """Return the transformed data."""
<<<<<<< HEAD
=======
        for result in data:
            result.pop("symbol", None)
            result.pop("cik", None)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return [FMPBalanceSheetData.model_validate(d) for d in data]
