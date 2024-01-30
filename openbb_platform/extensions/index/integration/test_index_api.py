import base64

import pytest
import requests
<<<<<<< HEAD
=======
from extensions.tests.conftest import parametrize
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.env import Env
from openbb_core.provider.utils.helpers import get_querystring


@pytest.fixture(scope="session")
def headers():
    userpass = f"{Env().API_USERNAME}:{Env().API_PASSWORD}"
    userpass_bytes = userpass.encode("ascii")
    base64_bytes = base64.b64encode(userpass_bytes)

    return {"Authorization": f"Basic {base64_bytes.decode('ascii')}"}


# pylint: disable=redefined-outer-name


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [({"index": "dowjones", "provider": "fmp"})],
=======
@parametrize(
    "params",
    [
        ({"index": "dowjones", "provider": "fmp"}),
        ({"index": "BUKBUS", "provider": "cboe"}),
    ],
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
)
@pytest.mark.integration
def test_index_constituents(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/constituents?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [
        (
            {
                "symbol": "^DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "provider": "fmp",
<<<<<<< HEAD
=======
                "sort": "desc",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "interval": "1m",
                "provider": "cboe",
                "symbol": "AAVE100",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
<<<<<<< HEAD
=======
                "use_cache": False,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "interval": "1d",
                "provider": "cboe",
                "symbol": "AAVE100",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
<<<<<<< HEAD
=======
                "use_cache": False,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "interval": "1min",
                "provider": "fmp",
                "symbol": "^DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "timeseries": 1,
<<<<<<< HEAD
=======
                "sort": "desc",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "interval": "1day",
                "provider": "fmp",
                "symbol": "^DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "timeseries": 1,
<<<<<<< HEAD
=======
                "sort": "desc",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "timespan": "minute",
                "sort": "desc",
                "limit": 49999,
                "adjusted": True,
                "multiplier": 1,
                "provider": "polygon",
                "symbol": "NDX",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "timespan": "day",
                "sort": "desc",
                "limit": 49999,
                "adjusted": True,
                "multiplier": 1,
                "provider": "polygon",
                "symbol": "NDX",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "interval": "1d",
                "period": "max",
                "prepost": True,
                "rounding": True,
                "provider": "yfinance",
                "symbol": "DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "provider": "intrinio",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
<<<<<<< HEAD
                "symbol": "$DJI",
                "tag": "level",
                "sort": "desc",
                "limit": 100,
                "type": None,
=======
                "symbol": "DJI",
                "sort": "desc",
                "limit": 100,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
    ],
)
@pytest.mark.integration
<<<<<<< HEAD
def test_index_market(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/market?{query_str}"
=======
def test_index_price_historical(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/price/historical?{query_str}"
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    result = requests.get(url, headers=headers, timeout=20)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [
        (
            {
<<<<<<< HEAD
                "symbol": "BUKBUS",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "provider": "cboe",
=======
                "symbol": "^DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "provider": "fmp",
                "sort": "desc",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "interval": "1m",
                "provider": "cboe",
<<<<<<< HEAD
                "symbol": "BUKBUS",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
=======
                "symbol": "AAVE100",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "use_cache": True,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
        (
            {
                "interval": "1d",
                "provider": "cboe",
<<<<<<< HEAD
                "symbol": "BUKBUS",
=======
                "symbol": "AAVE100",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "use_cache": False,
            }
        ),
        (
            {
                "interval": "1min",
                "provider": "fmp",
                "symbol": "^DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "timeseries": 1,
                "sort": "desc",
            }
        ),
        (
            {
                "interval": "1day",
                "provider": "fmp",
                "symbol": "^DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "timeseries": 1,
                "sort": "desc",
            }
        ),
        (
            {
                "timespan": "minute",
                "sort": "desc",
                "limit": 49999,
                "adjusted": True,
                "multiplier": 1,
                "provider": "polygon",
                "symbol": "NDX",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
<<<<<<< HEAD
    ],
)
@pytest.mark.integration
def test_index_european(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/european?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [({"symbol": "BUKBUS", "provider": "cboe"})],
)
@pytest.mark.integration
def test_index_european_constituents(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/european_constituents?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
=======
        (
            {
                "timespan": "day",
                "sort": "desc",
                "limit": 49999,
                "adjusted": True,
                "multiplier": 1,
                "provider": "polygon",
                "symbol": "NDX",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "interval": "1d",
                "period": "max",
                "prepost": True,
                "rounding": True,
                "provider": "yfinance",
                "symbol": "DJI",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "provider": "intrinio",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "symbol": "$DJI",
                "tag": "level",
                "sort": "desc",
                "limit": 100,
                "type": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_index_market(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/market?{query_str}"
    result = requests.get(url, headers=headers, timeout=20)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"europe": True, "provider": "cboe"}),
=======
@parametrize(
    "params",
    [
        ({"provider": "cboe", "use_cache": False}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        ({"provider": "fmp"}),
        ({"provider": "yfinance"}),
    ],
)
@pytest.mark.integration
def test_index_available(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/available?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"query": "D", "is_symbol": True, "provider": "cboe"}),
        ({"europe": True, "provider": "cboe", "query": "A", "is_symbol": False}),
=======
@parametrize(
    "params",
    [
        ({"query": "D", "is_symbol": True, "provider": "cboe", "use_cache": False}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    ],
)
@pytest.mark.integration
def test_index_search(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/search?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [({"provider": "cboe", "region": "US"})],
=======
@parametrize(
    "params",
    [({"provider": "cboe", "region": "us"})],
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
)
@pytest.mark.integration
def test_index_snapshots(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/snapshots?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [
        (
            {
                "series_name": "PE Ratio by Month",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "collapse": "monthly",
                "transform": "diff",
                "provider": "nasdaq",
            }
        )
    ],
)
@pytest.mark.integration
def test_index_sp500_multiples(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/index/sp500_multiples?{query_str}"
    result = requests.get(url, headers=headers, timeout=20)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200
