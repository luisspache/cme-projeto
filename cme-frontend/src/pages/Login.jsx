import React, { useState } from 'react'
import axios from 'axios'

export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [mensagem, setMensagem] = useState('')

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login/', null, {
        params: { username, password }
      })
      setMensagem(`✅ Login bem-sucedido: ${response.data.user.username} (${response.data.user.role})`)
    } catch (error) {
      setMensagem('❌ Falha no login. Verifique as credenciais.')
    }
  }

  return (
    <div>
      <h2>Login</h2>
      <input
        placeholder="Usuário"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        style={{ display: 'block', marginBottom: 8 }}
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ display: 'block', marginBottom: 8 }}
      />
      <button onClick={handleLogin}>Entrar</button>
      <p>{mensagem}</p>
    </div>
  )
}
