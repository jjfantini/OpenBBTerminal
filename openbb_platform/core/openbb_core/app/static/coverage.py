"""Coverage module."""
<<<<<<< HEAD
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.app.router import CommandMap


class Coverage:
    """/coverage

    providers
    commands
    command_model
    """

    def __init__(self):
        """Initialize coverage."""
=======

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from openbb_core.api.router.helpers.coverage_helpers import get_route_schema_map
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.app.router import CommandMap

if TYPE_CHECKING:
    from openbb_core.app.static.app_factory import BaseApp


class Coverage:
    """Coverage class.

    /coverage

        providers
        commands
        command_model
        command_schemas
    """

    def __init__(self, app: "BaseApp"):
        """Initialize coverage."""
        self._app = app
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        self._command_map = CommandMap(coverage_sep=".")
        self._provider_interface = ProviderInterface()

    def __repr__(self) -> str:
        """Return docstring."""
        return self.__doc__ or ""

    @property
<<<<<<< HEAD
    def providers(self):
=======
    def providers(self) -> Dict[str, List[str]]:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        """Return providers coverage."""
        return self._command_map.provider_coverage

    @property
<<<<<<< HEAD
    def commands(self):
=======
    def commands(self) -> Dict[str, List[str]]:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        """Return commands coverage."""
        return self._command_map.command_coverage

    @property
<<<<<<< HEAD
    def command_model(self):
        """Return command to model mapping."""
        return {
            command: self._provider_interface.map[
                self._command_map.commands_model[command]
            ]
            for command in self._command_map.commands_model  # pylint: disable=C0206
        }
=======
    def command_model(self) -> Dict[str, Dict[str, Dict[str, Dict[str, Any]]]]:
        """Return command to model mapping."""
        return {
            command: self._provider_interface.map[value]
            for command, value in self._command_map.commands_model.items()
        }

    def command_schemas(self, filter_by_provider: Optional[str] = None):
        """Return route schema for a command."""
        return get_route_schema_map(
            self._app, self._command_map.commands_model, filter_by_provider
        )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
