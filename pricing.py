"""Pricing rules for the Git collaboration exercise."""


DISCOUNT_RATES = {"standard": 0.05, "premium": 0.10}


def get_discount_rate(customer_level: str) -> float:
    """Return the configured discount rate for a customer level."""
    return DISCOUNT_RATES[customer_level]

