import asyncio
import os
import websockets
from websockets.exceptions import ConnectionClosed
from smotfuncs import encrypt, sha, baseify, attr, serverlogin, forever

async def handle_connection(websocket):
    print("Client connected.")
    try:
        # FIX 1: You MUST await this to get the actual string "login"
        login_signal = await websocket.recv() 
        
        # FIX 2: Check and run the login
        if not attr.logged:
            await serverlogin(websocket, login_signal)
        
        # FIX 3: Use a fresh IF (not ELSE) so that after serverlogin 
        # changes attr.logged to True, the server enters the loop.
        if attr.logged:
            print("Login successful. Listening for commands...")
            while True:
                message = await websocket.recv()
                await forever(websocket, message)
                
    except ConnectionClosed:
        print("Client disconnected gracefully.")
    except Exception as e:
        print(f"Error in connection handler: {e}")
    finally:
        attr.logged = False # Reset for the next session
async def serveron():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("WebSocket Server started on ws://localhost:8765")
        await asyncio.Future()  

if __name__ == "__main__":
    try:
        asyncio.run(serveron())
    except Exception as e:
        print(f"Server execution error: {e}")