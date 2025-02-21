import React from 'react';
import './Navbar.css';  // If you have a separate CSS file for styling

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Health Insurance</h1>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/login">Login</a></li>
        <li><a href="/signup">Signup</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
