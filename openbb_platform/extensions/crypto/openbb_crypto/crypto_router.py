"""Crypto Router."""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

from openbb_crypto.price.price_router import router as price_router

router = Router(prefix="")
router.include_router(price_router)


<<<<<<< HEAD
=======
# pylint: disable=unused-argument
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
@router.command(model="CryptoSearch")
async def search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Cryptocurrency Search. Search available cryptocurrency pairs."""
    return await OBBject.from_query(Query(**locals()))
