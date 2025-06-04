import os

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'auth_system'
}

# Chave secreta para sessões
SECRET_KEY = os.urandom(24)