// frontend/src/components/PredictionForm.js
import React, { useState } from 'react';
import axios from 'axios';
import './PredictionForm.css';

const PredictionForm = () => {
  const [age, setAge] = useState('');
  const [sex, setSex] = useState('');
  const [bmi, setBmi] = useState('');
  const [children, setChildren] = useState('');
  const [smoker, setSmoker] = useState('');
  const [region, setRegion] = useState('');
  const [expenses, setExpenses] = useState('');
  const [cibilScore, setCibilScore] = useState('');
  const [prediction, setPrediction] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    const formData = {
      data: {
        age,
        sex,
        bmi,
        children,
        smoker,
        region,
        expenses,
        cibil_score: cibilScore
      }
    };

    try {
      const response = await axios.post('http://localhost:5000/api/predict/predict', formData);
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error making prediction', error);
    }

    setLoading(false);
  };

  return (
    <div className="form-container">
      <h2>Enter Details for Prediction</h2>
      <form onSubmit={handleSubmit}>
        <label>Age:</label>
        <input type="number" value={age} onChange={(e) => setAge(e.target.value)} />

        <label>Sex (male/female):</label>
        <input type="text" value={sex} onChange={(e) => setSex(e.target.value)} />

        <label>BMI:</label>
        <input type="number" value={bmi} onChange={(e) => setBmi(e.target.value)} />

        <label>Children:</label>
        <input type="number" value={children} onChange={(e) => setChildren(e.target.value)} />

        <label>Smoker (yes/no):</label>
        <input type="text" value={smoker} onChange={(e) => setSmoker(e.target.value)} />

        <label>Region:</label>
        <input type="text" value={region} onChange={(e) => setRegion(e.target.value)} />

        <label>Expenses:</label>
        <input type="number" value={expenses} onChange={(e) => setExpenses(e.target.value)} />

        <label>CIBIL Score:</label>
        <input type="number" value={cibilScore} onChange={(e) => setCibilScore(e.target.value)} />

        <button type="submit" disabled={loading}>
          {loading ? 'Predicting...' : 'Predict'}
        </button>
      </form>

      {prediction && <div className="prediction-result">Prediction: {prediction}</div>}
    </div>
  );
};

export default PredictionForm;
