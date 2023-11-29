// ChatInput.js
import React, { useState } from 'react';

const ChatInput = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (message.trim()) {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} style={{ display: 'flex', width: '100%' }}>
        <input
          className="input-field"
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message..."
        />
        <button className="send-button" type="submit">Send</button>
      </form>
    </div>
  );
};

export default ChatInput;
