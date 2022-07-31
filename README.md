# API для проекта Yatube

## 1. [Описание](#1)
## 2. [Команды для запуска](#2)
## 3. [Техническая информация](#5)
## 4. [Об авторе](#6)

---
## 1. Описание <a id=1></a>

Проект API для социальной сети [Yatube](https://github.com/BERCUT38/hw05_final).  
Позволяет создавать, читать, изменять и удалять свои посты, а так же читать чужие посты и подписываться на их авторов посредством API-запросов.  
Для неавторизованных пользователей API доступен только для чтения.

---
## 2. Команды для запуска <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/BERCUT38/api_final_yatube.git
SSH: git clone git@github.com:BERCUT38/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```

Теперь доступность проекта можно проверить по адресу [http://localhost/admin/](http://localhost/admin/)

---
## 3. Техническая информация <a id=5></a>

Стек технологий: Python 3, Django, Django Rest, simple JWT.

---
## 4. Об авторе <a id=6></a>

Будник Сергей Александрович  
Python-разработчик (Backend)  
Россия, г. Краснодар  
E-mail: bercut38877@yandex.ru  
Telegram: @Bercut38
