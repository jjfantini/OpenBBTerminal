### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class ROUTER_regulators(Container):
    """/regulators
    /sec
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
<<<<<<< HEAD
    def sec(self):  # route = "/regulators/sec"
=======
    def sec(self):
        # pylint: disable=import-outside-toplevel
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        from . import regulators_sec

        return regulators_sec.ROUTER_regulators_sec(command_runner=self._command_runner)
