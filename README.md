# 📊 Dashboard de Salários na Área de Dados

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.44.1-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/vqrca/dashboard_salarios_dados/actions/workflows/ci.yml/badge.svg)](https://github.com/vqrca/dashboard_salarios_dados/actions)

Um dashboard interativo, escalável e de nível de produção, construído em **Streamlit** para análise de salários na área de dados. Explore dados globais sobre cargos, remunerações, modalidades de trabalho (remoto/híbrido/presencial) e níveis de senioridade, tudo com gráficos dinâmicos e de alta performance.

> **Status do Projeto:** Totalmente refatorado utilizando os princípios de Clean Architecture, Clean Code, SOLID e Type Hinting, garantindo segurança de tipos e performance otimizada.

---

## 🏗️ Visão Geral e Arquitetura

O projeto foi construído para servir de referência em boas práticas para aplicações de dados em Python:

- **Performance Otimizada:** Implementação de `@st.cache_data` para download e processamento único dos dados. O *fetch* de dados ocorre de forma otimizada.
- **Desacoplamento e Clean Architecture:** Componentes visuais (`src/components/`) são puramente focados na apresentação. Regras de negócios e filtragem de Pandas vivem isolados em `src/filters.py`, facilitando testes unitários sem mockar todo o frontend.
- **Robustez (Error Handling e Logging):** A aplicação implementa tratamento formal de exceções em todos os módulos, registrando logs estruturados. Se um gráfico falhar ao renderizar devido a dados corrompidos, a UI avisa o usuário sem "quebrar" a aplicação com tracebacks.
- **Ecossistema Moderno:** Utiliza `pyproject.toml` para o gerenciamento de dependências e metadados, além de conter `Dockerfile` para conteinerização rápida.

Consulte a [Documentação de Arquitetura](docs/architecture.md) para detalhes mais profundos.

---

## 🚀 Pré-requisitos

Para rodar ou contribuir com o projeto, você precisará de:

- **Python 3.10+**
- **Git**

*(Para deploy em containers)*
- **Docker** e **Docker Compose**

---

## ⚙️ Instalação Passo a Passo

Siga as instruções abaixo para executar o dashboard em sua máquina local.

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/dashboard_salarios_dados.git
cd dashboard_salarios_dados
```

### 2. Configurar o Ambiente Virtual
Recomenda-se a utilização do ambiente virtual para isolar as bibliotecas:

```bash
# No Windows
python -m venv venv
.\venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalação das Dependências
Instale o projeto e as dependências em modo de desenvolvimento, aproveitando o `pyproject.toml`:

```bash
pip install -e .[dev]
```

### 4. Configurar as Variáveis de Ambiente
Copie o template de `.env`:

```bash
cp .env.example .env
```

---

## 🎮 Exemplo de Uso

Inicie a aplicação utilizando o Streamlit. Como reestruturamos o entrypoint, você pode rodá-lo facilmente a partir da raiz:

```bash
streamlit run app.py
```

O dashboard abrirá no seu navegador padrão (`http://localhost:8501`).  
Use a barra lateral (**sidebar**) para aplicar múltiplos cruzamentos (ex: filtrar por `Ano: 2023`, `Senioridade: Pleno`, `Tamanho da Empresa: Grande`). Os KPIs e os gráficos (*Top Cargos*, *Histograma*, *Trabalho Remoto*) se atualizarão instantaneamente graças à otimização do Pandas.

---

## 🐳 Executando com Docker

Se preferir não instalar nada localmente, execute via Docker:

```bash
# Construir a imagem
docker build -t dashboard-salarios .

# Rodar o contêiner na porta 8501
docker run -p 8501:8501 dashboard-salarios
```

---

## 📁 Estrutura do Projeto

Abaixo a árvore de diretórios pós-refatoração (padrões de mercado):

```text
.
├── .github/workflows/   # CI/CD (GitHub Actions)
├── app.py               # Ponto de entrada (Entrypoint) do Streamlit
├── pyproject.toml       # Dependências e Metadados do Projeto
├── Dockerfile           # Imagem para implantação na nuvem
├── docs/                # Documentação complementar (ADRs, etc.)
├── src/                 # Pacote Python principal
│   ├── __init__.py
│   ├── config.py        # Central de configurações globais
│   ├── data_loader.py   # Lógica de extração e ingestão de dados
│   ├── filters.py       # Core Domain (regras de manipulação de dataframes)
│   └── components/      # UI: Módulos visuais (sidebar, metrics, charts)
├── tests/               # Testes unitários utilizando Pytest
└── README.md            # Documentação principal
```

---

## 🤝 Como Contribuir

Ficou interessado em ajudar a melhorar o projeto?  
Consulte o nosso **[Guia de Contribuição](CONTRIBUTING.md)** para entender:
- Fluxo de trabalho (Git Flow)
- Padrões de código (`flake8`, `black`)
- Como rodar os testes (`pytest`)

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.
