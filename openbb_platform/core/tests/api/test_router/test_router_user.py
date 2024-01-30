"""Test the router settings.py module."""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
import asyncio
from unittest.mock import Mock

from openbb_core.api.router.user import read_user_settings

# ruff: noqa: S106


def test_read_user_settings():
    """Test read user settings."""
    mock_user_settings = Mock()

    result = asyncio.run(read_user_settings(user_settings=mock_user_settings))

    assert result == mock_user_settings
