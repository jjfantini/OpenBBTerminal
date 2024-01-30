"""Test the system module."""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
import asyncio
from unittest.mock import MagicMock, patch

from openbb_core.api.dependency.system import (
    SystemSettings,
    get_system_settings,
)


@patch("openbb_core.api.dependency.system.SystemService")
def test_get_system_settings(mock_system_service):
    """Test get_system_settings."""
    mock_system_service.return_value.system_settings = SystemSettings()

    response = asyncio.run(get_system_settings(MagicMock(), mock_system_service))

    assert response
