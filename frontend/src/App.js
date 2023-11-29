import React, { useState, useEffect } from 'react';
import './App.css'
import ChatHistory from './components/ChatHistory.js';
import ChatInput from './components/ChatInput.js';

function App() {
  const [messages, setMessages] = useState([]);
  const [websocket, setWebsocket] = useState(null);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:1234/ws');
    ws.onmessage = (event) => {
      setMessages([...messages, event.data]);
    };
    setWebsocket(ws);
    return () => ws.close();
  }, [messages]);

  const sendMessage = (message) => {
    websocket.send(message);
    setMessages([...messages, message])
  };

  return (
    <div className="App">
      <ChatHistory messages={messages} />
      <ChatInput onSendMessage={sendMessage} />
    </div>
  );
}

export default App;
