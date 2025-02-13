<<<<<<< HEAD
=======
"""Preferences for the OpenBB platform."""

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class Preferences(BaseModel):
<<<<<<< HEAD
=======
    """Preferences for the OpenBB platform."""

>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
    data_directory: str = str(Path.home() / "OpenBBUserData")
    export_directory: str = str(Path.home() / "OpenBBUserData" / "exports")
    user_styles_directory: str = str(Path.home() / "OpenBBUserData" / "styles" / "user")
    cache_directory: str = str(Path.home() / "OpenBBUserData" / "cache")
    charting_extension: Literal["openbb_charting"] = "openbb_charting"
    chart_style: Literal["dark", "light"] = "dark"
    plot_enable_pywry: bool = True
    plot_pywry_width: PositiveInt = 1400
    plot_pywry_height: PositiveInt = 762
    plot_open_export: bool = (
        False  # Whether to open plot image exports after they are created
    )
    table_style: Literal["dark", "light"] = "dark"
    request_timeout: PositiveInt = 15
    metadata: bool = True
<<<<<<< HEAD
    output_type: Literal[
        "OBBject", "dataframe", "polars", "numpy", "dict", "chart"
    ] = Field(default="OBBject", description="Python default output type.")
=======
    field_order: bool = (
        False  # Whether to display the field order by which the data was defined
    )
    output_type: Literal["OBBject", "dataframe", "polars", "numpy", "dict", "chart"] = (
        Field(default="OBBject", description="Python default output type.")
    )
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe

    model_config = ConfigDict(validate_assignment=True)

    def __repr__(self) -> str:
<<<<<<< HEAD
=======
        """Return a string representation of the model."""
>>>>>>> 7a07970fc8bd4b03ea459cb0d892005ff5130ffe
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )
