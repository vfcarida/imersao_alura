# 📊 Dashboard de Salários na Área de Dados

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.44.1-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/vqrca/dashboard_salarios_dados/actions/workflows/ci.yml/badge.svg)](https://github.com/vqrca/dashboard_salarios_dados/actions)

Um dashboard interativo e escalável construído em **Streamlit** para análise de salários na área de dados. O projeto permite a filtragem de informações sobre cargos, salários, modelo de trabalho (remoto/presencial) e senioridade.

> **Status do Projeto:** Refatorado seguindo padrões de Clean Code, SOLID e Arquitetura Modular.

## 🏗️ Visão Geral e Arquitetura

A aplicação foi reescrita para garantir alta performance, testabilidade e fácil manutenção. O monólito original foi separado em componentes coesos:

- **Performance Otimizada:** Implementação de `@st.cache_data` para download e processamento único dos dados em CSV, evitando recarregamento na navegação e nos filtros.
- **Isolamento de Regras:** Camadas visuais (componentes do Streamlit) e regras de negócios (filtros no Pandas) operam de forma independente.
- **Monitoramento e Confiabilidade:** Tratamento proativo de erros no carregamento remoto de arquivos, além de logs estruturados e Type Hinting rigoroso em todo o código.

Consulte a [Documentação de Arquitetura](docs/architecture.md) para detalhes mais profundos.

## 🚀 Pré-requisitos

- Python 3.10 ou superior
- Pip e virtualenv instalados

## ⚙️ Instalação Passo a Passo

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/dashboard_salarios_dados.git
cd dashboard_salarios_dados
```

2. **Crie e ative o ambiente virtual:**
```bash
# No Windows
python -m venv venv
.\venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configuração do Ambiente:**
Copie o arquivo de exemplo de variáveis de ambiente.
```bash
cp .env.example .env
```

## 🎮 Exemplo de Uso

Inicie o servidor localmente executando o ponto de entrada da aplicação. Certifique-se de estar na raiz do projeto (importante para que o `src/` seja carregado no Python Path):

```bash
streamlit run src/app.py
```

O painel abrirá automaticamente em seu navegador padrão no endereço `http://localhost:8501`. Na barra lateral, você pode cruzar os dados usando múltiplos filtros simultâneos, e os gráficos Plotly (Top 10 Cargos, Histograma e Distribuição Remota) se ajustarão dinamicamente com animações fluidas.

## 📁 Estrutura do Projeto

```text
.
├── .github/workflows/   # Configurações do GitHub Actions (CI/CD)
├── docs/                # Documentação avançada (Arquitetura, etc.)
├── src/                 # Código-fonte principal da aplicação
│   ├── components/      # Módulos visuais Streamlit (sidebar, metrics, charts)
│   ├── app.py           # Entrypoint da aplicação Streamlit
│   ├── config.py        # Central de configurações e constantes
│   ├── data_loader.py   # Lógica de extração e cache de dados remotos
│   └── filters.py       # Regras de negócio de DataFrames (Pandas)
├── tests/               # Testes unitários com Pytest
├── .env.example         # Template de variáveis de ambiente
├── requirements.txt     # Dependências (Produção + Desenvolvimento)
├── README.md            # Documentação principal
└── CONTRIBUTING.md      # Diretrizes para contribuição
```

## 🤝 Como Contribuir

Ficou interessado em ajudar? Leia o nosso [Guia de Contribuição](CONTRIBUTING.md) para entender os padrões de código (flake8, black) e o fluxo de Pull Requests.

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
