# 🐘 ElephanTalk - Real Time Chat Integration

Este repositorio contiene una implementación completa y consolidada de un chat grupal en tiempo real, que integra:

👉 **Frontend** en React con Vite
👉 **Backend** con Socket.IO, JWT y persistencia de mensajes
👉 **Servicio de Moderación** con FastAPI usando el modelo Detoxify
👉 Documentación unificada y pruebas para cada componente

---

## 📦 Requisitos

* **Node.js** v20 o superior
* **Python** 3.10 o superior
* **Docker** (opcional para la moderación)
* **torch** para el servicio de moderación con Detoxify

---

## ✨ Configuración

### 1. Servicio de Moderación (FastAPI + Detoxify)

```bash
cd Backend/MicroserviceModeration
pip install -r requirements.txt
uvicorn main:app --reload
```

📌 El servicio usa el modelo Detoxify Multilingual y se conecta por defecto en `http://localhost:8000`.
📌 La primera ejecución descargará los pesos del modelo; se necesita conexión a internet.

#### Alternativa con Docker:

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
# Configura JWT_SECRET y MODERATION_URL si es necesario
npm start
```

📌 El servidor escucha en el puerto especificado en `.env` (por defecto `4000`).
📌 Los mensajes se guardan localmente en `messages.json`.

---

### 3. Frontend (React + Vite)

```bash
cd Frontend
npm install
cp .env.example .env
# Define VITE_CHAT_URL con la URL del servidor de chat (ej. http://localhost:4000)
npm run dev
```

📌 Abre `http://localhost:5173/chat`
📌 El usuario debe tener un token JWT válido almacenado en `localStorage`.

---

## ✅ Pruebas

### Backend (Servidor de Chat)

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

Este repositorio incluye `Dockerfile` para cada servicio principal. Puedes crear un `docker-compose.yml` si deseas orquestar todo el entorno con un solo comando.

---

## 💬 Flujo del Chat

1. El usuario inicia sesión en la aplicación y obtiene un token JWT.
2. El frontend se conecta vía Socket.IO al servidor de chat.
3. Al enviar un mensaje:

   * El backend lo reenvía al servicio de moderación.
   * Si es aceptado, se difunde a todos los clientes.
   * Si es rechazado, se notifica al remitente con la razón.

---

## 📁 Estructura del Proyecto

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

## 📅 Notas Finales

* Puedes personalizar los umbrales de toxicidad en `Backend/MicroserviceModeration/main.py`.
* La arquitectura está diseñada para escalar y permite reemplazar Detoxify por otro modelo si es necesario.
* Asegura el despliegue en producción con HTTPS, variables de entorno y tokens JWT fuertes.

---
