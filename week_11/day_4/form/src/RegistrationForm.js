import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function RegistrationForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false); // For showing loading indicator
  const navigate = useNavigate();
  const [error, setError] = useState(null);

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleRegistration = async (event) => {
    event.preventDefault();

    if (isLoading) {
      return; // Prevent multiple registration attempts while loading
    }

    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        // Registration successful
        navigate('/login'); // Redirect to the login page after successful registration
      } else {
        // Registration failed
        const data = await response.json();
        setError(data.message);
      }
    } catch (error) {
      // Handle network or other errors
      setError('An error occurred while registering.');
    } finally {
      setIsLoading(false); // Reset loading state
    }
  };

  return (
    <div>
      <h2>Registration</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleRegistration}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={handleUsernameChange}
          disabled={isLoading}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={handlePasswordChange}
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Registering...' : 'Register'}
        </button>
      </form>
    </div>
  );
}

export default RegistrationForm;
