<<<<<<< HEAD
"""CBOE provider module."""


from openbb_cboe.models.available_indices import CboeAvailableIndicesFetcher
from openbb_cboe.models.equity_historical import CboeEquityHistoricalFetcher
from openbb_cboe.models.equity_info import CboeEquityInfoFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.european_index_constituents import (
    CboeEuropeanIndexConstituentsFetcher,
)
from openbb_cboe.models.european_indices import (
    CboeEuropeanIndicesFetcher,
)
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
from openbb_cboe.models.market_indices import (
    CboeMarketIndicesFetcher,
)
=======
"""Cboe provider module."""

from openbb_cboe.models.available_indices import CboeAvailableIndicesFetcher
from openbb_cboe.models.equity_historical import CboeEquityHistoricalFetcher
from openbb_cboe.models.equity_quote import CboeEquityQuoteFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_constituents import (
    CboeIndexConstituentsFetcher,
)
from openbb_cboe.models.index_historical import (
    CboeIndexHistoricalFetcher,
)
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from openbb_cboe.models.options_chains import CboeOptionsChainsFetcher
from openbb_core.provider.abstract.provider import Provider

cboe_provider = Provider(
    name="cboe",
    website="https://www.cboe.com/",
    description="""Cboe is the world's go-to derivatives and exchange network,
    delivering cutting-edge trading, clearing and investment solutions to people
    around the world.""",
    credentials=None,
    fetcher_dict={
<<<<<<< HEAD
        "EquitySearch": CboeEquitySearchFetcher,
        "OptionsChains": CboeOptionsChainsFetcher,
        "EquityHistorical": CboeEquityHistoricalFetcher,
        "EquityInfo": CboeEquityInfoFetcher,
        "FuturesCurve": CboeFuturesCurveFetcher,
        "AvailableIndices": CboeAvailableIndicesFetcher,
        "EuropeanIndexConstituents": CboeEuropeanIndexConstituentsFetcher,
        "EuropeanIndices": CboeEuropeanIndicesFetcher,
        "MarketIndices": CboeMarketIndicesFetcher,
        "IndexSearch": CboeIndexSearchFetcher,
        "IndexSnapshots": CboeIndexSnapshotsFetcher,
=======
        "AvailableIndices": CboeAvailableIndicesFetcher,
        "EquityHistorical": CboeEquityHistoricalFetcher,
        "EquityQuote": CboeEquityQuoteFetcher,
        "EquitySearch": CboeEquitySearchFetcher,
        "IndexConstituents": CboeIndexConstituentsFetcher,
        "FuturesCurve": CboeFuturesCurveFetcher,
        "IndexHistorical": CboeIndexHistoricalFetcher,
        "IndexSearch": CboeIndexSearchFetcher,
        "IndexSnapshots": CboeIndexSnapshotsFetcher,
        "MarketIndices": CboeIndexHistoricalFetcher,
        "OptionsChains": CboeOptionsChainsFetcher,
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    },
)
