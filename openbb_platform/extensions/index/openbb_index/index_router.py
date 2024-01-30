"""Index Router."""
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

<<<<<<< HEAD
router = Router(prefix="")
=======
from openbb_index.price.price_router import router as price_router

router = Router(prefix="")
router.include_router(price_router)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

# pylint: disable=unused-argument


<<<<<<< HEAD
@router.command(model="MarketIndices")
=======
@router.command(
    model="MarketIndices",
    deprecated=True,
    deprecation_message="This endpoint will be deprecated in the future releases. Use '/index/price/historical' instead.",
)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
async def market(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Historical Market Indices."""
    return await OBBject.from_query(Query(**locals()))


<<<<<<< HEAD
@router.command(model="EuropeanIndices")
async def european(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Historical European Indices."""
    return await OBBject.from_query(Query(**locals()))


=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
@router.command(model="IndexConstituents")
async def constituents(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Index Constituents. Constituents of an index."""
    return await OBBject.from_query(Query(**locals()))


<<<<<<< HEAD
@router.command(model="EuropeanIndexConstituents")
async def european_constituents(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """European Index Constituents. Constituents of select european indices."""
    return await OBBject.from_query(Query(**locals()))


=======
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
@router.command(model="IndexSnapshots")
async def snapshots(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Index Snapshots. Current levels for all indices from a provider."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="AvailableIndices")
async def available(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Available Indices. Available indices for a given provider."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="IndexSearch")
async def search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Index Search. Search for indices."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="SP500Multiples")
async def sp500_multiples(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """S&P 500 Multiples. Historical S&P 500 multiples and Shiller PE ratios."""
    return await OBBject.from_query(Query(**locals()))
