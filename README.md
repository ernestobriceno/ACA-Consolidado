# 🐘 ElephanTalk - Chat Grupal en Tiempo Real

Este repositorio contiene una implementación completa y consolidada de un chat grupal en tiempo real, que integra:

📅 **Frontend** en React con Vite
🚀 **Backend** con Socket.IO, JWT y persistencia de mensajes
🔗 **Servicio de Moderación** con FastAPI usando el modelo Detoxify
📃 Documentación unificada y pruebas para cada componente

---

## 📦 Requisitos

* **Node.js** v20 o superior
* **Python** 3.10 o superior
* **Docker** (opcional para el servicio de moderación)
* **torch** para el servicio Detoxify (modelo AI)

---

## ✨ Configuración

### 1. Servicio de Moderación (FastAPI + Detoxify)

```bash
cd Backend/MicroserviceModeration
pip install -r requirements.txt
uvicorn main:app --reload
```

📌 Este servicio analiza mensajes con Detoxify Multilingual.

📅 Primer uso descarga pesos del modelo; requiere conexión a internet.

#### Alternativa con Docker:

```bash
docker build -t moderation-service .
docker run -p 8000:8000 moderation-service
```

### 2. Servidor de Chat (Node.js + Socket.IO)

```bash
cd Backend/ChatServer
npm install
cp .env.example .env
# Configura JWT_SECRET y MODERATION_URL si es necesario
npm start
```

🔹 El servidor escucha por defecto en el puerto `4000`.

🔹 Los mensajes se guardan en `messages.json`.

### 3. Frontend (React + Vite)

```bash
cd Frontend
npm install
cp .env.example .env
# Define VITE_CHAT_URL con la URL del servidor de chat (ej. http://localhost:4000)
npm run dev
```

🔹 Accede al chat en `http://localhost:5173/chat`

🔹 Se requiere JWT en `localStorage` para funcionar.

---

## ✅ Pruebas

### ChatServer (Node.js)

```bash
cd Backend/ChatServer
npm test
```

### Moderation (FastAPI)

```bash
cd Backend/MicroserviceModeration
pytest -q
```

Requiere:

```bash
pip install fastapi pydantic uvicorn httpx torch detoxify
```

---

## 🐳 Docker Compose (opcional)

Puedes crear un archivo `docker-compose.yml` si deseas ejecutar todos los servicios con un solo comando.

---

## 💬 Flujo del Chat

1. El usuario inicia sesión y obtiene un token JWT.
2. El frontend se conecta al backend con Socket.IO.
3. Al enviar un mensaje:

   * El backend lo reenvía al servicio de moderación.
   * Si se acepta, se difunde a todos los usuarios conectados.
   * Si se rechaza, se informa la razón al emisor.

---

## 📁 Estructura del Proyecto

```
Proyecto-ACA/
├── Backend/
│   ├── ChatServer/              → Socket.IO + JWT + persistencia
│   └── MicroserviceModeration/ → FastAPI + Detoxify
├── Frontend/                   → React + Vite + JWT
├── README.md                   → Documentación global
└── CHAT_AUDIT.md               → Registro de cambios e integraciones
```

---

## 📆 Notas Finales

* El umbral de toxicidad se puede personalizar en `main.py`
* Arquitectura preparada para escalar o cambiar de modelo de moderación
* Se recomienda uso de HTTPS y protección JWT en producción

---
