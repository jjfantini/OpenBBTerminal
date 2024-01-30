from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_yfinance.models.active import YFActiveFetcher
from openbb_yfinance.models.aggressive_small_caps import YFAggressiveSmallCapsFetcher
from openbb_yfinance.models.available_indices import YFinanceAvailableIndicesFetcher
from openbb_yfinance.models.balance_sheet import YFinanceBalanceSheetFetcher
from openbb_yfinance.models.cash_flow import YFinanceCashFlowStatementFetcher
from openbb_yfinance.models.company_news import YFinanceCompanyNewsFetcher
from openbb_yfinance.models.crypto_historical import YFinanceCryptoHistoricalFetcher
from openbb_yfinance.models.currency_historical import YFinanceCurrencyHistoricalFetcher
from openbb_yfinance.models.equity_historical import YFinanceEquityHistoricalFetcher
<<<<<<< HEAD
=======
from openbb_yfinance.models.equity_profile import YFinanceEquityProfileFetcher
from openbb_yfinance.models.equity_quote import YFinanceEquityQuoteFetcher
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_yfinance.models.etf_historical import YFinanceEtfHistoricalFetcher
from openbb_yfinance.models.futures_curve import YFinanceFuturesCurveFetcher
from openbb_yfinance.models.futures_historical import YFinanceFuturesHistoricalFetcher
from openbb_yfinance.models.gainers import YFGainersFetcher
from openbb_yfinance.models.growth_tech_equities import YFGrowthTechEquitiesFetcher
from openbb_yfinance.models.income_statement import YFinanceIncomeStatementFetcher
<<<<<<< HEAD
=======
from openbb_yfinance.models.index_historical import (
    YFinanceIndexHistoricalFetcher,
)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_yfinance.models.losers import YFLosersFetcher
from openbb_yfinance.models.market_indices import (
    YFinanceMarketIndicesFetcher,
)
from openbb_yfinance.models.undervalued_growth_equities import (
    YFUndervaluedGrowthEquitiesFetcher,
)
from openbb_yfinance.models.undervalued_large_caps import YFUndervaluedLargeCapsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Cookie", "MOCK_COOKIE"),
        ],
        "filter_query_parameters": [
            ("period1", "MOCK_PERIOD_1"),
            ("period2", "MOCK_PERIOD_2"),
            ("crumb", "MOCK_CRUMB"),
        ],
    }


@pytest.mark.record_http
<<<<<<< HEAD
def test_y_finance_equity_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "AAPL",
    }

    fetcher = YFinanceEquityHistoricalFetcher()
=======
def test_y_finance_market_indices_fetcher(credentials=test_credentials):
    params = {
        "symbol": "^GSPC",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = YFinanceMarketIndicesFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_y_finance_crypto_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "BTC-USD",
=======
def test_y_finance_index_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "^GSPC",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

<<<<<<< HEAD
    fetcher = YFinanceCryptoHistoricalFetcher()
=======
    fetcher = YFinanceIndexHistoricalFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_y_finance_currency_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "EURUSD",
=======
def test_y_finance_crypto_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "BTCUSD",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

<<<<<<< HEAD
    fetcher = YFinanceCurrencyHistoricalFetcher()
=======
    fetcher = YFinanceCryptoHistoricalFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_y_finance_market_indices_fetcher(credentials=test_credentials):
    params = {
        "symbol": "SPY",
=======
def test_y_finance_equity_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "AAPL",
    }

    fetcher = YFinanceEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_currency_historical_fetcher(credentials=test_credentials):
    params = {
        "symbol": "EURUSD",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

<<<<<<< HEAD
    fetcher = YFinanceMarketIndicesFetcher()
=======
    fetcher = YFinanceCurrencyHistoricalFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_futures_historical_fetcher(credentials=test_credentials):
    params = {
<<<<<<< HEAD
        "symbol": "ES",
=======
        "symbol": "ES=F",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = YFinanceFuturesHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


<<<<<<< HEAD
=======
@pytest.mark.skip("Unreliable amount of data while recording test.")
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
@pytest.mark.record_http
def test_y_finance_futures_curve_fetcher(credentials=test_credentials):
    params = {"symbol": "ES"}

    fetcher = YFinanceFuturesCurveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_company_news_fetcher(credentials=test_credentials):
    params = {"symbols": "AAPL,MSFT"}

    fetcher = YFinanceCompanyNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_balance_sheet_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceBalanceSheetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_cash_flow_statement_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceCashFlowStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_income_statement_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceIncomeStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_y_finance_available_fetcher(credentials=test_credentials):
    params = {}

    fetcher = YFinanceAvailableIndicesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_etf_historical_fetcher(credentials=test_credentials):
    params = {
<<<<<<< HEAD
        "symbol": "IOO",
=======
        "symbol": "SPY",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = YFinanceEtfHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_active_fetcher(credentials=test_credentials):
=======
def test_y_finance_active_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFActiveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_gainers_fetcher(credentials=test_credentials):
=======
def test_y_finance_gainers_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFGainersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_losers_fetcher(credentials=test_credentials):
=======
def test_y_finance_losers_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFLosersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_undervalued_large_caps_fetcher(credentials=test_credentials):
=======
def test_y_finance_undervalued_large_caps_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFUndervaluedLargeCapsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_undervalued_growth_equities_fetcher(credentials=test_credentials):
=======
def test_y_finance_undervalued_growth_equities_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFUndervaluedGrowthEquitiesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_aggressive_small_caps_fetcher(credentials=test_credentials):
=======
def test_y_finance_aggressive_small_caps_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFAggressiveSmallCapsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_yf_growth_tech_equities_fetcher(credentials=test_credentials):
=======
def test_y_finance_growth_tech_equities_fetcher(credentials=test_credentials):
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    params = {}

    fetcher = YFGrowthTechEquitiesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
<<<<<<< HEAD
=======


@pytest.mark.record_http
def test_y_finance_equity_profile_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceEquityProfileFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_y_finance_equity_quote_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = YFinanceEquityQuoteFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
