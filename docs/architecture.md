# Documentação de Arquitetura

O **Dashboard de Salários na Área de Dados** passou por uma refatoração massiva (Overhaul) para adotar princípios profissionais de engenharia de software.

## 1. O Problema (Antes da Refatoração)

A versão inicial (v1.0) era composta por um único arquivo `app.py` monolítico (aprox. 125 linhas) com os seguintes débitos técnicos ("Bad Smells"):
- **Spaghetti Code:** Funções da UI (`st.sidebar`, `st.plotly_chart`), extração de dados HTTP (`pd.read_csv`) e manipulações (`df.loc`, `isin`) vivendo soltos no mesmo script.
- **Desempenho:** O dataframe (um CSV de ~10 MB via web) era carregado completamente do zero toda vez que o Streamlit interagia com a UI (por não usar a funcionalidade de cache de estado).
- **Falha Inesperada (Bug Lógico):** Havia problemas de escopo de variáveis onde em situações de dataframe filtrado vazio, a aplicação lançava um `NameError` referenciando uma variável `cargo_mais_comum` não instanciada.
- **Falta de Testabilidade:** Sem separação de métodos, não era possível testar a eficácia de um filtro usando Pytest sem carregar o Streamlit e uma porta web HTTP.

## 2. Solução Arquitetural (Atual)

Para atender a cenários de nível de produção:

1. **Camada de Configuração (`config.py`)**: Atua concentrando as variáveis sensíveis e hardcodes num único local.
2. **Camada de Dados / Infraestrutura (`data_loader.py`)**: Utiliza o decorador `@st.cache_data(ttl=3600)`. O fetch remoto acontece 1 vez por hora, e os próximos rerenders do Streamlit recuperam a versão persistida em cache da memória, resultando em respostas na casa de milissegundos. Introduz tratamento de erro global para evitar que o Streamlit mostre _Tracebacks_ do interpretador Python para o usuário final.
3. **Camada de Regras de Negócio (`filters.py`)**: Módulos puros. Entram parâmetros, saem dataframes. Testável de maneira unitária pura via Pytest sem precisar mockar o frontend.
4. **Camada de Apresentação Visuais (`components/`)**: Funções desacopladas especializadas exclusivamente em renderizar a tela. Consomem Dataframes já processados para pintar os gráficos (Plotly) ou métricas. O ponto de entrada (`app.py`) atua apenas como um controlador, roteando a entrada de dados para os componentes visuais.
