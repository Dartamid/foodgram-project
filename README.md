![Foodrgram](https://github.com/SergePogorelov/foodgram-project/workflows/Foodrgram/badge.svg)

### «Продуктовый помощник».
Это онлайн-сервис, где пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Демо: http://dartamid.xyz/

## Описание проекта и функционала

### Главная страница

Содержимое главной страницы — список рецептов, отсортированных по дате публикации (от новых к старым).

### Страница рецепта

На странице — полное описание рецепта, возможность добавить рецепт в избранное и в список покупок, возможность подписаться на автора рецепта.

### Страница пользователя

На странице — имя пользователя, все рецепты, опубликованные пользователем и возможность подписаться на пользователя.

### Подписка на авторов

Подписка на публикации доступна только авторизованному пользователю. Страница подписок доступна только владельцу.

### Сценарий поведения пользователя:

- Пользователь переходит на страницу другого пользователя или на страницу рецепта и подписывается на публикации автора кликом по кнопке `Подписаться на автора`.
- Пользователь переходит на страницу «Мои подписки» и просматривает список рецептов, опубликованных теми авторами, на которых он подписался. Сортировка записей — по дате публикации (от новых к старым).
- При необходимости пользователь может отказаться от подписки на автора: переходит на страницу автора или на страницу его рецепта и нажимает `Отписаться от автора`.

### Список избранного
Работа со списком избранного доступна **только авторизованному** пользователю. Список избранного может просматривать **только его владелец**.
**Сценарий поведения пользователя:**

- Пользователь отмечает один или несколько рецептов кликом по кнопке `Добавить в избранное`.
- Пользователь переходит на страницу `«Список избранного»` и просматривает персональный список избранных рецептов.
- При необходимости пользователь может `Удалить` рецепт из избранного.

### Список покупок
Работа со списком покупок доступна **авторизованным и не авторизованным** пользователям. 
Список покупок может просматривать **только его владелец**.
**Сценарий поведения пользователя:**

- Пользователь отмечает один или несколько рецептов кликом по кнопке `Добавить в покупки`.
- Пользователь переходит на страницу `Список покупок`, там доступны все добавленные в список рецепты. Пользователь нажимает кнопку `Скачать` список и получает файл с суммированным перечнем и количеством необходимых ингредиентов для всех рецептов, сохранённых в `«Списке покупок»`.
- При необходимости пользователь может удалить рецепт из списка покупок.

Список покупок скачивается в формате PDF.
При скачивании списка покупок ингредиенты в результирующем суммируются 
`если в двух рецептах есть сахар (в одном рецепте 5 г, в другом — 10 г), то в списке будет один пункт: Сахар — 15 г.`

### Фильтрация по тегам
При нажатии на название тега выводится список рецептов, отмеченных этим тегом. Фильтрация может проводится по нескольким тегам в комбинации «или»: если выбраны несколько тегов — на странице будут показаны рецепты, которые отмечены хотя бы одним из этих тегов.
При фильтрации на странице пользователя фильтруются только рецепты выбранного пользователя. 
При фильтрации на странице избранного фильтруются только избранные рецепты. 


### Регистрация и авторизация
В проекте доступна система регистрации и авторизации пользователей. 
Обязательные поля для пользователя:

    Логин
    Пароль
    Email

### Что могут делать неавторизованные пользователи

- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл с количеством необходимых ингредиентов для рецептов из списка покупок.

### Что могут делать авторизованные пользователи

- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Восстанавливать свой пароль.
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять/удалять чужие рецепты, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл с количеством необходимых ингредиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.
    

## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.


### Запуск проекта (на примере Linux)

Перед тем, как начать: если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

- Создайте на своем компютере папку проекта foodgram `mkdir foodgram` и перейдите в нее `cd foodgram`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/SergePogorelov/foodgram .`
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения:
```
SECRET_KEY = #секретный ключ Django
DEBUG=1
```
- Установите зависимости `pip install -r requirements.txt`
- Накатите миграции `python manage.py migrate`
- Создайте суперпользователя Django `python manage.py createsuperuser --username admin --email 'admin@example.com'`
- Запустите сервер разработки Django `python manage.py runserver`

### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop) 
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск docker-compose
- Добавьте в файл `.env` переменные окружения для работы с базой данных:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
- Запустите docker-compose командой `sudo docker-compose up -d` 
- Накатите миграции `sudo docker-compose exec web python manage.py migrate`
- Соберите статику командой `sudo docker-compose exec web python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec web python manage.py createsuperuser --username admin --email 'admin@yamdb.com'`

## Деплой на удаленный сервер
Для запуска проекта на удаленном сервере необходимо:
- в файле `.env` поменять настройки `DEBUG=0`
- скопировать на сервер файлы `docker-compose.yaml`, `.env` и папку `nginx` командами:
```
scp docker-compose.yaml  {user}@{server-ip}:
scp .env {user}@{server-ip}:
scp -r nginx/ {user}@{server-ip}:

```
- запустить на сервере контейнеры командой `sudo docker-compose up`

## CI/CD
### Для автоматического деплоя на сервер необходимо:
- создать переменные окружения в разделе `secrets` настроек текущего репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на стандарты `PEP8`.
2. Сборка и публикация образа на `Docker Hub`.
3. Автоматический деплой.
4. Отправка уведомления в персональный чат.

## В разработке использованы

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Sorl-thumbnail](https://pypi.org/project/sorl-thumbnail/)
- [WeasyPrint](https://weasyprint.org/) 
- [Yandex Cloud](https://cloud.yandex.ru/)
- [PostgreSQL](https://www.postgresql.org/)
- [Dokcer](https://www.docker.com/)
- [Gunicorn](https://gunicorn.org/)
- [Nginx](https://nginx.org/)
- [GitHub Actions](https://github.com/features/actions)
