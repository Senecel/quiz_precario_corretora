# Quiz Precario Corretora

Aplicacao web em Django para quizzes sobre precos, comissoes e servicos. Inclui autenticacao (login/registo), resultados por utilizador e historico.

## Requisitos
- Python 3.14
- Django 6.0.x

## Configuracao local
1. Criar/ativar ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias

```powershell
python -m pip install --upgrade pip
python -m pip install "Django>=6.0,<6.1"
```

3. Migrar base de dados

```powershell
python manage.py migrate
```

4. Criar superutilizador (opcional, para o admin)

```powershell
python manage.py createsuperuser
```

5. Iniciar servidor

```powershell
python manage.py runserver
```

## Funcionalidades
- Login, registo e logout
- Quizzes protegidos por autenticacao
- Resultados guardados por utilizador
- Pagina "Meus resultados"

## Admin
- Acede a `/admin/` para gerir quizzes, perguntas e opcoes.

## Producao
- Usar PostgreSQL em producao.
- Para migracao de dados, usar `dumpdata`/`loaddata` ou ferramentas equivalentes.
- Manter settings separados por ambiente.

## Testes
- Sem pytest configurado. Usa:

```powershell
python manage.py test
```
