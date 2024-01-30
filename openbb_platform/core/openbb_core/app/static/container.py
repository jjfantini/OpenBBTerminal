"""Container class."""
<<<<<<< HEAD
from typing import Union

import pandas as pd
=======

from typing import Any
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.app.command_runner import CommandRunner
from openbb_core.app.model.obbject import OBBject


class Container:
    """Container class for the command runner session."""

    def __init__(self, command_runner: CommandRunner) -> None:
        self._command_runner = command_runner
        OBBject._credentials = command_runner.user_settings.credentials

<<<<<<< HEAD
    def _run(self, *args, **kwargs) -> Union[OBBject, pd.DataFrame, dict]:
=======
    def _run(self, *args, **kwargs) -> Any:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        """Run a command in the container."""
        obbject = self._command_runner.sync_run(*args, **kwargs)
        output_type = self._command_runner.user_settings.preferences.output_type
        if output_type == "OBBject":
            return obbject
        return getattr(obbject, "to_" + output_type)()
