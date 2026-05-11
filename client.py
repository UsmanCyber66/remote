from smotfuncs import inpute, baseify,sha, noncify
import websockets 
async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("login") 
        
        # 1. Prepare credentials
        # Note: inpute() returns string -> sha() -> baseify()
        user_raw = inpute("Username: ")
        username_base = baseify(sha(user_raw)).decode() # Decode to string
        
        # 2. Get nonce and solve challenge
        nonce = await websocket.recv()
        auth_token = noncify(username_base, nonce)
        await websocket.send(auth_token)
        
        # 3. Wait for result
        response = await websocket.recv()
        print(f"Server: {response}")
        y="successful"
        if y in response:
            await websocket.send("ls") 
            while True:
                try:
                    data = await websocket.recv()
                    print(f"Output: {data}")
                except websockets.exceptions.ConnectionClosed:
                    break
        else:
            print("Login rejected by server.")