<<<<<<< HEAD
=======
"""OpenBB Router."""

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
import traceback
import warnings
from functools import lru_cache, partial
from inspect import Parameter, Signature, isclass, iscoroutinefunction, signature
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    Optional,
    Type,
    Union,
    get_args,
    get_origin,
    get_type_hints,
    overload,
)

from fastapi import APIRouter, Depends
<<<<<<< HEAD
from importlib_metadata import entry_points
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from pydantic import BaseModel
from pydantic.v1.validators import find_validators
from typing_extensions import Annotated, ParamSpec, _AnnotatedAlias

<<<<<<< HEAD
=======
from openbb_core.app.example_generator import ExampleGenerator
from openbb_core.app.extension_loader import ExtensionLoader
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.model.abstract.warning import OpenBBWarning
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    ProviderInterface,
    StandardParams,
)
from openbb_core.env import Env

P = ParamSpec("P")


class OpenBBErrorResponse(BaseModel):
    """OpenBB Error Response."""

    detail: str
    error_kind: str


class CommandValidator:
<<<<<<< HEAD
=======
    """Validate Command."""

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    @staticmethod
    def is_standard_pydantic_type(value_type: Type) -> bool:
        """Check whether or not a parameter type is a valid Pydantic Standard Type."""
        try:
            func = next(
<<<<<<< HEAD
                find_validators(value_type, config=dict(arbitrary_types_allowed=True))
=======
                find_validators(value_type, config=dict(arbitrary_types_allowed=True))  # type: ignore
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            )
            valid_type = func.__name__ != "arbitrary_type_validator"
        except Exception:
            valid_type = False

        return valid_type

    @staticmethod
    def is_valid_pydantic_model_type(model_type: Type) -> bool:
<<<<<<< HEAD
=======
        """Check whether or not a parameter type is a valid Pydantic Model Type."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if not isclass(model_type):
            return False

        if issubclass(model_type, BaseModel):
            try:
                model_type.model_json_schema()
                return True
            except ValueError:
                return False
        return False

    @classmethod
    def is_serializable_value_type(cls, value_type: Type) -> bool:
<<<<<<< HEAD
=======
        """Check whether or not a parameter type is a valid serializable type."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return cls.is_standard_pydantic_type(
            value_type=value_type
        ) or cls.is_valid_pydantic_model_type(model_type=value_type)

    @staticmethod
    def is_annotated_dc(annotation) -> bool:
<<<<<<< HEAD
=======
        """Check whether or not a parameter type is an annotated dataclass."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return isinstance(annotation, _AnnotatedAlias) and hasattr(
            annotation.__args__[0], "__dataclass_fields__"
        )

    @staticmethod
    def check_reserved_param(
        name: str,
        expected_annot: Any,
        parameter_map: Mapping[str, Parameter],
        func: Callable,
        sig: Signature,
    ):
<<<<<<< HEAD
=======
        """Check whether or not a parameter is reserved."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if name in parameter_map:
            annotation = getattr(parameter_map[name], "annotation", None)
            if annotation is not None and CommandValidator.is_annotated_dc(annotation):
                annotation = annotation.__args__[0].__bases__[0]
            if not annotation == expected_annot:
                raise TypeError(
                    f"The parameter `{name}` must be a {expected_annot}.\n"
                    f"module    = {func.__module__}\n"
                    f"function  = {func.__name__}\n"
                    f"signature = {sig}\n"
                )

    @classmethod
    def check_parameters(cls, func: Callable):
<<<<<<< HEAD
=======
        """Check whether or not a parameter is a valid."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        sig = signature(func)
        parameter_map = sig.parameters

        check_reserved = partial(
            cls.check_reserved_param, parameter_map=parameter_map, func=func, sig=sig
        )
        check_reserved("cc", CommandContext)
        check_reserved("provider_choices", ProviderChoices)
        check_reserved("standard_params", StandardParams)
        check_reserved("extra_params", ExtraParams)

        for parameter in parameter_map.values():
            if not cls.is_serializable_value_type(value_type=parameter.annotation):
                raise TypeError(
                    "Invalid parameter type, please provide a serializable type like:"
                    "BaseModel, Pydantic Standard Type or CommandContext.\n"
                    f"module    = {func.__module__}\n"
                    f"function  = {func.__name__}\n"
                    f"signature = {sig}\n"
                    f"parameter = {parameter}\n"
                )

    @classmethod
    def check_return(cls, func: Callable):
<<<<<<< HEAD
=======
        """Check whether or not a return type is a valid."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        sig = signature(func)
        return_type = sig.return_annotation

        valid_return_type = False

        if isclass(return_type) and issubclass(return_type, OBBject):
            results_type = return_type.__pydantic_generic_metadata__.get("args", [])[
                0
            ]  # type: ignore
            if not isinstance(results_type, type(None)):
                generic_type_list = get_args(results_type)
                if len(generic_type_list) >= 1:
                    valid_return_type = cls.is_serializable_value_type(
                        value_type=generic_type_list[len(generic_type_list) - 1]
                    )
                else:
                    valid_return_type = cls.is_serializable_value_type(
                        value_type=results_type
                    )

        if not valid_return_type:
            raise TypeError(
                "\nInvalid function: "
                f"    {func.__module__}.{func.__name__}\n"
                "Invalid return type in signature:"
                f"    {func.__name__}(...) -> {sig.return_annotation}:\n"
                "Allowed return type:"
                f"    {func.__name__}(...) -> OBBject[T] :\n"
                "If you need T = None, use an empty model instead.\n"
            )

    @classmethod
    def check(cls, func: Callable, model: str = ""):
<<<<<<< HEAD
=======
        """Check whether or not a function is valid."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if model and not iscoroutinefunction(func):
            raise TypeError(
                f"Invalid function: {func.__module__}.{func.__name__}\n"
                "Model is specified but function is not async.\n"
                "\n\n"
                '\033[92m@router.command(model="WorldNews")\n'
                "async def world(\n"
                "    cc: CommandContext,\n"
                "    provider_choices: ProviderChoices,\n"
                "    standard_params: StandardParams,\n"
                "    extra_params: ExtraParams,\n"
                ") -> OBBject[BaseModel]:\n"
                '    """World News. Global news data."""\n'
                "    return await OBBject.from_query(Query(**locals()))\033[0m"
            )

        cls.check_return(func=func)
        cls.check_parameters(func=func)


class Router:
<<<<<<< HEAD
    @property
    def api_router(self) -> APIRouter:
=======
    """OpenBB Router Class."""

    @property
    def api_router(self) -> APIRouter:
        """API Router."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return self._api_router

    def __init__(
        self,
        prefix: str = "",
    ) -> None:
<<<<<<< HEAD
=======
        """Initialize Router."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        self._api_router = APIRouter(
            prefix=prefix,
            responses={404: {"description": "Not found"}},
        )

    @overload
    def command(self, func: Optional[Callable[P, OBBject]]) -> Callable[P, OBBject]:
        pass

    @overload
    def command(self, **kwargs) -> Callable:
        pass

    def command(
        self,
        func: Optional[Callable[P, OBBject]] = None,
        **kwargs,
    ) -> Optional[Callable]:
<<<<<<< HEAD
=======
        """Command decorator for routes."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if func is None:
            return lambda f: self.command(f, **kwargs)

        api_router = self._api_router

        model = kwargs.pop("model", "")
<<<<<<< HEAD
        if model:
            kwargs["response_model_exclude_unset"] = True
            kwargs["openapi_extra"] = {"model": model}

        func = SignatureInspector.complete_signature(func, model)

        if func:
            CommandValidator.check(func=func, model=model)

=======
        deprecation_message = kwargs.pop("deprecation_message", None)
        examples = kwargs.pop("examples", [])
        exclude_auto_examples = kwargs.pop("exclude_auto_examples", False)

        if func := SignatureInspector.complete(func, model):
            if not exclude_auto_examples:
                examples.insert(
                    0,
                    ExampleGenerator.generate(
                        route=SignatureInspector.get_operation_id(func, sep="."),
                        model=model,
                    ),
                )

            kwargs["response_model_exclude_unset"] = True
            kwargs["openapi_extra"] = kwargs.get("openapi_extra", {})
            kwargs["openapi_extra"]["model"] = model
            kwargs["openapi_extra"]["examples"] = examples
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            kwargs["operation_id"] = kwargs.get(
                "operation_id", SignatureInspector.get_operation_id(func)
            )
            kwargs["path"] = kwargs.get("path", f"/{func.__name__}")
            kwargs["endpoint"] = func
            kwargs["methods"] = kwargs.get("methods", ["GET"])
            kwargs["response_model"] = kwargs.get(
                "response_model",
                func.__annotations__["return"],  # type: ignore
            )
            kwargs["response_model_by_alias"] = kwargs.get(
                "response_model_by_alias", False
            )
            kwargs["description"] = SignatureInspector.get_description(func)
            kwargs["responses"] = kwargs.get(
                "responses",
                {
                    400: {
                        "model": OpenBBErrorResponse,
                        "description": "No Results Found",
                    },
                    404: {"description": "Not found"},
                    500: {
                        "model": OpenBBErrorResponse,
                        "description": "Internal Error",
                    },
                },
            )

<<<<<<< HEAD
=======
            # For custom deprecation messages
            if kwargs.get("deprecated", False):
                if deprecation_message:
                    kwargs["summary"] = deprecation_message
                else:
                    kwargs["summary"] = (
                        "This functionality will be deprecated in the future releases."
                    )

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            api_router.add_api_route(**kwargs)

        return func

    def include_router(
        self,
        router: "Router",
        prefix: str = "",
    ):
<<<<<<< HEAD
=======
        """Include router."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        tags = [prefix[1:]] if prefix else None
        self._api_router.include_router(
            router=router.api_router, prefix=prefix, tags=tags  # type: ignore
        )


class SignatureInspector:
<<<<<<< HEAD
    @classmethod
    def complete_signature(
        cls, func: Callable[P, OBBject], model: str
    ) -> Optional[Callable[P, OBBject]]:
        """Complete function signature."""

=======
    """Inspect function signature."""

    @classmethod
    def complete(
        cls, func: Callable[P, OBBject], model: str
    ) -> Optional[Callable[P, OBBject]]:
        """Complete function signature."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        if isclass(return_type := func.__annotations__["return"]) and not issubclass(
            return_type, OBBject
        ):
            return func

        provider_interface = ProviderInterface()

        if model:
            if model not in provider_interface.models:
                if Env().DEBUG_MODE:
                    warnings.warn(
                        message=f"\nSkipping api route '/{func.__name__}'.\n"
                        f"Model '{model}' not found.\n\n"
                        "Check available models in ProviderInterface().models",
                        category=OpenBBWarning,
                    )
                return None
<<<<<<< HEAD

=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            cls.validate_signature(
                func,
                {
                    "provider_choices": ProviderChoices,
                    "standard_params": StandardParams,
                    "extra_params": ExtraParams,
                },
            )

            func = cls.inject_dependency(
                func=func,
                arg="provider_choices",
                callable_=provider_interface.model_providers[model],
            )

            func = cls.inject_dependency(
                func=func,
                arg="standard_params",
                callable_=provider_interface.params[model]["standard"],
            )

            func = cls.inject_dependency(
                func=func,
                arg="extra_params",
                callable_=provider_interface.params[model]["extra"],
            )

            func = cls.inject_return_type(
                func=func,
                inner_type=provider_interface.return_schema[model],
                outer_type=provider_interface.return_map[model],
            )
        else:
            func = cls.polish_return_schema(func)
            if (
                "provider_choices" in func.__annotations__
                and func.__annotations__["provider_choices"] == ProviderChoices
            ):
                func = cls.inject_dependency(
                    func=func,
                    arg="provider_choices",
                    callable_=provider_interface.provider_choices,
                )

        return func

    @staticmethod
    def inject_return_type(
        func: Callable[P, OBBject], inner_type: Any, outer_type: Any
    ) -> Callable[P, OBBject]:
<<<<<<< HEAD
        """Inject full return model into the function.
        Also updates __name__ and __doc__ for API schemas."""
        ReturnModel = inner_type
        if get_origin(outer_type) == list:
            ReturnModel = List[inner_type]  # type: ignore
        elif get_origin(outer_type) == Union:
=======
        """
        Inject full return model into the function.

        Also updates __name__ and __doc__ for API schemas.
        """
        ReturnModel = inner_type
        outer_type_origin = get_origin(outer_type)

        if outer_type_origin == list:
            ReturnModel = List[inner_type]  # type: ignore
        elif outer_type_origin == Union:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            ReturnModel = Union[List[inner_type], inner_type]  # type: ignore

        return_type = OBBject[ReturnModel]  # type: ignore
        return_type.__name__ = f"OBBject[{inner_type.__name__}]"
        return_type.__doc__ = f"OBBject with results of type '{inner_type.__name__}'."
<<<<<<< HEAD
        return_type.model_rebuild(force=True)
=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

        func.__annotations__["return"] = return_type
        return func

    @staticmethod
    def polish_return_schema(func: Callable[P, OBBject]) -> Callable[P, OBBject]:
<<<<<<< HEAD
        """Polish API schemas by filling __doc__ and __name__"""
=======
        """Polish API schemas by filling `__doc__` and `__name__`."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return_type = func.__annotations__["return"]
        is_list = False

        results_type = get_type_hints(return_type)["results"]
<<<<<<< HEAD
        if not isinstance(results_type, type(None)):
            results_type = get_args(results_type)[0]

        is_list = get_origin(results_type) == list
        args = get_args(results_type)
        inner_type = args[0] if is_list and args else results_type
=======
        results_type_args = get_args(results_type)
        if not isinstance(results_type, type(None)):
            results_type = results_type_args[0]

        is_list = get_origin(results_type) == list
        inner_type = (
            results_type_args[0] if is_list and results_type_args else results_type
        )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        inner_type_name = getattr(inner_type, "__name__", inner_type)

        func.__annotations__["return"].__doc__ = "OBBject"
        func.__annotations__["return"].__name__ = f"OBBject[{inner_type_name}]"

        return func

    @staticmethod
    def validate_signature(
        func: Callable[P, OBBject], expected: Dict[str, type]
    ) -> None:
        """Validate function signature before binding to model."""
        for k, v in expected.items():
            if k not in func.__annotations__:
                raise AttributeError(
                    f"Invalid signature: '{func.__name__}'. Missing '{k}' parameter."
                )

            if func.__annotations__[k] != v:
                raise TypeError(
                    f"Invalid signature: '{func.__name__}'. '{k}' parameter must be of type '{v.__name__}'."
                )

    @staticmethod
    def inject_dependency(
        func: Callable[P, OBBject], arg: str, callable_: Any
    ) -> Callable[P, OBBject]:
        """Annotate function with dependency injection."""
        func.__annotations__[arg] = Annotated[callable_, Depends()]  # type: ignore
        return func

    @staticmethod
    def get_description(func: Callable) -> str:
        """Get description from docstring."""
        doc = func.__doc__
        if doc:
            description = doc.split("    Parameters\n    ----------")[0]
            description = description.split("    Returns\n    -------")[0]
<<<<<<< HEAD
=======
            description = description.split("    Example\n    -------")[0]
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            description = "\n".join([line.strip() for line in description.split("\n")])

            return description
        return ""

    @staticmethod
<<<<<<< HEAD
    def get_operation_id(func: Callable) -> str:
        """Get operation id"""
=======
    def get_operation_id(func: Callable, sep: str = "_") -> str:
        """Get operation id."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        operation_id = [
            t.replace("_router", "").replace("openbb_", "")
            for t in func.__module__.split(".") + [func.__name__]
        ]
<<<<<<< HEAD
        cleaned_id = "_".join({c: "" for c in operation_id if c}.keys())
=======
        cleaned_id = sep.join({c: "" for c in operation_id if c}.keys())
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return cleaned_id


class CommandMap:
    """Matching Routes with Commands."""

    def __init__(
        self, router: Optional[Router] = None, coverage_sep: Optional[str] = None
    ) -> None:
<<<<<<< HEAD
        self._router = router or RouterLoader.from_extensions()
        self._map = self.get_command_map(router=self._router)
        self._provider_coverage = self.get_provider_coverage(
            router=self._router, sep=coverage_sep
        )
        self._command_coverage = self.get_command_coverage(
            router=self._router, sep=coverage_sep
        )
        self._commands_model = self.get_commands_model(
            router=self._router, sep=coverage_sep
        )

    @property
    def map(self) -> Dict[str, Callable]:
=======
        """Initialize CommandMap."""
        self._router = router or RouterLoader.from_extensions()
        self._map = self.get_command_map(router=self._router)
        self._provider_coverage: Dict[str, List[str]] = {}
        self._command_coverage: Dict[str, List[str]] = {}
        self._commands_model: Dict[str, str] = {}
        self._coverage_sep = coverage_sep

    @property
    def map(self) -> Dict[str, Callable]:
        """Get command map."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return self._map

    @property
    def provider_coverage(self) -> Dict[str, List[str]]:
<<<<<<< HEAD
=======
        """Get provider coverage."""
        if not self._provider_coverage:
            self._provider_coverage = self.get_provider_coverage(
                router=self._router, sep=self._coverage_sep
            )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return self._provider_coverage

    @property
    def command_coverage(self) -> Dict[str, List[str]]:
<<<<<<< HEAD
        return self._command_coverage

    @property
    def commands_model(self) -> Dict[str, List[str]]:
=======
        """Get command coverage."""
        if not self._command_coverage:
            self._command_coverage = self.get_command_coverage(
                router=self._router, sep=self._coverage_sep
            )
        return self._command_coverage

    @property
    def commands_model(self) -> Dict[str, str]:
        """Get commands model."""
        if not self._commands_model:
            self._commands_model = self.get_commands_model(
                router=self._router, sep=self._coverage_sep
            )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return self._commands_model

    @staticmethod
    def get_command_map(
        router: Router,
    ) -> Dict[str, Callable]:
<<<<<<< HEAD
=======
        """Get command map."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        api_router = router.api_router
        command_map = {route.path: route.endpoint for route in api_router.routes}  # type: ignore
        return command_map

    @staticmethod
    def get_provider_coverage(
        router: Router, sep: Optional[str] = None
    ) -> Dict[str, List[str]]:
<<<<<<< HEAD
=======
        """Get provider coverage."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        api_router = router.api_router

        mapping = ProviderInterface().map

        coverage_map: Dict[Any, Any] = {}
        for route in api_router.routes:
            openapi_extra = getattr(route, "openapi_extra")
            if openapi_extra:
                model = openapi_extra.get("model", None)
                if model:
                    providers = list(mapping[model].keys())
                    if "openbb" in providers:
                        providers.remove("openbb")
                    for provider in providers:
                        if provider not in coverage_map:
                            coverage_map[provider] = []
                        if hasattr(route, "path"):
                            rp = (
                                route.path  # type: ignore
                                if sep is None
                                else route.path.replace("/", sep)  # type: ignore
                            )
                            coverage_map[provider].append(rp)

        return coverage_map

    @staticmethod
    def get_command_coverage(
        router: Router, sep: Optional[str] = None
    ) -> Dict[str, List[str]]:
<<<<<<< HEAD
=======
        """Get command coverage."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        api_router = router.api_router

        mapping = ProviderInterface().map

        coverage_map: Dict[Any, Any] = {}
        for route in api_router.routes:
            openapi_extra = getattr(route, "openapi_extra")
            if openapi_extra:
                model = openapi_extra.get("model", None)
                if model:
                    providers = list(mapping[model].keys())
                    if "openbb" in providers:
                        providers.remove("openbb")

                    if hasattr(route, "path"):
                        rp = (
                            route.path if sep is None else route.path.replace("/", sep)  # type: ignore
                        )
                        if route.path not in coverage_map:  # type: ignore
                            coverage_map[rp] = []
                        coverage_map[rp] = providers
        return coverage_map

    @staticmethod
<<<<<<< HEAD
    def get_commands_model(
        router: Router, sep: Optional[str] = None
    ) -> Dict[str, List[str]]:
=======
    def get_commands_model(router: Router, sep: Optional[str] = None) -> Dict[str, str]:
        """Get commands model."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        api_router = router.api_router

        coverage_map: Dict[Any, Any] = {}
        for route in api_router.routes:
            openapi_extra = getattr(route, "openapi_extra")
            if openapi_extra:
                model = openapi_extra.get("model", None)
                if model and hasattr(route, "path"):
                    rp = (
                        route.path if sep is None else route.path.replace("/", sep)  # type: ignore
                    )
                    if route.path not in coverage_map:  # type: ignore
                        coverage_map[rp] = []
                    coverage_map[rp] = model
        return coverage_map

    def get_command(self, route: str) -> Optional[Callable]:
<<<<<<< HEAD
=======
        """Get command from route."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return self._map.get(route, None)


class LoadingError(Exception):
    """Error loading extension."""


class RouterLoader:
<<<<<<< HEAD
    @staticmethod
    @lru_cache
    def from_extensions() -> Router:
        router = Router()

        for entry_point in sorted(entry_points(group="openbb_core_extension")):
            try:
                entry = entry_point.load()
                if isinstance(entry, Router):
                    router.include_router(router=entry, prefix=f"/{entry_point.name}")
            except Exception as e:
                msg = f"Error loading extension: {entry_point.name}\n"
=======
    """Router Loader."""

    @staticmethod
    @lru_cache
    def from_extensions() -> Router:
        """Load routes from extensions."""
        router = Router()

        for name, entry in ExtensionLoader().core_objects.items():
            try:
                router.include_router(router=entry, prefix=f"/{name}")
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

        return router
