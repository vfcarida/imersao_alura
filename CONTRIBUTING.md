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
- **Docstrings**: Todas as funções, módulos e classes devem estar documentados seguindo o formato de Docstrings utilizado (baseado em Sphinx/Google).
- **Separação de Responsabilidades**: Não adicione regras de negócio nos arquivos dentro de `src/components/`. A manipulação de dados pesada deve estar isolada ou no `filters.py` ou em serviços separados.
- **Sem Magic Strings**: Se você precisa adicionar uma URL ou constante, coloque no `config.py`.

## 3. Testes Locais

Antes de abrir o Pull Request, você deve certificar-se de que os testes passam e que o código está seguindo os padrões de estilo.

1. **Rode os Linters**:
```bash
flake8 src tests
black --check src tests
```

2. **Execute os Testes Unitários**:
```bash
pytest tests/ -v
```

Apenas PRs que passam em todas as verificações do CI/CD (GitHub Actions) serão aprovados e integrados.
