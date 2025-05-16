import streamlit as st
import asyncio
import time  # <-- add time module here

from datafeed.orderbook_ws import OrderBookClient
from models.slippage_model import calculate_slippage
from models.fee_model import calculate_fees
from models.impact_model import estimate_market_impact
from models.maker_taker_model import predict_maker_taker
# from utils.latency import measure_latency  # no longer needed

st.set_page_config(page_title="📊 Trading Cost Simulator", layout="wide")

# Page Title with emoji
st.markdown("<h1 style='text-align:center; color:#4B8BBE;'>📊 Trading Cost Simulator</h1>", unsafe_allow_html=True)

# Sidebar Inputs
with st.sidebar:
    st.header("⚙️ Simulation Inputs")
    exchange = st.selectbox("Select Exchange", ["OKX", "Binance", "Coinbase", "Bybit"])
    default_assets = [
        "BTC-USDT", "ETH-USDT", "SOL-USDT",
        "XRP-USDT", "DOGE-USDT", "BTC-USDT-SWAP", "ETH-USDT-SWAP"
    ]
    selected_asset = st.selectbox("Spot Asset", default_assets + ["Custom"])
    asset = st.text_input("Enter Custom Asset", value="BTC-USDT-SWAP") if selected_asset == "Custom" else selected_asset
    st.markdown("---")
    order_type = st.selectbox("Order Type", ["Market", "Limit", "Stop-Loss", "Post-Only"])
    quantity = st.number_input("Quantity (USD)", min_value=1.0, value=100.0, step=1.0)
    volatility = st.slider("Volatility", 0.1, 10.0, step=0.1, value=1.0)
    fee_tier = st.selectbox("Fee Tier", ["Tier 1", "Tier 2", "Tier 3"])
    st.markdown("---")
    run_sim = st.button("▶️ Start Simulation")

output_placeholder = st.container()

# async def simulate_once():
#     ob_client = OrderBookClient(asset)
#     await ob_client.connect()
    
#     # Measure latency locally by timing the orderbook data fetch
#     start_time = time.perf_counter()
#     data = await ob_client.get_orderbook()
#     end_time = time.perf_counter()
#     latency = (end_time - start_time) * 1000  # milliseconds

#     if data:
#         slippage = calculate_slippage(data, quantity)
#         fees = calculate_fees(fee_tier, quantity)
#         market_impact = estimate_market_impact(quantity, volatility)
#         net_cost = slippage + fees + market_impact
#         maker_taker_ratio = predict_maker_taker(data)

#         with output_placeholder:
#             st.markdown("## 📈 Simulation Results")
#             col1, col2, col3 = st.columns(3)
#             col1.metric("Expected Slippage", f"${slippage:.2f}")
#             col2.metric("Expected Fees", f"${fees:.2f}")
#             col3.metric("Market Impact", f"${market_impact:.2f}")

#             col4, col5, col6 = st.columns(3)
#             col4.metric("Net Cost", f"${net_cost:.2f}")
#             col5.metric("Maker/Taker Ratio", f"{maker_taker_ratio:.2f}")
#             col6.metric("Internal Latency", f"{latency:.2f} ms")

#             st.markdown("---")
#             st.markdown(f"""
#             **Details:**
#             - **Exchange:** {exchange}  
#             - **Spot Asset:** {asset}  
#             - **Order Type:** {order_type}  
#             - **Quantity (USD):** ${quantity:.2f}
#             """)
#     else:
#         st.error("❌ Failed to retrieve orderbook data. Please try again.")

# if run_sim:
#     asyncio.run(simulate_once())
async def simulate_once():
    ob_client = OrderBookClient(asset)
    await ob_client.connect()

    start_time = time.perf_counter()
    data = await ob_client.get_orderbook()
    end_time = time.perf_counter()
    latency = (end_time - start_time) * 1000  # milliseconds

    await ob_client.close()

    if not data:
        st.error("❌ Failed to retrieve orderbook data. Please try again.")
        return

    slippage = calculate_slippage(data, quantity)
    fees = calculate_fees(fee_tier, quantity)
    market_impact = estimate_market_impact(quantity, volatility)
    net_cost = slippage + fees + market_impact
    maker_taker_ratio = predict_maker_taker(data)

    with output_placeholder:
        st.markdown("## 📈 Simulation Results")
        col1, col2, col3 = st.columns(3)
        col1.metric("Expected Slippage", f"${slippage:.2f}")
        col2.metric("Expected Fees", f"${fees:.2f}")
        col3.metric("Market Impact", f"${market_impact:.2f}")

        col4, col5, col6 = st.columns(3)
        col4.metric("Net Cost", f"${net_cost:.2f}")
        col5.metric("Maker/Taker Ratio", f"{maker_taker_ratio:.2f}")
        col6.metric("Latency", f"{latency:.2f} ms")

        st.markdown("---")
        st.markdown(f"""
        **Details:**
        - **Exchange:** {exchange}  
        - **Spot Asset:** {asset}  
        - **Order Type:** {order_type}  
        - **Quantity (USD):** ${quantity:.2f}
        """)
if run_sim:
    print("🔄 Starting simulation...")
    asyncio.run(simulate_once())
