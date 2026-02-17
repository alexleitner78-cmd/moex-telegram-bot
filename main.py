import os
import requests
from fastapi import FastAPI, Request

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

app = FastAPI()

def send_telegram(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text}, timeout=10)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message", str(data))
    send_telegram(message)
    return {"ok": True}

@app.get("/")
def root():
    return {"status": "running"}
