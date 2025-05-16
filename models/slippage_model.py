def calculate_slippage(orderbook_data, quantity):
    # Assuming market buy order (so you take from asks)
    asks = orderbook_data['asks']  # list of [price, volume]

    total_qty = 0
    total_cost = 0

    # Iterate over asks until order quantity fulfilled
    for price_str, volume_str in asks:
        price = float(price_str)
        volume = float(volume_str)

        qty_to_take = min(volume, quantity - total_qty)
        total_cost += price * qty_to_take
        total_qty += qty_to_take

        if total_qty >= quantity:
            break

    if total_qty < quantity:
        # Not enough liquidity, handle this case
        executed_price = total_cost / total_qty if total_qty > 0 else 0
    else:
        executed_price = total_cost / quantity

    # Expected price = mid price
    best_ask = float(asks[0][0])
    best_bid = float(orderbook_data['bids'][0][0])
    expected_price = (best_ask + best_bid) / 2

    slippage = ((executed_price - expected_price) / expected_price) * 100
    return slippage
