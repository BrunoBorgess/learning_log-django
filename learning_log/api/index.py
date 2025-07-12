import sys
import os

# Adiciona a raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Agora importa o WSGI da pasta correta
from learning_log.wsgi import application

