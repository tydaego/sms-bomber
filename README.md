<h1 align="center">SMS Bomber, v0.2</h1>
<h4 align="center">SMS Bomber - это программа, позволяющая отправлять SMS для проверки защиты от спам-рассылки или "Just For Fun".</h4>

## Предупреждения:
- Для работы программы необходим **доступ в Интернет**,
- Убедитесь, что вы используете последнюю версию **SMS Bomber**,
- Убедитесь, что вы используете библиотеку **requests**
- Убедитесь, что вы используете **Python 3.x**,
- Программа **не собирает и не отправляет персональные данные третьим лицам!** 

## Особенности:
- Поддерживаются номера РФ, Украины и Беларуси.
- Возможность отправки **по таймеру**.

## Использование:
**Windows:**
- Скачайте **.zip-файл** по **[ссылке](https://github.com/MatroCholo/sms-bomber/releases)**
- Установите **Python 3.x** и **pip**,
- Используя **pip**, установите **requests**,
- Запустите **sms-bomber.py**

**Linux:**
- Установите **Python 3.x**, **pip** и **git** в соответствии с вашим дистрибутивом,
- Используя **pip**, установите **requests**,
- git clone **https://github.com/MatroCholo/sms-bomber**
- cd **sms-bomber/**
- python **sms-bomber.py**

## Ручная конвертация .py в .exe:
- Нажмите **Windows + R**, введите **cmd** и нажмите **Enter**,
- В открывшемся окне введите **pip install pyinstaller requests**,
- После установки введите:
**pyinstaller C:\Directory\file.py --onefile --icon C:\Directory\file.icon**, где
- - **pyinstaller** - **команда конвертирования**,
- - **C:\Directory\file.py** - **путь к файлу с расширением .py**,
- - **--onefile** - **конвертация в один файл**,
- - **--icon C:\Directory\file.icon** - **добавление иконки и путь к ней (необязательно)**.

## Поддерживаемые версии:

| Версия       | Поддержка          |
| -------------| ------------------ |
| v0.3         | Скоро              |
| v0.2         | :white_check_mark: |
| v0.1         | :x:                |

## Обратная связь:
- ВК: https://vk.com/matrocholo
- Telegram: https://t.me/MatroCholo
