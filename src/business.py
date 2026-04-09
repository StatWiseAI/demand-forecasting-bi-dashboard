def estimate_working_capital_release(baseline_error: float, improved_error: float) -> float:
    return max(baseline_error - improved_error, 0.0)
