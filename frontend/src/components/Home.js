// frontend/src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <h1>Welcome to the Insurance Prediction App</h1>
      <p>Predict insurance risk based on the provided features.</p>
      <div className="home-links">
        <Link to="/register">Register</Link>
        <Link to="/predict">Make a Prediction</Link>
      </div>
    </div>
  );
};

export default Home;
