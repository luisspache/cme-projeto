import React, { useState } from 'react'
import axios from 'axios'

export default function CadastroMaterial() {
  const [name, setName] = useState('')
  const [type, setType] = useState('')
  const [expirationDate, setExpirationDate] = useState('')
  const [mensagem, setMensagem] = useState('')

  const handleCadastrar = async () => {
    try {
      const response = await axios.post('http://localhost:8000/materials/', null, {
        params: {
          name,
          type,
          expiration_date: expirationDate
        }
      })
      setMensagem(`✅ Material cadastrado com serial: ${response.data.serial}`)
    } catch (error) {
      setMensagem('❌ Erro ao cadastrar material')
    }
  }

  return (
    <div>
      <h2>Cadastro de Material</h2>
      <input
        placeholder="Nome"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ display: 'block', marginBottom: 8 }}
      />
      <input
        placeholder="Tipo"
        value={type}
        onChange={(e) => setType(e.target.value)}
        style={{ display: 'block', marginBottom: 8 }}
      />
      <input
        type="date"
        placeholder="Data de Validade"
        value={expirationDate}
        onChange={(e) => setExpirationDate(e.target.value)}
        style={{ display: 'block', marginBottom: 8 }}
      />
      <button onClick={handleCadastrar}>Cadastrar</button>
      <p>{mensagem}</p>
    </div>
  )
}
