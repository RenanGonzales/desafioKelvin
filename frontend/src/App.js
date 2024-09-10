// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Cadastro from './Cadastro';
import Resgate from './Resgate';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Cadastro />} />
      <Route path="/resgate" element={<Resgate />} />
    </Routes>
  </Router>
);

export default App;