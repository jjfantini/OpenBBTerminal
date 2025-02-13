"""Shorts Router."""
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

router = Router(prefix="/shorts")

# pylint: disable=unused-argument


@router.command(model="EquityFTD")
async def fails_to_deliver(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Get reported Fail-to-deliver (FTD) data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="ShortVolume")
async def short_volume(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Get reported Fail-to-deliver (FTD) data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="EquityShortInterest")
async def short_interest(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Get reported Short Volume and Days to Cover data."""
    return await OBBject.from_query(Query(**locals()))
