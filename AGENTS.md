# AGENTS.md

## Linguagem
- Todas as respostas e comentários devem ser em português.

## Ambiente
- Diretório de trabalho: `C:\Projectos 2026\teste`
- Shell: PowerShell

## Convenções de trabalho
- Priorizar comandos `rg` para busca de ficheiros e texto.
- Evitar ações destrutivas (ex.: `git reset --hard`) salvo pedido explícito.
- Explicar de forma clara o que foi feito e porquê, em português.

## Projeto
- Tipo: aplicação web full-stack.
- Backend: Django 6.0 (versão estável atual).
- Python: 3.14 (usar a última versão micro disponível).
- Frontend: templates Django por padrão (JS/CSS quando necessário).
- Base de dados: SQLite para desenvolvimento local; PostgreSQL para produção.
- Para produção, planear migração com `dumpdata/loaddata` ou ferramentas da stack, mantendo `settings` separados por ambiente.

## Qualidade e execução
- Testes: `python -m pytest` se houver `pytest`, caso contrário `python manage.py test`.
- Lint/format: seguir o que existir no repositório; se nada existir, manter estilo consistente.
