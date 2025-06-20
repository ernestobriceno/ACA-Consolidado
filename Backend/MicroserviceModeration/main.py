from fastapi import FastAPI
from schemas.message import Message

# Basic list of words considered toxic for demonstration purposes.
BANNED_WORDS = {"stupid", "idiot"}

app = FastAPI()


@app.post("/moderate")
async def moderate(message: Message):
    """Return whether the provided content is acceptable."""
    text = message.content.lower()
    toxic = any(word in text for word in BANNED_WORDS)
    return {
        "accepted": not toxic,
        "reason": "toxic content" if toxic else None,
    }

