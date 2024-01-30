"""Constants for the OpenBB Platform."""
<<<<<<< HEAD
from pathlib import Path

=======

from pathlib import Path

ASSETS_DIRECTORY = Path(__file__).parent / "assets"
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
HOME_DIRECTORY = Path.home()
OPENBB_DIRECTORY = Path(HOME_DIRECTORY, ".openbb_platform")
USER_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "user_settings.json")
SYSTEM_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "system_settings.json")
