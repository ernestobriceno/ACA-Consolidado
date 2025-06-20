from fastapi import FastAPI
from schemas.message import Message
from DetoxifyMultillingual.DetoxifyMultillingual import Detoxify

THRESHOLD = 0.5

detoxify = Detoxify()
app = FastAPI()

@app.post('/moderate')
async def moderate(message: Message):
    results = detoxify.predict(message.content)
    scores = {key: float(value) for key, value in results.items()}
    toxic = any(score >= THRESHOLD for score in scores.values())
    return {
        'accepted': not toxic,
        'reason': 'toxic content' if toxic else None,
        'scores': scores,
    }

