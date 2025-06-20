import express from 'express';
import { Server } from 'socket.io';
import http from 'http';
import axios from 'axios';
import jwt from 'jsonwebtoken';
import { promises as fs } from 'fs';
import { v4 as uuidv4 } from 'uuid';

const PORT = process.env.PORT || 4000;
const JWT_SECRET = process.env.JWT_SECRET || 'secret';
const MODERATION_URL = process.env.MODERATION_URL || 'http://localhost:8000/moderate';
const MESSAGES_FILE = './messages.json';

async function loadMessages() {
  try {
    const data = await fs.readFile(MESSAGES_FILE, 'utf-8');
    return JSON.parse(data);
  } catch {
    return [];
  }
}

async function saveMessages(messages) {
  await fs.writeFile(MESSAGES_FILE, JSON.stringify(messages, null, 2));
}

const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

io.use((socket, next) => {
  const { token } = socket.handshake.auth || {};
  try {
    const payload = jwt.verify(token, JWT_SECRET);
    socket.user = { id: payload.sub };
    next();
  } catch (err) {
    next(new Error('Authentication error'));
  }
});

io.on('connection', async (socket) => {
  const messages = await loadMessages();
  socket.emit('history', messages);

  socket.on('message', async (content) => {
    try {
      const { data } = await axios.post(MODERATION_URL, { content });
      if (data.accepted) {
        const message = { id: uuidv4(), user: socket.user.id, content, timestamp: Date.now() };
        const newMessages = [...messages, message];
        await saveMessages(newMessages);
        io.emit('message', message);
      } else {
        socket.emit('rejected', data.reason || 'Message rejected');
      }
    } catch (err) {
      socket.emit('rejected', 'Moderation service error');
    }
  });
});

server.listen(PORT, () => {
  console.log(`Chat server listening on port ${PORT}`);
});
