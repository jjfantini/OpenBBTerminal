"""FMP ETF Holdings Performance Model."""

from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher

from .etf_holdings import FMPEtfHoldingsFetcher
from .etf_holdings_date import FMPEtfHoldingsDateFetcher
from .price_performance import (
    FMPPricePerformanceData,
    FMPPricePerformanceFetcher,
    FMPPricePerformanceQueryParams,
)


class FMPEtfHoldingsPerformanceQueryParams(FMPPricePerformanceQueryParams):
    """FMP ETF Holdings Performance Query."""


class FMPEtfHoldingsPerformanceData(FMPPricePerformanceData):
    """FMP ETF Holdings Performance Data."""


class FMPEtfHoldingsPerformanceFetcher(
    Fetcher[
        FMPEtfHoldingsPerformanceQueryParams,
        List[FMPEtfHoldingsPerformanceData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPEtfHoldingsPerformanceQueryParams:
        """Transform the query."""
        return FMPEtfHoldingsPerformanceQueryParams(**params)

    @staticmethod
<<<<<<< HEAD
    def extract_data(
=======
    async def aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        query: FMPEtfHoldingsPerformanceQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        # Get latest available holdings filing date
<<<<<<< HEAD
        dates = FMPEtfHoldingsDateFetcher().extract_data(
=======
        dates = await FMPEtfHoldingsDateFetcher().aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            FMPEtfHoldingsDateFetcher.transform_query(query.model_dump()),
            credentials,
            **kwargs,
        )
        if dates is None:
            return []
        # Get holdings for that date
<<<<<<< HEAD
        holdings = FMPEtfHoldingsFetcher().extract_data(
=======
        holdings = await FMPEtfHoldingsFetcher().aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
            FMPEtfHoldingsFetcher.transform_query(
                {"symbol": query.symbol, "date": max([d["date"] for d in dates])}
            ),
            credentials,
            **kwargs,
        )
        if holdings is None:
            return []
        holdings_list = [
            holding["symbol"] for holding in holdings if holding["symbol"] is not None
        ]
        # Split into chunks of 500
        chunks = [holdings_list[i : i + 500] for i in range(0, len(holdings_list), 500)]
        # Get price performance for the holdings
        holdings_performance: list = []
        for holding_chunk in chunks:
            holdings_str = (
                ",".join(holding_chunk) if len(holding_chunk) > 1 else holding_chunk[0]
            )
<<<<<<< HEAD
            _performance = FMPPricePerformanceFetcher().extract_data(
=======
            _performance = await FMPPricePerformanceFetcher().aextract_data(
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
                FMPPricePerformanceFetcher.transform_query({"symbol": holdings_str}),
                credentials,
                **kwargs,
            )
            holdings_performance.extend(_performance)
        return holdings_performance

    @staticmethod
    def transform_data(
        query: FMPEtfHoldingsPerformanceQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[FMPEtfHoldingsPerformanceData]:
        """Return the transformed data."""
        return [FMPEtfHoldingsPerformanceData.model_validate(d) for d in data]
