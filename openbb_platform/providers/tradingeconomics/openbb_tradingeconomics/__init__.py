"""Trading Economics provider module."""
<<<<<<< HEAD
=======

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_core.provider.abstract.provider import Provider
from openbb_tradingeconomics.models.economic_calendar import TEEconomicCalendarFetcher

tradingeconomics_provider = Provider(
    name="tradingeconomics",
    website="https://tradingeconomics.com/",
    description="""Trading Economics""",
    credentials=["api_key"],
    fetcher_dict={"EconomicCalendar": TEEconomicCalendarFetcher},
)
