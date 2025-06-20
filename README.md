# ElephanTalk - Real Time Chat Prototype

This repository contains a minimal chat application that integrates a Node.js Socket.IO server, a React frontend and a Python FastAPI service for message moderation using Detoxify.

## Requirements
- **Node.js 20+** for the frontend and chat server
- **Python 3.10+** for the moderation service
- **Docker** *(optional)* if you prefer containerised execution

## Setup
Follow these steps to run each service locally. Copy the provided `.env.example` files and adjust the variables as needed.

### 1. Moderation Service
```bash
cd Backend/MicroserviceModeration
pip install -r requirements.txt
uvicorn main:app --reload
```
This demo uses a simplified moderation rule set that blocks messages containing
words like `stupid` or `idiot`. No additional environment variables are
required. The service will be available on `http://localhost:8000`.

To run it with Docker instead:
```bash
docker build -t moderation-service .
docker run -p 8000:8000 moderation-service
```

### 2. Chat Server
```bash
cd Backend/ChatServer
npm install
cp .env.example .env
# set JWT_SECRET and MODERATION_URL if different
npm start
```
The server listens on the port defined in `.env` (default `4000`). Messages are stored in `messages.json`.

### 3. Frontend
```bash
cd Frontent
npm install
cp .env.example .env
# set VITE_CHAT_URL to the chat server URL
npm run dev
```
After starting, open `http://localhost:5173/chat` (or the Vite dev server port) to use the chat. The user must be authenticated in the main app so a JWT token is available in `localStorage`.

## Testing
Execute the automated tests for each backend service:
```bash
cd Backend/ChatServer && npm test
cd ../MicroserviceModeration && pytest -q
```
These tests run using the simplified rule set so heavy dependencies such as `torch` are not required. Installing `torch` is only needed when running the original Detoxify model.

## Using Docker Compose
The repository includes individual Dockerfiles but no compose file. You can build and run the moderation and API images separately using the commands shown above or adapt them to your own `docker-compose.yml`.

---
With all services running you can send and receive messages in real time. Content is checked by the moderation service before being broadcast to all connected clients.
