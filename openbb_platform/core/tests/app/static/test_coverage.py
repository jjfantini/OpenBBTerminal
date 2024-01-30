"""Test the coverage.py file."""
<<<<<<< HEAD
# pylint: disable=redefined-outer-name

import pytest
=======

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.command_runner import CommandRunner
from openbb_core.app.static.app_factory import BaseApp
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.static.coverage import Coverage


@pytest.fixture(scope="module")
<<<<<<< HEAD
def coverage():
    """Return coverage."""
    return Coverage()
=======
def app():
    """Return a BaseApp instance."""
    return BaseApp(command_runner=CommandRunner())


@pytest.fixture(scope="module")
def coverage(app):
    """Return coverage."""
    return Coverage(app)  # Pass the BaseApp instance to Coverage
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


def test_coverage_init(coverage):
    """Test coverage init."""
    assert coverage


def test_coverage_providers(coverage):
    """Test coverage providers."""
    provider_coverage = coverage.providers
    assert provider_coverage
    assert isinstance(provider_coverage, dict)


def test_coverage_commands(coverage):
    """Test coverage commands."""
    command_coverage = coverage.commands
    assert command_coverage
    assert isinstance(command_coverage, dict)
