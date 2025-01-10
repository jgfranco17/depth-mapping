from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class MidasConstants:
    # Hub model repository
    HUB_MODEL_REPO: Final[str] = "intel-isl/MiDaS"

    # Model sizes
    MODEL_SMALL: Final[str] = "MiDaS_small"
    MODEL_MEDIUM: Final[str] = "DPT_Hybrid"
    MODEL_LARGE: Final[str] = "DPT_Large"
