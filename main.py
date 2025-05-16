import json
from models.slippage_model import calculate_slippage

# Load orderbook data
with open("orderbook_data.json", "r") as f:
    orderbook = json.load(f)

# Assume we're placing a market buy order
# So, expected price is the best ask
asks = orderbook.get("asks", [])
if not asks:
    print("No ask data available in orderbook.")
    exit()

# Sort asks by price to get the best (lowest) ask
best_ask = sorted(asks, key=lambda x: x[0])[0]  # [price, quantity]
expected_price = float(best_ask[0])

# Simulate that the trade was executed at a worse price (e.g., due to slippage)
# You can adjust this value to simulate different scenarios
executed_price = expected_price + 0.5  # simulate 0.5 increase due to slippage

# Calculate slippage
slippage = calculate_slippage(expected_price, executed_price)

# Print and log the result
print(f"Expected Price: {expected_price}, Executed Price: {executed_price}, Slippage: {slippage:.2f}%")

# Log to file
with open("outputs/simulation_log.txt", "a") as f:
    f.write(f"Expected Price: {expected_price}, Executed Price: {executed_price}, Slippage: {slippage:.2f}%\n")
