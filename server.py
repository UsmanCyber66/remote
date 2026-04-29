import asyncio
import websockets
async def serveron():
    async def handle_connection(websocket):
        print("A client connected!")
        try:
            # This loop keeps the connection open to listen for multiple messages
            async for message in websocket:
                message = message.strip().strip("|")
                
                # Optional: Send a response back to the client
                await websocket.send(f"Echo: {message}")
                
        except websockets.exceptions.ConnectionClosedOK:
            print("Client disconnected gracefully.")
        except Exception as e:
            print(f"Error: {e}")

    async def main():
        # Start the server on localhost, port 8765
        async with websockets.serve(handle_connection, "localhost", 8765):
            print("WebSocket Server started on ws://localhost:8765")
            await asyncio.Future()  # This keeps the server running forever

    await main()

if __name__ == "__main__":
    asyncio.run(serveron())