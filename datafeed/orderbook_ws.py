# import websockets
# import asyncio
# import json
# from collections import deque
# from datetime import datetime

# class OrderBookClient:
#     def __init__(self, symbol="BTC-USDT-SWAP"):
#         self.url = f"wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/{symbol}"
#         self.orderbook_queue = deque()

#     async def connect(self):
#         self.connection = await websockets.connect(self.url)
#         print("WebSocket connected.")

#     async def get_orderbook(self):
#         try:
#             msg = await self.connection.recv()
#             data = json.loads(msg)
#             data["received_at"] = datetime.utcnow().isoformat()
#             return data
#         except Exception as e:
#             print("Error receiving orderbook data:", e)
#             return None


import asyncio
import websockets
import json
from datetime import datetime

class OrderBookClient:
    def __init__(self, symbol="BTC-USDT-SWAP"):
        self.url = f"wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/{symbol}"
        self.latest_data = None
        self.ws = None

    async def connect(self):
        try:
            self.ws = await websockets.connect(self.url)
            print("✅ WebSocket connected.")
        except Exception as e:
            print("❌ Failed to connect:", e)

    async def get_orderbook(self, timeout=5):
        try:
            start_time = datetime.utcnow()
            while True:
                msg = await asyncio.wait_for(self.ws.recv(), timeout=timeout)
                data = json.loads(msg)
                data["received_at"] = datetime.utcnow().isoformat()
                return data
        except Exception as e:
            print("❌ Error getting orderbook:", e)
            return None

    async def close(self):
        if self.ws:
            await self.ws.close()
