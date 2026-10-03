# api_yatube

Учебный REST API для постов, групп и комментариев Yatube. Исходный Django проект находится в `yatube_api/`. Используйте Python 3.9 и SQLite.

```powershell
py -3.9 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python yatube_api/manage.py migrate
.venv\Scripts\python yatube_api/manage.py runserver
```

Токен получается запросом `POST /api/v1/api-token-auth/`; посты доступны под `/api/v1/posts/`, группы под `/api/v1/groups/`. Для изменений поста или комментария нужен автор. `djoser` указан в зависимостях, так как он включён в настройки Django.

```powershell
.venv\Scripts\python -m pytest -q
```

Для `DJANGO_DEBUG=0` задайте переменные `DJANGO_SECRET_KEY` и `DJANGO_ALLOWED_HOSTS`. `.env.example` содержит только образцы значений; файл `.env` автоматически не загружается.
