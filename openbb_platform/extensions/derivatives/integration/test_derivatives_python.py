"""Python interface integration tests for the derivatives extension."""

import pytest
<<<<<<< HEAD
=======
from extensions.tests.conftest import parametrize
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.model.obbject import OBBject

# pylint: disable=too-many-lines,redefined-outer-name
# pylint: disable=import-outside-toplevel,inconsistent-return-statements


@pytest.fixture(scope="session")
def obb(pytestconfig):
    """Fixture to setup obb."""
    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb

        return openbb.obb


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
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
def test_derivatives_options_chains(params, obb):
    result = obb.derivatives.options.chains(**params)
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
        ({"symbol": "AAPL"}),
        ({"provider": "intrinio", "source": "delayed", "symbol": "AAPL"}),
        ({"provider": "intrinio", "symbol": "PLTR", "source": "delayed"}),
    ],
)
@pytest.mark.integration
def test_derivatives_options_unusual(params, obb):
    result = obb.derivatives.options.unusual(**params)
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
                "start_date": "2023-05-05",
                "end_date": "2023-06-06",
                "expiration": "2024-06",
=======
                "provider": "yfinance",
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
def test_derivatives_futures_historical(params, obb):
    result = obb.derivatives.futures.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


<<<<<<< HEAD
@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "VX", "date": "2023-01-25", "provider": "cboe"}),
=======
@parametrize(
    "params",
    [
        ({"symbol": "VX", "provider": "cboe", "date": None}),
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        ({"provider": "yfinance", "symbol": "ES", "date": "2023-08-01"}),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_curve(params, obb):
    result = obb.derivatives.futures.curve(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
