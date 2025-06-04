# auth-system
Gabarito do Trabalho 1 do segundo trimestre da disciplina Desenvolvimento WEB 2

# Sistema de Autenticação de Usuários

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1+-purple.svg)

## 📌 Visão Geral

Sistema completo de autenticação de usuários desenvolvido com Flask, implementando as melhores práticas de segurança.

## ✨ Funcionalidades Principais

- 🛡️ **Autenticação Segura**
  - Cadastro de novos usuários
  - Login com hash bcrypt
  - Logout com limpeza de sessão

- 🔐 **Proteção Avançada**
  - CSRF tokens em todos os forms
  - Prevenção contra SQL Injection
  - Sanitização contra XSS

- 👤 **Gerenciamento de Conta**
  - Perfil do usuário
  - Alteração segura de senha
  - Sessões controladas

## 🛠️ Tecnologias

| Camada       | Tecnologias                          |
|--------------|--------------------------------------|
| **Backend**  | Python, Flask, Flask-Login, Bcrypt   |
| **Frontend** | HTML5, Bootstrap 5, Jinja2          |
| **Banco**    | MySQL com conexão segura             |
| **Segurança**| CSRF protection, Password hashing    |

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- MySQL 8.0+
- Pipenv (recomendado)

bash
# 1. Clone o repositório
git clone https://github.com/rafael-vieira-coelho/auth-system.git
cd auth-system

# 2. Configure ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure o banco (edite config.py)
nano config.py

# 5. Execute
python app.py

Acesse: http://localhost:5000

## 🛡️ Medidas de Segurança

1. **Senhas**
   - Hash com bcrypt (salt automático)
   - Complexidade mínima exigida

2. **Sessões**
   - Cookies seguros (HttpOnly, Secure)
   - Timeout automático

3. **Proteção CSRF**
   - Tokens em todos os formulários
   - Validação server-side

4. **Banco de Dados**
   - Prepared statements
   - Conexões criptografadas

## 📝 Documentação Adicional

### Variáveis de Ambiente

Crie um arquivo .env na raiz:

ini
FLASK_SECRET_KEY=sua_chave_super_secreta
DB_HOST=localhost
DB_USER=root
DB_PASS=
DB_NAME=auth_system


### API Endpoints

| Endpoint            | Método | Descrição                          |
|---------------------|--------|------------------------------------|
| /api/register     | POST   | Registro de usuário (JSON)         |
| /api/login        | POST   | Autenticação (JWT)                 |
| /api/user         | GET    | Dados do usuário autenticado       |

