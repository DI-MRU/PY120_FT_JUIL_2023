import React from 'react';
import { useAuth } from './Auth';
import { useNavigate } from 'react-router-dom';

function HomePage() {
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  if (!isAuthenticated) {
    // Redirect to the login page if not authenticated
    navigate('/login');
    return <div>Not login</div>; 
  }

  return (
    <div>
      <h2>Home Page</h2>
      <p>Welcome to the Home Page! You are authenticated.</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default HomePage;
