"""CBOE Fetchers Tests.

The CBOE provider extension uses request caching.
<<<<<<< HEAD
So, when an item like a symbol directory is already cached, the cassette recorder does
=======

For tests, set all functions using cache with the `use_cache` parameter to `False`.

When an item like a symbol directory is already cached, the cassette recorder does
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
not record the request event. If functions share a cached resource, it will only capture
the cassette for the first instance.

If an update of the cassettes is required the procedure is to delete the cache file and
then only run the single test which needs to be recorded.
"""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from datetime import date

import pytest
from openbb_cboe.models.available_indices import CboeAvailableIndicesFetcher
from openbb_cboe.models.equity_historical import CboeEquityHistoricalFetcher
<<<<<<< HEAD
from openbb_cboe.models.equity_info import CboeEquityInfoFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.european_index_constituents import (
    CboeEuropeanIndexConstituentsFetcher,
)
from openbb_cboe.models.european_indices import (
    CboeEuropeanIndicesFetcher,
)
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
from openbb_cboe.models.market_indices import (
    CboeMarketIndicesFetcher,
)
=======
from openbb_cboe.models.equity_quote import CboeEquityQuoteFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_constituents import CboeIndexConstituentsFetcher
from openbb_cboe.models.index_historical import CboeIndexHistoricalFetcher
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_cboe.models.options_chains import CboeOptionsChainsFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


<<<<<<< HEAD
@pytest.mark.record_http
def test_cboe_available_indices_fetcher(credentials=test_credentials):
    params = {}

    fetcher = CboeAvailableIndicesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_cboe_index_search_fetcher(credentials=test_credentials):
    params = {}

    fetcher = CboeIndexSearchFetcher()
=======
@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            None,
        ],
    }


@pytest.mark.record_http
def test_cboe_index_historical_fetcher(credentials=test_credentials):
    params = {"symbol": "AAVE10RP", "use_cache": False}

    fetcher = CboeIndexHistoricalFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_cboe_options_chains_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = CboeOptionsChainsFetcher()
=======
def test_cboe_index_constituents_fetcher(credentials=test_credentials):
    params = {"symbol": "BUKBUS"}

    fetcher = CboeIndexConstituentsFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


<<<<<<< HEAD
@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            None,
        ],
    }


@pytest.mark.record_http
def test_cboe_equity_search_fetcher(credentials=test_credentials):
    params = {}

    fetcher = CboeEquitySearchFetcher()
=======
@pytest.mark.record_http
def test_cboe_index_search_fetcher(credentials=test_credentials):
    params = {"query": "uk", "use_cache": False}

    fetcher = CboeIndexSearchFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_cboe_equity_historical_fetcher(credentials=test_credentials):
<<<<<<< HEAD
    params = params = {
=======
    params = {
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
        "interval": "1d",
<<<<<<< HEAD
=======
        "use_cache": False,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    }

    fetcher = CboeEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_cboe_equity_info_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = CboeEquityInfoFetcher()
=======
def test_cboe_available_indices_fetcher(credentials=test_credentials):
    params = {"use_cache": False}

    fetcher = CboeAvailableIndicesFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_cboe_futures_curve_fetcher(credentials=test_credentials):
    params = {"symbol": "VX"}

    fetcher = CboeFuturesCurveFetcher()
=======
def test_cboe_options_chains_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL", "use_cache": False}

    fetcher = CboeOptionsChainsFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_cboe_european_index_constituents_fetcher(credentials=test_credentials):
    params = {"symbol": "BUKBUS"}

    fetcher = CboeEuropeanIndexConstituentsFetcher()
=======
def test_cboe_equity_search_fetcher(credentials=test_credentials):
    params = {"query": "ETF", "use_cache": False}

    fetcher = CboeEquitySearchFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_cboe_european_indices_fetcher(credentials=test_credentials):
    params = {
        "symbol": "BUKBUS",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = CboeEuropeanIndicesFetcher()
=======
def test_cboe_equity_quote_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL", "use_cache": False}

    fetcher = CboeEquityQuoteFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
<<<<<<< HEAD
def test_cboe_market_indices_fetcher(credentials=test_credentials):
    params = {"symbol": "AAVE10RP"}

    fetcher = CboeMarketIndicesFetcher()
=======
def test_cboe_futures_curve_fetcher(credentials=test_credentials):
    params = {"symbol": "VX"}

    fetcher = CboeFuturesCurveFetcher()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_cboe_index_snapshots_fetcher(credentials=test_credentials):
<<<<<<< HEAD
    params = {}
=======
    params = {"region": "eu"}
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    fetcher = CboeIndexSnapshotsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
