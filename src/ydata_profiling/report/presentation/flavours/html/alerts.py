from ydata_profiling.report.presentation.core.alerts import Alerts
from ydata_profiling.report.presentation.flavours.html import templates


class HTMLAlerts(Alerts):
    def render(self) -> str:
        styles = {
            "constant": "warning",
            "unsupported": "warning",
            "type_date": "warning",
            "constant_length": "primary",
            "high_cardinality": "primary",
            "imbalance": "primary",
            "unique": "primary",
            "uniform": "primary",
            "infinite": "info",
            "zeros": "info",
            "truncated": "info",
            "missing": "info",
            "skewed": "info",
            "high_correlation": "default",
            "duplicates": "default",
            "non_stationary": "default",
            "seasonal": "default",
        }

        alter_desc = {
            "constant_length": _("has constant length"),
            "constant": _("has constant value"),
            "duplicates": [_("Dataset has"), _("duplicate rows")],
            "empty": _("Dataset is empty"),
            "high_cardinality": [_("has a high cardinality"), _("distinct values")],
            "high_correlation": [
                _("is highly"),
                _("correlated with"),
                _("and"),
                _("other fields"),
            ],
            "imbalance": _("is highly imbalanced"),
            "infinite": [_("has"), _("infinite values")],
            "missing": [_("has"), _("missing values")],
            "non_stationary": _("is non stationary"),
            "seasonal": _("is seasonal"),
            "skewed": _("is highly skewed"),
            "truncated": [_("has"), _("truncated files")],
            "type_date": _(
                "only contains datetime values, but is categorical. Consider applying"
            ),
            "uniform": _("is uniformly distributed"),
            "unique": _("has unique values"),
            "unsupported": _(
                "is an unsupported type, check if it needs cleaning or further analysis"
            ),
            "zeros": [_("has"), _("zeros")],
        }

        return templates.template("alerts.html").render(
            **self.content, styles=styles, alter_desc=alter_desc
        )
