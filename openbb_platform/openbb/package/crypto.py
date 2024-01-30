### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

<<<<<<< HEAD
from typing import List, Literal, Optional
=======
from typing import Literal, Optional
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
<<<<<<< HEAD
from openbb_core.app.static.decorators import validate
from openbb_core.app.static.filters import filter_inputs
from openbb_core.provider.abstract.data import Data
=======
from openbb_core.app.static.utils.decorators import validate
from openbb_core.app.static.utils.filters import filter_inputs
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from typing_extensions import Annotated


class ROUTER_crypto(Container):
    """/crypto
    /price
    search
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
<<<<<<< HEAD
    def price(self):  # route = "/crypto/price"
=======
    def price(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import crypto_price

        return crypto_price.ROUTER_crypto_price(command_runner=self._command_runner)

    @validate
    def search(
        self,
        query: Annotated[
            Optional[str], OpenBBCustomParameter(description="Search query.")
<<<<<<< HEAD
        ] = "",
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List[Data]]:
=======
        ] = None,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject:
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        """Cryptocurrency Search. Search available cryptocurrency pairs.

        Parameters
        ----------
        query : Optional[str]
            Search query.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[CryptoSearch]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        CryptoSearch
        ------------
        symbol : str
            Symbol representing the entity requested in the data. (Crypto)
        name : Optional[str]
            Name of the crypto.
        currency : Optional[str]
            The currency the crypto trades for. (provider: fmp)
        exchange : Optional[str]
            The exchange code the crypto trades on. (provider: fmp)
        exchange_name : Optional[str]
            The short name of the exchange the crypto trades on. (provider: fmp)

        Example
        -------
        >>> from openbb import obb
        >>> obb.crypto.search()
        """  # noqa: E501

<<<<<<< HEAD
        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "query": query,
            },
            extra_params=kwargs,
        )

        return self._run(
            "/crypto/search",
            **inputs,
=======
        return self._run(
            "/crypto/search",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "query": query,
                },
                extra_params=kwargs,
            )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        )
