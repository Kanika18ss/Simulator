import math

def estimate_market_impact(quantity_usd, volatility, market_depth_usd=1000000):
    """
    Estimate market impact using a simplified Almgren-Chriss model.
    
    Parameters:
        quantity_usd (float): Order value in USD.
        volatility (float): Estimated market volatility (user input).
        market_depth_usd (float): Estimated market liquidity. Higher = more liquid.
    
    Returns:
        float: Estimated market impact in USD.
    """
    gamma = 0.0001  # permanent impact parameter
    eta = 0.01      # temporary impact parameter

    # Normalize quantity as a fraction of market depth
    q_frac = quantity_usd / market_depth_usd

    # Almgren-Chriss impact = gamma * q + eta * volatility * sqrt(q)
    impact = (gamma * quantity_usd) + (eta * volatility * math.sqrt(q_frac * market_depth_usd))

    return impact
