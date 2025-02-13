<<<<<<< HEAD
import pytest


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
@pytest.mark.integration
def test_econometrics_corr():
    ...


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
@pytest.mark.integration
def test_econometrics_ols_summary():
    ...


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
@pytest.mark.integration
def test_econometrics_dwat():
    ...


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
@pytest.mark.integration
def test_econometrics_bgot():
    ...


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
def test_econometrics_coint():
    ...


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
@pytest.mark.integration
def test_econometrics_granger():
    ...


@pytest.mark.skip(reason="econometrics is a python only extensions so far")
@pytest.mark.integration
def test_econometrics_unitroot():
    ...
=======
"""Test econometrics extension."""

import base64
import json
import random
from typing import Dict, Literal

import pytest
import requests
from openbb_core.env import Env
from openbb_core.provider.utils.helpers import get_querystring

data: Dict = {}


def get_headers():
    if "headers" in data:
        return data["headers"]

    userpass = f"{Env().API_USERNAME}:{Env().API_PASSWORD}"
    userpass_bytes = userpass.encode("ascii")
    base64_bytes = base64.b64encode(userpass_bytes)

    data["headers"] = {"Authorization": f"Basic {base64_bytes.decode('ascii')}"}
    return data["headers"]


def request_data(menu: str, symbol: str, provider: str):
    """Randomly pick a symbol and a provider and get data from the selected menu."""
    url = f"http://0.0.0.0:8000/api/v1/{menu}/price/historical?symbol={symbol}&provider={provider}"
    result = requests.get(url, headers=get_headers(), timeout=10)
    return result.json()["results"]


def get_equity_data():
    if "equity_data" in data:
        return data["equity_data"]

    symbol = random.choice(["AAPL", "NVDA", "MSFT", "TSLA", "AMZN", "V"])  # noqa: S311
    provider = random.choice(["fmp", "intrinio", "polygon"])  # noqa: S311

    data["equity_data"] = request_data("equity", symbol=symbol, provider=provider)
    return data["equity_data"]


def get_crypto_data():
    if "crypto_data" in data:
        return data["crypto_data"]

    # TODO : add more crypto providers and symbols
    symbol = random.choice(["BTC"])  # noqa: S311
    provider = random.choice(["fmp"])  # noqa: S311

    data["crypto_data"] = request_data(
        menu="crypto",
        symbol=symbol,
        provider=provider,
    )
    return data["crypto_data"]


def get_data(menu: Literal["equity", "crypto"]):
    funcs = {"equity": get_equity_data, "crypto": get_crypto_data}
    return funcs[menu]()


@pytest.mark.parametrize(
    "params, data_type",
    [
        ({"data": ""}, "equity"),
        ({"data": ""}, "crypto"),
    ],
)
@pytest.mark.integration
def test_econometrics_correlation_matrix(params, data_type):
    params = {p: v for p, v in params.items() if v}

    body = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/econometrics/correlation_matrix?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params, data_type",
    [
        (
            {"data": "", "y_column": "close", "x_columns": ["high"]},
            "equity",
        ),
        (
            {"data": "", "y_column": "close", "x_columns": ["high"]},
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_econometrics_ols_regression_summary(params, data_type):
    params = {p: v for p, v in params.items() if v}

    body = json.dumps(
        {
            "data": get_data(data_type),
            "x_columns": params.pop("x_columns"),
        }
    )

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/econometrics/ols_regression_summary?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=20, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params, data_type",
    [
        (
            {"data": "", "y_column": "volume", "x_columns": ["close"]},
            "equity",
        ),
        (
            {"data": "", "y_column": "volume", "x_columns": ["close"]},
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_econometrics_autocorrelation(params, data_type):
    params = {p: v for p, v in params.items() if v}

    body = json.dumps(
        {
            "data": get_data(data_type),
            "x_columns": params.pop("x_columns"),
        }
    )

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/econometrics/autocorrelation?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "y_column": "volume",
                "x_columns": ["close"],
                "lags": "",
            },
            "equity",
        ),
        (
            {
                "data": "",
                "y_column": "volume",
                "x_columns": ["close"],
                "lags": "2",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_econometrics_residual_autocorrelation(params, data_type):
    params = {p: v for p, v in params.items() if v}

    body = json.dumps(
        {
            "data": get_data(data_type),
            "x_columns": params.pop("x_columns"),
        }
    )

    query_str = get_querystring(params, [])
    url = (
        f"http://0.0.0.0:8000/api/v1/econometrics/residual_autocorrelation?{query_str}"
    )
    result = requests.post(url, headers=get_headers(), timeout=10, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "columns": ["close", "volume"],
            },
            "equity",
        ),
        (
            {
                "data": "",
                "columns": ["close", "volume"],
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_econometrics_cointegration(params, data_type):
    params = {p: v for p, v in params.items() if v}

    body = json.dumps(
        {
            "data": get_data(data_type),
            "columns": params.pop("columns"),
        }
    )

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/econometrics/cointegration?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params, data_type",
    [
        (
            {"data": "", "y_column": "volume", "x_column": "close", "lag": ""},
            "equity",
        ),
        (
            {"data": "", "y_column": "volume", "x_column": "close", "lag": "2"},
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_econometrics_causality(params, data_type):
    params = {p: v for p, v in params.items() if v}
    body = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/econometrics/causality?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params, data_type",
    [({"data": "", "column": "high", "regression": "c"}, "equity")],
)
@pytest.mark.integration
def test_econometrics_unit_root(params, data_type):
    params = {p: v for p, v in params.items() if v}
    body = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/econometrics/unit_root?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=body)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
