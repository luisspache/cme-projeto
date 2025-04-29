import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import Login from './pages/Login'
import CadastroMaterial from './pages/CadastroMaterial'
import Rastreabilidade from './pages/Rastreabilidade'

export default function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>CME - Central de Materiais e Esterilização</h1>
      <nav style={{ marginBottom: '20px' }}>
        <Link to="/" style={{ marginRight: '10px' }}>Login</Link>
        <Link to="/cadastro" style={{ marginRight: '10px' }}>Cadastro de Material</Link>
        <Link to="/rastreabilidade">Rastreabilidade</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/cadastro" element={<CadastroMaterial />} />
        <Route path="/rastreabilidade" element={<Rastreabilidade />} />
      </Routes>
    </div>
  )
}
