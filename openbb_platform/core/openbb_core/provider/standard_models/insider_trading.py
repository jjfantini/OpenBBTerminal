"""Insider Trading Standard Model."""

<<<<<<< HEAD
from datetime import date, datetime, time
=======
from datetime import (
    date as dateType,
    datetime,
    time,
)
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from typing import List, Optional, Set, Union

from dateutil import parser
from pydantic import Field, StrictInt, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class InsiderTradingQueryParams(QueryParams):
    """Insider Trading Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: StrictInt = Field(
        default=500,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class InsiderTradingData(Data):
    """Insider Trading Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
<<<<<<< HEAD
    company_cik: int = Field(description="Company CIK of the insider trading.")
    filing_date: datetime = Field(description="Filing date of the insider trading.")
    transaction_date: Optional[date] = Field(
        default=None, description="Transaction date of the insider trading."
    )
    owner_cik: int = Field(description="Reporting CIK of the insider trading.")
    owner_name: str = Field(description="Reporting name of the insider trading.")
    owner_title: Optional[str] = Field(
        default=None, description="Designation of owner of the insider trading."
    )
    transaction_type: str = Field(
        description="Transaction type of the insider trading."
    )
    acquisition_or_disposition: Optional[str] = Field(
        default=None,
        description="Acquisition or disposition of the insider trading.",
    )
    security_type: str = Field(description="Security type of the insider trading.")
    securities_owned: Optional[float] = Field(
        default=None, description="Number of securities owned in the insider trading."
    )
    securities_transacted: Optional[float] = Field(
        default=None, description="Securities transacted of the insider trading."
    )
    transaction_price: Optional[float] = Field(
        default=None,
        description="Price of the insider trading.",
    )
    filing_url: str = Field(description="Link of the insider trading.")

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])

    @field_validator("filing_date", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        filing_date = parser.isoparse(str(v))

        if filing_date.time() == time(0, 0):
            return datetime.combine(filing_date.date(), time(0, 0, 0))
        return filing_date
=======
    company_cik: Optional[Union[int, str]] = Field(
        default=None, description="CIK number of the company."
    )
    filing_date: Optional[Union[dateType, datetime]] = Field(
        default=None, description="Filing date of the trade."
    )
    transaction_date: Optional[dateType] = Field(
        default=None, description="Date of the transaction."
    )
    owner_cik: Optional[Union[int, str]] = Field(
        default=None, description="Reporting individual's CIK."
    )
    owner_name: Optional[str] = Field(
        default=None, description="Name of the reporting individual."
    )
    owner_title: Optional[str] = Field(
        default=None, description="The title held by the reporting individual."
    )
    transaction_type: Optional[str] = Field(
        default=None, description="Type of transaction being reported."
    )
    acquisition_or_disposition: Optional[str] = Field(
        default=None, description="Acquisition or disposition of the shares."
    )
    security_type: Optional[str] = Field(
        default=None, description="The type of security transacted."
    )
    securities_owned: Optional[float] = Field(
        default=None,
        description="Number of securities owned by the reporting individual.",
    )
    securities_transacted: Optional[float] = Field(
        default=None,
        description="Number of securities transacted by the reporting individual.",
    )
    transaction_price: Optional[float] = Field(
        default=None, description="The price of the transaction."
    )
    filing_url: Optional[str] = Field(default=None, description="Link to the filing.")

    @field_validator(
        "filing_date", "transaction_date", mode="before", check_fields=False
    )
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        if v:
            filing_date = parser.isoparse(str(v))
            if filing_date.time() == time(0, 0):
                return filing_date.date()
            return filing_date
        return None
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
