CME - Central de Materiais e Esterilização

Este projeto é uma aplicação web fullstack para gerenciamento e rastreabilidade de materiais esterilizados
Desenvolvido com:

Backend: FastAPI (Python)
Frontend: React + Vite
Banco de dados: PostgreSQL
Containerização: Docker + Docker Compose
Funcionalidades

Tela de login
Cadastro de materiais (nome, tipo, validade com serial automático)
Registro de etapas do processo (ex: Lavagem, Esterilização, Distribuição)
Consulta da rastreabilidade por serial
Integração completa entre frontend, backend e banco de dados
Estrutura do Projeto

cme-projeto-fullstack/
├── cme-backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── cme-frontend/
│   ├── public/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
└── README.md
Requisitos

Docker
Docker Compose
Como executar

Tecnologias utilizadas

Python 3.11
FastAPI
PostgreSQL
SQLAlchemy
React 18 + Vite
Docker
Autor

Luis Cláudio Pacheco Seixas
GitHub: @luisspache
