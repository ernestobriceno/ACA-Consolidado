import { useEffect, useState } from 'react';
import { io } from 'socket.io-client';
import { toast } from 'react-toastify';

const socket = io(import.meta.env.VITE_CHAT_URL, {
  autoConnect: false,
  auth: () => ({ token: localStorage.getItem('token') }),
});

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    socket.connect();
    socket.on('history', (msgs) => setMessages(msgs));
    socket.on('message', (msg) => setMessages((m) => [...m, msg]));
    socket.on('rejected', (reason) => toast.error(reason));
    return () => {
      socket.off('history');
      socket.off('message');
      socket.off('rejected');
      socket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    if (input.trim()) {
      socket.emit('message', input.trim());
      setInput('');
    }
  };

  return (
    <div className="p-4 border rounded-md">
      <div className="h-64 overflow-y-auto mb-2">
        {messages.map((m) => (
          <div key={m.id} className="mb-1">
            <strong>{m.user}:</strong> {m.content}
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          className="flex-1 border p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message"
        />
        <button className="px-4 py-2 bg-blue-500 text-white" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}
