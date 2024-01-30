"""Test the coverate module."""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
import asyncio
from unittest.mock import MagicMock

from openbb_core.api.dependency.coverage import get_command_map


def test_get_system_settings():
    """Test get_system_settings."""

    response = asyncio.run(get_command_map(MagicMock()))

    assert response
