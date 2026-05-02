"""
Configurações globais do sistema.
Centraliza variáveis, constantes, URLs e configurações estáticas para evitar 'magic strings' no código.
"""
import logging

# Configuração de Logging Estruturado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# URLs e Constantes de Dados
DATA_URL = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"

# Configurações de Interface (Streamlit)
PAGE_TITLE = "Dashboard de Salários na Área de Dados"
PAGE_ICON = "📊"
LAYOUT = "wide"
