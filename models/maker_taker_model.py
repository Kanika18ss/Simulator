import random
import math

def predict_maker_taker(orderbook_data):
    """
    Predict the proportion of maker vs taker orders using a simple logistic model.
    
    Parameters:
        orderbook_data (dict): Latest L2 orderbook tick.
    
    Returns:
        float: Maker/Taker ratio (0.0 to 1.0 where closer to 1 = more maker-like).
    """
    try:
        best_bid = float(orderbook_data["bids"][0][0])
        best_ask = float(orderbook_data["asks"][0][0])
    except (IndexError, KeyError, TypeError):
        return 0.5  # default balanced ratio

    # Spread indicates market tightness
    spread = best_ask - best_bid
    mid_price = (best_ask + best_bid) / 2

    # Normalize spread relative to mid price
    spread_pct = spread / mid_price

    # Logistic model: higher spread => more taker orders
    x = 10 * (0.002 - spread_pct)  # 0.2% spread is midpoint
    ratio = 1 / (1 + math.exp(-x))

    # Add randomness for simulation realism
    noise = random.uniform(-0.05, 0.05)
    ratio = min(max(ratio + noise, 0), 1)

    return ratio
