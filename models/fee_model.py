def calculate_fees(fee_tier, quantity_usd):
    """
    Calculate trading fees based on the selected fee tier.
    Fee values are estimated from OKX's public fee tiers.
    """
    fee_tiers = {
        "Tier 1": 0.0010,  # 0.10%
        "Tier 2": 0.0008,  # 0.08%
        "Tier 3": 0.0005   # 0.05%
    }

    fee_rate = fee_tiers.get(fee_tier, 0.0010)  # Default to Tier 1
    return quantity_usd * fee_rate
