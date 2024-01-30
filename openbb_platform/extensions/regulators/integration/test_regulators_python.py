"""Test Regulators extension."""
<<<<<<< HEAD
import pytest
=======

import pytest
from extensions.tests.conftest import parametrize
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.model.obbject import OBBject


# pylint: disable=inconsistent-return-statements
@pytest.fixture(scope="session")
def obb(pytestconfig):
    """Fixture to setup obb."""

    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint: disable=import-outside-toplevel

        return openbb.obb


# pylint: disable=redefined-outer-name


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [
        ({"symbol": "TSLA", "provider": "sec"}),
        ({"symbol": "SQQQ", "provider": "sec"}),
    ],
)
@pytest.mark.integration
def test_regulators_sec_cik_map(params, obb):
    result = obb.regulators.sec.cik_map(**params)
    assert result
    assert isinstance(result, OBBject)
    assert hasattr(result.results, "cik")
    assert isinstance(result.results.cik, str)


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [
        ({"query": "berkshire hathaway", "provider": "sec"}),
    ],
)
@pytest.mark.integration
def test_regulators_sec_institutions_search(params, obb):
    result = obb.regulators.sec.institutions_search(**params)
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
        ({"query": "2022", "provider": "sec", "url": None}),
        (
            {
                "query": "",
                "provider": "sec",
                "url": "https://xbrl.fasb.org/us-gaap/2014/entire/",
            }
        ),
    ],
)
@pytest.mark.integration
def test_regulators_sec_schema_files(params, obb):
    result = obb.regulators.sec.schema_files(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results.files) > 0


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [
        ({"query": "0000909832", "provider": "sec"}),
        ({"query": "0001067983", "provider": "sec"}),
    ],
)
@pytest.mark.integration
def test_regulators_sec_symbol_map(params, obb):
    result = obb.regulators.sec.symbol_map(**params)
    assert result
    assert isinstance(result, OBBject)
    assert hasattr(result.results, "symbol")
    assert isinstance(result.results.symbol, str)


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [({"provider": "sec"})],
)
@pytest.mark.integration
def test_regulators_sec_rss_litigation(params, obb):
    result = obb.regulators.sec.rss_litigation(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


<<<<<<< HEAD
@pytest.mark.parametrize(
=======
@parametrize(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    "params",
    [({"query": "oil", "use_cache": False, "provider": "sec"})],
)
@pytest.mark.integration
def test_regulators_sec_sic_search(params, obb):
    result = obb.regulators.sec.sic_search(**params)
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
        ({"query": "grain", "provider": "nasdaq"}),
    ],
)
@pytest.mark.integration
def test_regulators_cftc_cot_search(params, obb):
    result = obb.regulators.cftc.cot_search(**params)
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
                "id": "13874P",
                "data_type": "FO",
                "legacy_format": True,
                "report_type": "ALL",
                "measure": "CR",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "transform": "diff",
                "provider": "nasdaq",
            }
        ),
    ],
)
@pytest.mark.integration
def test_regulators_cftc_cot(params, obb):
    result = obb.regulators.cftc.cot(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
