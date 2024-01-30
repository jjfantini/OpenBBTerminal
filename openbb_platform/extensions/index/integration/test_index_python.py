"""Test economy extension."""

import pytest
<<<<<<< HEAD
=======
from extensions.tests.conftest import parametrize
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.model.obbject import OBBject


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
    """Fixture to setup obb."""

    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint: disable=import-outside-toplevel

        return openbb.obb


# pylint: disable=redefined-outer-name


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"index": "dowjones"}),
=======
@parametrize(
    "params",
    [
        ({"index": "dowjones", "provider": "fmp"}),
        ({"index": "BUKBUS", "provider": "cboe"}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    ],
)
@pytest.mark.integration
def test_index_constituents(params, obb):
    result = obb.index.constituents(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


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
                "symbol": "AAVE100",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
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
def test_index_market(params, obb):
    result = obb.index.market(**params)
=======
def test_index_price_historical(params, obb):
    result = obb.index.price.historical(**params)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


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
=======
                "symbol": "AAVE100",
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
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
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
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
                "symbol": "$DJI",
                "tag": "level",
                "sort": "desc",
                "limit": 100,
                "type": None,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            }
        ),
    ],
)
@pytest.mark.integration
<<<<<<< HEAD
def test_index_european(params, obb):
    result = obb.index.european(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "BUKBUS"}),
    ],
)
@pytest.mark.integration
def test_index_european_constituents(params, obb):
    result = obb.index.european_constituents(**params)
=======
def test_index_market(params, obb):
    result = obb.index.market(**params)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({}),
        ({"europe": True, "provider": "cboe"}),
=======
@parametrize(
    "params",
    [
        ({}),
        ({"provider": "cboe", "use_cache": False}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        ({"provider": "fmp"}),
        ({"provider": "yfinance"}),
    ],
)
@pytest.mark.integration
def test_index_available(params, obb):
    result = obb.index.available(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"query": "D", "is_symbol": True}),
        ({"europe": True, "provider": "cboe", "query": "A", "is_symbol": False}),
=======
@parametrize(
    "params",
    [
        ({"query": "D", "is_symbol": True, "use_cache": False, "provider": "cboe"}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    ],
)
@pytest.mark.integration
def test_index_search(params, obb):
    result = obb.index.search(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"region": "US"}),
=======
@parametrize(
    "params",
    [
        ({"region": "us", "provider": "cboe"}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    ],
)
@pytest.mark.integration
def test_index_snapshots(params, obb):
    result = obb.index.snapshots(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


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
        ),
    ],
)
@pytest.mark.integration
def test_index_sp500_multiples(params, obb):
    result = obb.index.sp500_multiples(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
