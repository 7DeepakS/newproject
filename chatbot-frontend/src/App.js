import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [userInput, setUserInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  const handleUserInput = (e) => {
    setUserInput(e.target.value);
  };

  const handleSendMessage = async () => {
    setChatHistory([...chatHistory, { role: 'user', content: userInput }]);
    setUserInput('');

    try {
      const response = await axios.post('http://localhost:5000/chatbot', {
        input: userInput,
      });
      const botMessage = response.data.output;
      setChatHistory([...chatHistory, { role: 'bot', content: botMessage }]);
    } catch (error) {
      console.error('Error sending message to the server:', error);
    }
  };

  return (
    <div>
      <div>
        {chatHistory.map((message, index) => (
          <div key={index} className={message.role}>
            {message.content}
          </div>
        ))}
      </div>
      <div>
        <input type="text" value={userInput} onChange={handleUserInput} />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
