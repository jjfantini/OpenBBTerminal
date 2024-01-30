"""Seeking Alpha Provider module."""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.provider import Provider
from openbb_seeking_alpha.models.upcoming_release_days import (
    SAUpcomingReleaseDaysFetcher,
)

seeking_alpha_provider = Provider(
    name="seeking_alpha",
    website="https://seekingalpha.com",
    description="""Seeking Alpha is a data provider with access to news, analysis, and
    real-time alerts on stocks.""",
    fetcher_dict={
        "UpcomingReleaseDays": SAUpcomingReleaseDaysFetcher,
    },
)
