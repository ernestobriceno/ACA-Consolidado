# ElephanTalk Chat

This repository contains a simple real-time chat prototype.

## Setup

### Moderation Service
```
cd Backend/MicroserviceModeration
pip install -r requirements.txt
uvicorn main:app --reload
```

### Chat Server
```
cd Backend/ChatServer
npm install
cp .env.example .env
# edit .env with JWT secret and moderation URL
npm start
```

### Frontend
```
cd Frontent
npm install
cp .env.example .env
# set VITE_CHAT_URL to the chat server url
npm run dev
```

## Usage
1. Authenticate in the main application so a JWT token is stored in `localStorage`.
2. Open the chat component page and start sending messages.
3. Messages are moderated before broadcasting. If rejected you will see a toast notification.

## Testing
- Backend chat server currently has no automated tests.
- Moderation service tests can be executed with:
```
cd Backend/MicroserviceModeration
pytest
```

