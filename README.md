# Pokemon Map
Урок № 4 модуля "Знакомство с Django: ORM" от Devman.

## Описание

Сайт с картой покемонов.


### Особенности

- имеет CRUD-функционал для работы с БД,
- отражает покемонов на карте города Москвы,
- предоставляет справочную информацию по каждой разновидности покемона.

### Карта покемонов

![screenshot](https://github.com/Padking/pokemon-map/blob/master/screenshots/pokemons_map.png)

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
- применение фикстуры:
```bash
python manage.py migrate
python manage.py loaddata db_data.json
```

- Создание суперпользователя в интерактивном режиме**,
- добавление картинок покемонов через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) из [каталога](https://github.com/Padking/pokemon-map/tree/master/pokemons_images),
- запуск сайта:
```bash
python manage.py createsuperuser
python manage.py runserver
```


\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

\** для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
