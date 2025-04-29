import React, { useState } from 'react'
import axios from 'axios'

export default function Rastreabilidade() {
  const [serial, setSerial] = useState('')
  const [etapas, setEtapas] = useState([])
  const [mensagem, setMensagem] = useState('')

  const buscarRastreamento = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/tracking/${serial}`)
      setEtapas(response.data)
      setMensagem('')
    } catch (error) {
      setEtapas([])
      setMensagem('❌ Material não encontrado ou erro na consulta.')
    }
  }

  return (
    <div>
      <h2>Rastreabilidade</h2>
      <input
        placeholder="Serial do Material"
        value={serial}
        onChange={(e) => setSerial(e.target.value)}
        style={{ display: 'block', marginBottom: 8 }}
      />
      <button onClick={buscarRastreamento}>Buscar</button>

      {mensagem && <p>{mensagem}</p>}

      {etapas.length > 0 && (
        <div>
          <h3>Etapas:</h3>
          <ul>
            {etapas.map((etapa, index) => (
              <li key={index}>
                {etapa.step} {etapa.failure ? `(falha: ${etapa.failure})` : ''}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}
