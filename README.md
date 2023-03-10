# pynchon

Проект для фанатов Пинчона

## Что внутри?

1. User – приложение для управления пользователями;
2. Wiki – приложение для управления книгами, главами и комментариями;
3. Core – приложение для хранения базовых моделей;
4. Service – для хранения и создания вспомогательных функций;

## Полезные команды

- make requirements - установка всех зависимостей
- make migrate - выполнение миграции БД
- make seed - загрузка тестовых данных

### Доступ в админ панель

После выполнения команды сидирования данных можно зайти под пользователем:

```
python pynchon_wiki/manage.py seed
```

| username  |   password   |
|:----------: |:------------:|
| admin     |    admin     |

## Как запустить проект локально с помощью venv:

1. Клонируем репозиторий;
2. Создать и активировать виртуальное окружение:
    ```
   python3.7 -m venv venv
   . venv/bin/activate
   python -m pip install --upgrade pip
    ```    

3. Установить зависимости из файла requirements.txt:

    ```
   pip install -r pynchon_wiki/requirements.txt
    ```   

4. Выполнить миграции и залить тестовые данные:

    ```
   python pynchon_wiki/manage.py migrate
   python pynchon_wiki/manage.py seed
    ```       

5. Запустить проект:

    ```
    python pynchon_wiki/manage.py runserver
    ```

## Как запустить проект с помощью docker:

1. В файле nginx.conf указать список ваших доменов;
2. Заполнить .env файл по аналогии с .env.example, указав валидные данные;
3. На сервер скопировать из папки infra .env, docker-compose-server.yml, nginx.conf
4. Поднять контейнер
    ```
   docker compose up -d 
    ```
5. В Django контейнере выполнить команды:
    ```
   make migrate
   make seed
    ```