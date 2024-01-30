"""API integration tests for the derivatives extension."""

import base64

import pytest
import requests
<<<<<<< HEAD
=======
from extensions.tests.conftest import parametrize
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.env import Env
from openbb_core.provider.utils.helpers import get_querystring

# pylint: disable=too-many-lines,redefined-outer-name


@pytest.fixture(scope="session")
def headers():
    userpass = f"{Env().API_USERNAME}:{Env().API_PASSWORD}"
    userpass_bytes = userpass.encode("ascii")
    base64_bytes = base64.b64encode(userpass_bytes)

    return {"Authorization": f"Basic {base64_bytes.decode('ascii')}"}


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "intrinio", "symbol": "AAPL", "date": "2023-01-25"}),
        ({"provider": "cboe", "symbol": "AAPL"}),
=======
@parametrize(
    "params",
    [
        ({"provider": "intrinio", "symbol": "AAPL", "date": "2023-01-25"}),
        ({"provider": "cboe", "symbol": "AAPL", "use_cache": False}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    ],
)
@pytest.mark.integration
def test_derivatives_options_chains(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/options/chains?{query_str}"
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
        ({"symbol": "AAPL"}),
        ({"provider": "intrinio", "source": "delayed", "symbol": "AAPL"}),
        ({"provider": "intrinio", "symbol": "PLTR", "source": "delayed"}),
    ],
)
@pytest.mark.integration
def test_derivatives_options_unusual(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/options/unusual?{query_str}"
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
                "provider": "yfinance",
<<<<<<< HEAD
                "symbol": "ES",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "expiration": "2024-06",
            }
        ),
        (
            {
                "provider": "yfinance",
                "interval": "1d",
                "period": "max",
                "prepost": True,
                "adjust": True,
                "back_adjust": True,
                "symbol": "ES",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "expiration": "2024-06",
=======
                "interval": "1d",
                "symbol": "CL,BZ",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "expiration": "2025-12",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_historical(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/futures/historical?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "cboe", "symbol": "VX", "date": "2023-01-25"}),
=======
@parametrize(
    "params",
    [
        ({"provider": "cboe", "symbol": "VX", "date": None}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        ({"provider": "yfinance", "symbol": "ES", "date": "2023-08-01"}),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_curve(params, headers):
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/futures/curve?{query_str}"
    result = requests.get(url, headers=headers, timeout=30)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200
