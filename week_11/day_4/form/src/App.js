import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import RegistrationForm from "./RegistrationForm";
import LoginForm from "./LoginForm";
import HomePage from "./HomePage";
import { useAuth } from "./Auth";

function App() {
  const { isAuthenticated } = useAuth();

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route
            path="/"
            element={isAuthenticated ? <HomePage /> : <RegistrationForm />}
          />
          <Route path="/home" element={<HomePage />} />
          <Route path="/login" element={<LoginForm />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

