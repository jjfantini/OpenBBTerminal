<<<<<<< HEAD
=======
"""Extension class for OBBject extensions."""

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
import warnings
from typing import Callable, List, Optional


class Extension:
<<<<<<< HEAD
    """Serves as extension entry point and must be created by each extension package.

    See README.md for more information on how to create an extension.
=======
    """
    Serves as OBBject extension entry point and must be created by each extension package.

    See https://docs.openbb.co/platform/development/developer-guidelines/obbject_extensions.
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    """

    def __init__(
        self,
        name: str,
        credentials: Optional[List[str]] = None,
    ) -> None:
        """Initialize the extension.

        Parameters
        ----------
        name : str
            Name of the extension.
        credentials : Optional[List[str]], optional
            List of required credentials, by default None
        """
        self.name = name
        self.credentials = credentials or []

    @property
    def obbject_accessor(self) -> Callable:
        """Extend an OBBject, inspired by pandas."""
        # pylint: disable=import-outside-toplevel
        # Avoid circular imports

        from openbb_core.app.model.obbject import OBBject

        return self.register_accessor(self.name, OBBject)

    @staticmethod
    def register_accessor(name, cls) -> Callable:
<<<<<<< HEAD
        """Register a custom accessor"""
=======
        """Register a custom accessor."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        def decorator(accessor):
            if hasattr(cls, name):
                warnings.warn(
                    f"registration of accessor '{repr(accessor)}' under name "
                    f"'{repr(name)}' for type '{repr(cls)}' is overriding a preexisting "
                    f"attribute with the same name.",
                    UserWarning,
                )
            setattr(cls, name, CachedAccessor(name, accessor))
            # pylint: disable=protected-access
            cls._accessors.add(name)
            return accessor

        return decorator


class CachedAccessor:
<<<<<<< HEAD
    """CachedAccessor"""

    def __init__(self, name: str, accessor) -> None:
=======
    """CachedAccessor."""

    def __init__(self, name: str, accessor) -> None:
        """Initialize the cached accessor."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        self._name = name
        self._accessor = accessor

    def __get__(self, obj, cls):
<<<<<<< HEAD
=======
        """Get the cached accessor."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if obj is None:
            return self._accessor
        accessor_obj = self._accessor(obj)
        object.__setattr__(obj, self._name, accessor_obj)
        return accessor_obj
