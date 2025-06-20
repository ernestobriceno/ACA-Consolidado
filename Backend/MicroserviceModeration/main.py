from fastapi import FastAPI
from schemas.message import Message
from DetoxifyMultilingual import DetoxifyMultilingual

# load detoxify model once at startup
model = DetoxifyMultilingual()

THRESHOLD = 0.5
TOXIC_FIELDS = [
    'toxicity',
    'severe_toxicity',
    'obscene',
    'identity_attack',
    'insult',
    'threat',
]

app = FastAPI()

@app.post('/moderate')
async def moderate(message: Message):
    scores = model.predict(message.content)
    toxic = any(scores.get(field, 0) >= THRESHOLD for field in TOXIC_FIELDS)
    return {
        'accepted': not toxic,
        'reason': 'toxic content' if toxic else None,
    }
