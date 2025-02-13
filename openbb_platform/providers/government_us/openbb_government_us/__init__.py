"""Government US provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_government_us.models.treasury_auctions import (
    GovernmentUSTreasuryAuctionsFetcher,
)
<<<<<<< HEAD
=======
from openbb_government_us.models.treasury_prices import (
    GovernmentUSTreasuryPricesFetcher,
)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

government_us_provider = Provider(
    name="government_us",
    website="https://data.gov/",
    description=(
        "Data.gov is the United States government's open data website."
        + " It provides access to datasets published by agencies across the federal government. "
        + "Data.gov is intended to provide access to government open data to the public, "
        + "achieve agency missions, drive innovation, fuel economic activity, "
        + "and uphold the ideals of an open and transparent government."
    ),
    fetcher_dict={
        "TreasuryAuctions": GovernmentUSTreasuryAuctionsFetcher,
<<<<<<< HEAD
=======
        "TreasuryPrices": GovernmentUSTreasuryPricesFetcher,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    },
)
