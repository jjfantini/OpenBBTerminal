### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /crypto
    /currency
    /derivatives
    /economy
    /equity
    /etf
    /fixedincome
    /index
    /news
    /regulators

Extensions:
<<<<<<< HEAD
    - crypto@1.0.0
    - currency@1.0.0
    - derivatives@1.0.0
    - economy@1.0.0
    - equity@1.0.0
    - etf@1.0.0
    - fixedincome@1.0.0
    - index@1.0.0
    - news@1.0.0
    - regulators@1.0.0

    - benzinga@1.0.0
    - fmp@1.0.0
    - fred@1.0.0
    - intrinio@1.0.0
    - oecd@1.0.0
    - polygon@1.0.0
    - sec@1.0.0
    - tiingo@1.0.0
    - tradingeconomics@1.0.0    """
    # fmt: on
=======
    - crypto@1.1.1
    - currency@1.1.1
    - derivatives@1.1.1
    - economy@1.1.1
    - equity@1.1.1
    - etf@1.1.1
    - fixedincome@1.1.1
    - index@1.1.1
    - news@1.1.1
    - regulators@1.1.1

    - benzinga@1.1.1
    - federal_reserve@1.1.1
    - fmp@1.1.1
    - fred@1.1.1
    - intrinio@1.1.1
    - oecd@1.1.1
    - polygon@1.1.1
    - sec@1.1.1
    - tiingo@1.1.1
    - tradingeconomics@1.1.1
    - yfinance@1.1.1    """
    # fmt: on

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
<<<<<<< HEAD
    def crypto(self):  # route = "/crypto"
=======
    def crypto(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import crypto

        return crypto.ROUTER_crypto(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def currency(self):  # route = "/currency"
=======
    def currency(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import currency

        return currency.ROUTER_currency(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def derivatives(self):  # route = "/derivatives"
=======
    def derivatives(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import derivatives

        return derivatives.ROUTER_derivatives(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def economy(self):  # route = "/economy"
=======
    def economy(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import economy

        return economy.ROUTER_economy(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def equity(self):  # route = "/equity"
=======
    def equity(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import equity

        return equity.ROUTER_equity(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def etf(self):  # route = "/etf"
=======
    def etf(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import etf

        return etf.ROUTER_etf(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def fixedincome(self):  # route = "/fixedincome"
=======
    def fixedincome(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import fixedincome

        return fixedincome.ROUTER_fixedincome(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def index(self):  # route = "/index"
=======
    def index(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import index

        return index.ROUTER_index(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def news(self):  # route = "/news"
=======
    def news(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import news

        return news.ROUTER_news(command_runner=self._command_runner)

    @property
<<<<<<< HEAD
    def regulators(self):  # route = "/regulators"
=======
    def regulators(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import regulators

        return regulators.ROUTER_regulators(command_runner=self._command_runner)
