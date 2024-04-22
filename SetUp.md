## Развёртывание проекта:
+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```shell script
python -m venv venv
```

```shell script
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```shell script
python -m pip install --upgrade pip
```

```shell script
pip install -r backend/requirements.txt
```

+ Установите [Docker compose](https://www.docker.com/) на свой компьютер.

+ Запустите проект через docker-compose:
```shell script
docker compose -f docker-compose.production.yml up --build -d
```

+ Выполнить миграции:
```shell script
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```

+ Запустите проект Python:
```shell script
pythin manage.py runserver
```