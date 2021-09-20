# Pokemon Map
Урок № 4 модуля "Знакомство с Django: ORM" от Devman.

## Описание

Сайт с картой покемонов.


### Особенности

- имеет CRUD-функционал для работы с БД,
- отражает покемонов на карте города Москвы,
- предоставляет справочную информацию по каждой разновидности покемона.

### Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО),
* Фикстура.

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [python-dotenv](https://pypi.org/project/python-dotenv/).

#### Параметры проекта

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DEBUG`| Режим отладки |`True`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|

### Установка

- Клонирование проекта,
- создание каталога виртуального окружения (ВО)*,
- связывание каталогов ВО и проекта,
- установка зависимостей:
```bash
git clone https://github.com/Padking/pokemon-map.git
cd pokemon-map
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt

```

- Применение миграций к проекту,
- применение фикстуры к проекту,
- создание суперпользователя в интерактивном режиме**,
- запуск сайта:
```bash

python manage.py migrate
python manage.py runserver
```


\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

\** для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)


### Пример запуска

```
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 20, 2021 - 15:24:19
Django version 3.1.13, using settings 'pogomap.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
