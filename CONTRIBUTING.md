# Guia de Contribuição

Obrigado pelo seu interesse em contribuir para o **Dashboard de Salários na Área de Dados**! Para mantermos a alta qualidade, segurança e a legibilidade do código, por favor, siga estas diretrizes:

## 1. Fluxo de Trabalho (Workflow)

1. Faça o **Fork** do projeto.
2. Crie uma branch para sua feature ou correção de bug: `git checkout -b feature/minha-feature-incrivel`.
3. Desenvolva seu código.
4. Faça commit das mudanças de forma descritiva: `git commit -m 'feat: Adiciona novo filtro de localidade'`.
5. Faça o push para a branch: `git push origin feature/minha-feature-incrivel`.
6. Abra um **Pull Request (PR)** detalhando as mudanças realizadas e a motivação.

## 2. Padrões de Código (Clean Code e SOLID)

- **Type Hinting**: Sempre utilize anotações de tipo estático (`-> int`, `: pd.DataFrame`, etc.) nas assinaturas das funções.
- **Tratamento de Exceções**: Todos os componentes visuais devem tratar falhas de dados. Use os blocos `try-except` integrados com a biblioteca `logging`.
- **Docstrings**: Todas as funções, módulos e classes devem estar documentados seguindo o formato de Docstrings utilizado.
- **Separação de Responsabilidades**: Não adicione regras de negócio pesadas dentro de `src/components/`. Utilize ou crie módulos dentro de `src/` (como `filters.py`) para isso.

## 3. Testes Locais e CI/CD

Antes de abrir o Pull Request, certifique-se de que o código segue os padrões exigidos (Linters) e que os testes passam. O nosso CI/CD via GitHub Actions validará essas etapas.

### 1. Instalar as Dependências de Dev
```bash
pip install -e .[dev]
```

### 2. Rodar os Linters
```bash
flake8 src tests app.py
black --check src tests app.py
```

### 3. Executar os Testes Unitários
```bash
pytest tests/ -v
```

Apenas PRs que passam em todas as verificações do CI/CD (GitHub Actions) serão analisados para integração na `main`.
