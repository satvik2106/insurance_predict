// frontend/src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from './components/Register';
import PredictionForm from './components/PredictionForm';
import Home from './components/Home'; // Assuming you have a Home component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/predict" element={<PredictionForm />} />
      </Routes>
    </Router>
  );
}

export default App;
