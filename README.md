# Desafio Técnico – Desenvolvedor(a) Full-Stack (Sênior)

## 📌 Contexto

A Prefeitura do Rio de Janeiro quer oferecer aos cidadãos uma Plataforma de Solicitação de Serviços Municipais, onde qualquer pessoa pode solicitar reparos urbanos (como buracos na rua, semáforos quebrados, coleta de entulho, entre outros). O sistema deve permitir que os moradores cadastrem solicitações, acompanhem o status dos pedidos e visualizem demandas já registradas em sua região.

Seu desafio é desenvolver uma aplicação full-stack usando Next.js no front-end e FastAPI no back-end para oferecer essa funcionalidade de maneira eficiente e escalável.

## ✨ Requisitos do Desafio

### 🔹 Funcionalidades Esperadas

#### Frontend (Next.js)

- Página principal com:
    - Lista de solicitações mais recentes, incluindo título, categoria, bairro e status (pendente, em andamento, concluído).
    - Botão para registrar uma nova solicitação.

- Página de detalhe de solicitação:
    - Exibir todas as informações da solicitação.
    - Permitir que o usuário acompanhe o status da solicitação.

- Formulário de nova solicitação:
    - Campos: Título, descrição, categoria, bairro, fotos (upload opcional).
    - Validação dos campos obrigatórios.

- Mapa interativo:
    - Exibir as solicitações em um mapa, permitindo visualizar as ocorrências por bairro.

#### Backend (FastAPI)

- API RESTful para gerenciar solicitações com os seguintes endpoints:
    - POST /solicitacoes/ → Criar uma nova solicitação.
    - GET /solicitacoes/ → Listar todas as solicitações.
    - GET /solicitacoes/{id}/ → Obter detalhes de uma solicitação específica.
    - PATCH /solicitacoes/{id}/ → Atualizar o status da solicitação.

- Banco de Dados: Usar PostgreSQL (ou SQLite para desenvolvimento).
- ORM: Usar SQLAlchemy ou Tortoise-ORM para manipulação do banco.

### 🔹 Requisitos Técnicos

- Next.js para o front-end, com SSR (Server-Side Rendering) e otimizações de performance.
- FastAPI para o back-end, estruturado de forma modular e bem organizada.
- Gerenciamento de estado no front-end (Redux, Context API, Zustand, etc).
- Banco de dados relacional para armazenar as solicitações.
- Testes automatizados no back-end e front-end.
- Docker para facilitar o setup do projeto.
- CI/CD: Pipeline básico para rodar os testes automaticamente.
- Documentação clara sobre como rodar o projeto.

### 🔹 Diferenciais (não obrigatórios, mas valorizados)

- Uso de TypeScript no front-end.
- Autenticação JWT para proteger endpoints de administração.
- Integração com um serviço de mapas (ex: OpenStreetMap, Leaflet.js, Mapbox).
- Boas práticas de acessibilidade e SEO.
- Hospedagem do projeto em um ambiente online (Vercel, Railway, etc).

## 🏗️ Como Submeter o Desafio

1. Faça um fork ou clone este repositório.
2. Implemente a solução seguindo os requisitos descritos.
3. Inclua um pequeno documento (ou atualize este README) explicando suas decisões técnicas, estrutura do código e instruções para rodar o projeto.
4. Envie o link do repositório para nós!

## 📖 O que será avaliado?
- Qualidade do código e organização do projeto.
- Boas práticas de desenvolvimento (clean code, componentização, modularidade, etc.).
- Eficiência no consumo de APIs e manipulação de dados.
- Usabilidade, responsividade e acessibilidade da interface.
- Implementação de testes e boas práticas de CI/CD.
- Documentação clara do projeto.

## ❓ Dúvidas?

Se tiver qualquer dúvida, fique à vontade para perguntar!

Boa sorte! 🚀