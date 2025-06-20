# ElephanTalk - Real Time Chat Integration

Este repositorio contiene una implementación consolidada de un chat grupal en tiempo real, que integra:

* ✅ **Frontend** en React con Vite
* ✅ **Backend** con Socket.IO, JWT y persistencia de mensajes
* ✅ **Servicio de moderación** con FastAPI usando el modelo Detoxify
* ✅ Documentación unificada y pruebas para cada componente

---

## 📦 Requisitos

* **Node.js** v20 o superior
* **Python** 3.10 o superior
* **Docker** (opcional para moderación)
* **torch** para el servicio de moderación con Detoxify

---

## 🚀 Setup

### 1. Servicio de Moderación (FastAPI + Detoxify)

```bash
cd Backend/MicroserviceModeration
pip install -r requirements.txt
uvicorn main:app --reload
```

📌 Este servicio analiza el contenido con el modelo Detoxify para detectar mensajes tóxicos.
📌 Corre por defecto en `http://localhost:8000`.

#### Alternativa con Docker

```bash
docker build -t moderation-service .
docker run -p 8000:8000 moderation-service
```

---

### 2. Servidor de Chat (Node.js + Socket.IO)

```bash
cd Backend/ChatServer
npm install
cp .env.example .env
# Edita .env con tu JWT_SECRET y MODERATION_URL si es necesario
npm start
```

📌 El servidor escucha en el puerto especificado en `.env` (por defecto `4000`).
📌 Los mensajes se guardan en `messages.json`.

---

### 3. Frontend (React + Vite)

```bash
cd Frontend
npm install
cp .env.example .env
# Asegúrate de definir VITE_CHAT_URL con la URL del chat server
npm run dev
```

📌 Abre `http://localhost:5173/chat`
📌 El usuario debe tener un token JWT válido almacenado en `localStorage`.

---

## ✅ Pruebas

### Backend (Chat Server)

```bash
cd Backend/ChatServer
npm test
```

### Servicio de Moderación

```bash
cd Backend/MicroserviceModeration
pytest -q
```

📌 Asegúrate de tener instaladas las dependencias necesarias:

```bash
pip install fastapi pydantic uvicorn httpx torch
```

---

## 🐳 Docker Compose (opcional)

Este repositorio incluye `Dockerfile` para los servicios principales, pero no incluye un archivo `docker-compose.yml`. Puedes crear uno con base en los `Dockerfile` existentes si deseas orquestar el despliegue con un solo comando.

---

## 💬 Flujo del Chat

1. El usuario inicia sesión en la aplicación y obtiene un token JWT.
2. El frontend se conecta al servidor de chat mediante Socket.IO.
3. Al enviar un mensaje:

   * El backend lo reenvía al servicio de moderación.
   * Si es aceptado, se difunde a todos los clientes conectados.
   * Si es rechazado, se notifica al remitente con la razón.

---

## 📚 Estructura del Proyecto

```
Proyecto-ACA/
│
├── Backend/
│   ├── ChatServer/              → Socket.IO server con JWT y persistencia
│   └── MicroserviceModeration/ → Servicio FastAPI con Detoxify
│
├── Frontend/                   → Aplicación React con chat integrado
├── README.md                   → Este documento
└── CHAT_AUDIT.md               → Bitácora técnica de la integración del chat
```

---

## 📝 Notas Finales

* El servicio de moderación puede ampliarse con modelos más complejos en producción.
* La comunicación se basa en WebSockets en tiempo real usando Socket.IO.
* Se recomienda asegurar el despliegue con HTTPS y tokens JWT robustos.

---
