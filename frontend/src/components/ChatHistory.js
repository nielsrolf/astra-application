import React from 'react';

const ChatHistory = ({ messages }) => {
  return (
    <div className="chat-history">
      {messages.map((message, index) => (
        <p key={index}>{message}</p>
      ))}
    </div>
  );
};

export default ChatHistory;
