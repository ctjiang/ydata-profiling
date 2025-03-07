from typing import Any

from ydata_profiling.report.presentation.core.item_renderer import ItemRenderer


class FrequencyTable(ItemRenderer):
    def __init__(self, rows: list, redact: bool, **kwargs):
        super().__init__(
            "frequency_table",
            {
                "rows": rows,
                "redact": redact,
                "th_value": _("Value"),
                "th_count": _("Count"),
                "th_frequency": _("Frequency (%)"),
            },
            **kwargs
        )

    def __repr__(self) -> str:
        return "FrequencyTable"

    def render(self) -> Any:
        raise NotImplementedError()
