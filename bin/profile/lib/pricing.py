"""Cost calculation from token usage and per-model MTok pricing.

Pricing itself lives in models.yaml (price_in / price_out, USD per 1M
tokens) so it can be corrected without touching code. A model with no
pricing fields (all local Ollama entries) is treated as free.
"""

from __future__ import annotations


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    price_in: float | None,
    price_out: float | None,
) -> float:
    if price_in is None or price_out is None:
        return 0.0
    return (input_tokens / 1_000_000) * price_in + (output_tokens / 1_000_000) * price_out


def format_usd(amount: float, free: bool = False) -> str:
    if free:
        return "$0.00 (local)"
    if amount < 0.01:
        return f"${amount:.4f}"
    return f"${amount:.2f}"
