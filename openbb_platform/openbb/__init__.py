"""OpenBB Platform."""
<<<<<<< HEAD
# flake8: noqa

import os
=======

# flake8: noqa

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from pathlib import Path
from typing import List, Optional, Union

from openbb_core.app.static.app_factory import (
    BaseApp as _BaseApp,
    create_app as _create_app,
)
<<<<<<< HEAD
from openbb_core.app.static.build_utils import (
    auto_build as _auto_build,
    build as _build,
)

_this_dir = Path(os.path.dirname(os.path.realpath(__file__)))
=======
from openbb_core.app.static.package_builder import PackageBuilder as _PackageBuilder

_this_dir = Path(__file__).parent.resolve()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe


def build(
    modules: Optional[Union[str, List[str]]] = None,
    lint: bool = True,
    verbose: bool = False,
) -> None:
    """Build extension modules.

    Parameters
    ----------
    modules : Optional[List[str]], optional
        The modules to rebuild, by default None
        For example: "/news" or ["/news", "/crypto"]
        If None, all modules are rebuilt.
    lint : bool, optional
        Whether to lint the code, by default True
    verbose : bool, optional
        Enable/disable verbose mode
    """
<<<<<<< HEAD
    _build(directory=_this_dir, modules=modules, lint=lint, verbose=verbose)


_auto_build(directory=_this_dir)
=======
    _PackageBuilder(_this_dir, lint, verbose).build(modules)


_PackageBuilder(_this_dir).auto_build()
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

try:
    # pylint: disable=import-outside-toplevel
    from openbb.package.__extensions__ import Extensions as _Extensions

    obb: Union[_BaseApp, _Extensions] = _create_app(_Extensions)  # type: ignore
    sdk = obb
except (ImportError, ModuleNotFoundError):
    print("Failed to import extensions.")
    obb = sdk = _create_app()  # type: ignore
