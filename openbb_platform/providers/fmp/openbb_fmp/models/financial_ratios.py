"""FMP Financial Ratios Model."""

<<<<<<< HEAD
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from itertools import repeat
=======
from datetime import datetime
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.financial_ratios import (
    FinancialRatiosData,
    FinancialRatiosQueryParams,
)
<<<<<<< HEAD
from openbb_fmp.utils.helpers import get_data_many, get_data_one
from pydantic import Field

PeriodType = Literal["annual", "quarter"]
=======
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.helpers import (
    amake_requests,
    to_snake_case,
)
from pydantic import Field, model_validator
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


class FMPFinancialRatiosQueryParams(FinancialRatiosQueryParams):
    """FMP Financial Ratios Query.

    Source: https://financialmodelingprep.com/developer/docs/#Company-Financial-Ratios
    """

<<<<<<< HEAD
    with_ttm: Optional[bool] = Field(
        default=False, description="Include trailing twelve months (TTM) data."
=======
    period: Literal["annual", "quarter", "ttm"] = Field(
        default="annual", description=QUERY_DESCRIPTIONS.get("period", "")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    )


class FMPFinancialRatiosData(FinancialRatiosData):
    """FMP Financial Ratios Data."""

    __alias_dict__ = {
<<<<<<< HEAD
        "net_income_per_ebt": "netIncomePerEBT",
        "dividend_yield": "dividendYiel",
        "dividend_yield_percentage": "dividendYieldPercentage",
        "dividend_per_share": "dividendPerShare",
        "research_and_developement_to_revenue": "researchAndDevelopementToRevenue",
        "debt_to_market_cap": "debtToMarketCap",
    }

=======
        "dividend_yield_ttm": "dividend_yiel_ttm",
        "dividend_yield_ttm_percent": "dividend_yiel_percentage_ttm",
        "period_ending": "date",
        "fiscal_period": "period",
        "fiscal_year": "calendar_year",
    }

    current_ratio: Optional[float] = Field(default=None, description="Current ratio.")
    quick_ratio: Optional[float] = Field(default=None, description="Quick ratio.")
    cash_ratio: Optional[float] = Field(default=None, description="Cash ratio.")
    days_of_sales_outstanding: Optional[float] = Field(
        default=None, description="Days of sales outstanding."
    )
    days_of_inventory_outstanding: Optional[float] = Field(
        default=None, description="Days of inventory outstanding."
    )
    operating_cycle: Optional[float] = Field(
        default=None, description="Operating cycle."
    )
    days_of_payables_outstanding: Optional[float] = Field(
        default=None, description="Days of payables outstanding."
    )
    cash_conversion_cycle: Optional[float] = Field(
        default=None, description="Cash conversion cycle."
    )
    gross_profit_margin: Optional[float] = Field(
        default=None, description="Gross profit margin."
    )
    operating_profit_margin: Optional[float] = Field(
        default=None, description="Operating profit margin."
    )
    pretax_profit_margin: Optional[float] = Field(
        default=None, description="Pretax profit margin."
    )
    net_profit_margin: Optional[float] = Field(
        default=None, description="Net profit margin."
    )
    effective_tax_rate: Optional[float] = Field(
        default=None, description="Effective tax rate."
    )
    return_on_assets: Optional[float] = Field(
        default=None, description="Return on assets."
    )
    return_on_equity: Optional[float] = Field(
        default=None, description="Return on equity."
    )
    return_on_capital_employed: Optional[float] = Field(
        default=None, description="Return on capital employed."
    )
    net_income_per_ebt: Optional[float] = Field(
        default=None, description="Net income per EBT."
    )
    ebt_per_ebit: Optional[float] = Field(default=None, description="EBT per EBIT.")
    ebit_per_revenue: Optional[float] = Field(
        default=None, description="EBIT per revenue."
    )
    debt_ratio: Optional[float] = Field(default=None, description="Debt ratio.")
    debt_equity_ratio: Optional[float] = Field(
        default=None, description="Debt equity ratio."
    )
    long_term_debt_to_capitalization: Optional[float] = Field(
        default=None, description="Long term debt to capitalization."
    )
    total_debt_to_capitalization: Optional[float] = Field(
        default=None, description="Total debt to capitalization."
    )
    interest_coverage: Optional[float] = Field(
        default=None, description="Interest coverage."
    )
    cash_flow_to_debt_ratio: Optional[float] = Field(
        default=None, description="Cash flow to debt ratio."
    )
    company_equity_multiplier: Optional[float] = Field(
        default=None, description="Company equity multiplier."
    )
    receivables_turnover: Optional[float] = Field(
        default=None, description="Receivables turnover."
    )
    payables_turnover: Optional[float] = Field(
        default=None, description="Payables turnover."
    )
    inventory_turnover: Optional[float] = Field(
        default=None, description="Inventory turnover."
    )
    fixed_asset_turnover: Optional[float] = Field(
        default=None, description="Fixed asset turnover."
    )
    asset_turnover: Optional[float] = Field(default=None, description="Asset turnover.")
    operating_cash_flow_per_share: Optional[float] = Field(
        default=None, description="Operating cash flow per share."
    )
    free_cash_flow_per_share: Optional[float] = Field(
        default=None, description="Free cash flow per share."
    )
    cash_per_share: Optional[float] = Field(default=None, description="Cash per share.")
    payout_ratio: Optional[float] = Field(default=None, description="Payout ratio.")
    operating_cash_flow_sales_ratio: Optional[float] = Field(
        default=None, description="Operating cash flow sales ratio."
    )
    free_cash_flow_operating_cash_flow_ratio: Optional[float] = Field(
        default=None, description="Free cash flow operating cash flow ratio."
    )
    cash_flow_coverage_ratios: Optional[float] = Field(
        default=None, description="Cash flow coverage ratios."
    )
    short_term_coverage_ratios: Optional[float] = Field(
        default=None, description="Short term coverage ratios."
    )
    capital_expenditure_coverage_ratio: Optional[float] = Field(
        default=None, description="Capital expenditure coverage ratio."
    )
    dividend_paid_and_capex_coverage_ratio: Optional[float] = Field(
        default=None, description="Dividend paid and capex coverage ratio."
    )
    dividend_payout_ratio: Optional[float] = Field(
        default=None, description="Dividend payout ratio."
    )
    price_book_value_ratio: Optional[float] = Field(
        default=None, description="Price book value ratio."
    )
    price_to_book_ratio: Optional[float] = Field(
        default=None, description="Price to book ratio."
    )
    price_to_sales_ratio: Optional[float] = Field(
        default=None, description="Price to sales ratio."
    )
    price_earnings_ratio: Optional[float] = Field(
        default=None, description="Price earnings ratio."
    )
    price_to_free_cash_flows_ratio: Optional[float] = Field(
        default=None, description="Price to free cash flows ratio."
    )
    price_to_operating_cash_flows_ratio: Optional[float] = Field(
        default=None, description="Price to operating cash flows ratio."
    )
    price_cash_flow_ratio: Optional[float] = Field(
        default=None, description="Price cash flow ratio."
    )
    price_earnings_to_growth_ratio: Optional[float] = Field(
        default=None, description="Price earnings to growth ratio."
    )
    price_sales_ratio: Optional[float] = Field(
        default=None, description="Price sales ratio."
    )
    dividend_yield: Optional[float] = Field(default=None, description="Dividend yield.")
    dividend_yield_percentage: Optional[float] = Field(
        default=None, description="Dividend yield percentage."
    )
    dividend_per_share: Optional[float] = Field(
        default=None, description="Dividend per share."
    )
    enterprise_value_multiple: Optional[float] = Field(
        default=None, description="Enterprise value multiple."
    )
    price_fair_value: Optional[float] = Field(
        default=None, description="Price fair value."
    )

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return {k: None if v == 0 else v for k, v in values.items()}

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

class FMPFinancialRatiosFetcher(
    Fetcher[
        FMPFinancialRatiosQueryParams,
        List[FMPFinancialRatiosData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPFinancialRatiosQueryParams:
        """Transform the query params."""
        return FMPFinancialRatiosQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPFinancialRatiosQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"
<<<<<<< HEAD
        data: List[Dict] = []

        def multiple_symbols(symbol: str, data: List[Dict]) -> None:
            url = (
                f"{base_url}/ratios/{symbol}?"
                f"period={query.period}&limit={query.limit}&apikey={api_key}"
            )

            # TTM data
            ttm_url = f"{base_url}/ratios-ttm/{symbol}?&apikey={api_key}"
            if query.with_ttm and (ratios_ttm := get_data_one(ttm_url, **kwargs)):
                data.append(
                    {
                        "symbol": symbol,
                        "period": "TTM",
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        **{k.replace("TTM", ""): v for k, v in ratios_ttm.items()},
                    }
                )

            return data.extend(get_data_many(url, **kwargs))

        with ThreadPoolExecutor() as executor:
            executor.map(multiple_symbols, query.symbol.split(","), repeat(data))

        return data
=======

        ttm_url = f"{base_url}/ratios-ttm/{query.symbol}?&apikey={api_key}"

        url = (
            f"{base_url}/ratios/{query.symbol}?"
            f"period={query.period}&limit={query.limit}&apikey={api_key}"
            if query.period != "ttm"
            else ttm_url
        )
        results = await amake_requests(url, **kwargs)

        return results
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    @staticmethod
    def transform_data(
        query: FMPFinancialRatiosQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPFinancialRatiosData]:
        """Return the transformed data."""
<<<<<<< HEAD
        return [FMPFinancialRatiosData.model_validate(d) for d in data]
=======
        results = [
            {to_snake_case(k).replace("ttm", ""): v for k, v in item.items()}
            for item in data
        ]
        if query.period == "ttm":
            results[0].update(
                {"period": "TTM", "date": datetime.now().date().strftime("%Y-%m-%d")}
            )
        for item in results:
            item.pop("symbol", None)
            item.pop("dividend_yiel_percentage", None)
        return [FMPFinancialRatiosData.model_validate(d) for d in results]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
