<<<<<<< HEAD
=======
"""Credentials model and its utilities."""

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
import traceback
import warnings
from typing import Dict, Optional, Set, Tuple

<<<<<<< HEAD
from importlib_metadata import entry_points
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    create_model,
)
from pydantic.functional_serializers import PlainSerializer
from typing_extensions import Annotated

<<<<<<< HEAD
from openbb_core.app.model.abstract.warning import OpenBBWarning
from openbb_core.app.model.extension import Extension
=======
from openbb_core.app.extension_loader import ExtensionLoader
from openbb_core.app.model.abstract.warning import OpenBBWarning
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.provider_interface import ProviderInterface
from openbb_core.env import Env


class LoadingError(Exception):
    """Error loading extension."""


# @model_serializer blocks model_dump with pydantic parameters (include, exclude)
OBBSecretStr = Annotated[
    SecretStr,
    PlainSerializer(
        lambda x: x.get_secret_value(), return_type=str, when_used="json-unless-none"
    ),
]


class CredentialsLoader:
<<<<<<< HEAD
    """Here we create the Credentials model"""
=======
    """Here we create the Credentials model."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    credentials: Dict[str, Set[str]] = {}

    @staticmethod
    def prepare(
        credentials: Dict[str, Set[str]],
    ) -> Dict[str, Tuple[object, None]]:
<<<<<<< HEAD
        """Prepare credentials map to be used in the Credentials model"""
=======
        """Prepare credentials map to be used in the Credentials model."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        formatted: Dict[str, Tuple[object, None]] = {}
        for origin, creds in credentials.items():
            for c in creds:
                # Not sure we should do this, if you require the same credential it breaks
                # if c in formatted:
                #     raise ValueError(f"Credential '{c}' already in use.")
                formatted[c] = (
                    Optional[OBBSecretStr],
                    Field(
                        default=None, description=origin
                    ),  # register the credential origin (obbject, providers)
                )

        return formatted

    def from_obbject(self) -> None:
<<<<<<< HEAD
        """Load credentials from OBBject extensions"""
        self.credentials["obbject"] = set()
        for entry_point in sorted(entry_points(group="openbb_obbject_extension")):
            try:
                entry = entry_point.load()
                if isinstance(entry, Extension):
                    for c in entry.credentials:
                        self.credentials["obbject"].add(c)
            except Exception as e:
                msg = f"Error loading extension: {entry_point.name}\n"
=======
        """Load credentials from OBBject extensions."""
        self.credentials["obbject"] = set()
        for name, entry in ExtensionLoader().obbject_objects.items():
            try:
                for c in entry.credentials:
                    self.credentials["obbject"].add(c)
            except Exception as e:
                msg = f"Error loading extension: {name}\n"
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
                if Env().DEBUG_MODE:
                    traceback.print_exception(type(e), e, e.__traceback__)
                    raise LoadingError(msg + f"\033[91m{e}\033[0m") from e
                warnings.warn(
                    message=msg,
                    category=OpenBBWarning,
                )

    def from_providers(self) -> None:
<<<<<<< HEAD
        """Load credentials from providers"""
=======
        """Load credentials from providers."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        self.credentials["providers"] = set()
        for c in ProviderInterface().credentials:
            self.credentials["providers"].add(c)

    def load(self) -> BaseModel:
<<<<<<< HEAD
        """Load credentials from providers"""
=======
        """Load credentials from providers."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        # We load providers first to give them priority choosing credential names
        self.from_providers()
        self.from_obbject()
        return create_model(  # type: ignore
            "Credentials",
            __config__=ConfigDict(validate_assignment=True),
            **self.prepare(self.credentials),
        )


_Credentials = CredentialsLoader().load()


class Credentials(_Credentials):  # type: ignore
<<<<<<< HEAD
    """Credentials model used to store provider credentials"""

    def __repr__(self) -> str:
        """String representation of the credentials"""
=======
    """Credentials model used to store provider credentials."""

    def __repr__(self) -> str:
        """String representation of the credentials."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return (
            self.__class__.__name__
            + "\n\n"
            + "\n".join([f"{k}: {v}" for k, v in sorted(self.__dict__.items())])
        )

    def show(self):
<<<<<<< HEAD
        """Unmask credentials and print them"""
=======
        """Unmask credentials and print them."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        print(  # noqa: T201
            self.__class__.__name__
            + "\n\n"
            + "\n".join(
                [f"{k}: {v}" for k, v in sorted(self.model_dump(mode="json").items())]
            )
        )
