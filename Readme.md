# 📊 Trading Cost Simulator

A real-time trading cost simulator that retrieves live order book data over WebSocket, simulates trade slippage, calculates exchange fees, and estimates market impact. Built using **Streamlit**, **Asyncio**, and **WebSockets**.

---

## 🚀 Features

- 📡 Live order book streaming via WebSockets (OKX, Binance, Bybit, etc.)
- 📈 Real-time latency measurement (ms)
- 💸 Trading cost breakdown: Slippage, Fees, Market Impact
- ⚙️ Custom inputs: Asset, Order Type, Quantity, Volatility, Fee Tier
- 📊 Maker/Taker ratio estimation
- 🔁 Async architecture with minimal latency

---

## 🧱 Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Backend:** Python (`asyncio`, `websockets`, `time`)
- **Models:** Custom modules for slippage, fees, impact, and maker-taker prediction

---


