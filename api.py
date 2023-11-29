from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from main import Agent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    print("yo")
    await websocket.accept()
    while True:
        try:
            user_message = await websocket.receive_text()
            print(user_message)

            async def send_to_websocket(message: str):
                try:
                    await websocket.send_text(message)
                except Exception as e:
                    print("websocket error", e)
                
            agent = Agent(on_new_token=send_to_websocket)
            return await agent.reply(user_message)
        except Exception as e:
            print(e)
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1234)
