# Selenium_proj

## Установка и настройка:

Установить python версией не ниже 3.6 ==> https://www.python.org/downloads/ далее, запустить файл предварительной настройки [presetting.py](https://github.com/mikibouns/selenium_proj/blob/master/presetting.py), для этого необходимо находиться в каталоге проекта (selenium_proj):
  + *Windows*  
     ```python presetting.py```
  + *Linux*  
     ```python3 presetting.py```   
     или  
     ```chmod +x presetting.py && ./presetting.py```  
  + *MacOS*  
     ```python3 presetting.py```  

### Активация виртуальной среды
Активировать виртуальную можно следующим способом, для этого необходимо находиться в текущем каталоге (selenium_proj):  
  + *Windows*  
      ```venv\Scripts\activate.bat```
      > возможно прийдется указать абсолютный путь в файлу `activate.bat`
  + *Linux*  
      ```. env/bin/activate```  
      или  
      ```source env/bin/activate```  
  + *MacOS*  
     ```. env/bin/activate```  
     или  
     ```source env/bin/activate```
> Деактивируется виртуальная среда командой `deactivate`

## Запуск:

> Следующие команды необходимо выполнять в [виртуальной среде](#Активация-виртуальной-среды). 

`python test_pytest_yandex.py` - запуск теста

### Пояснение к работе

В результате выполнения скрипта [test_pytest_yandex.py](https://github.com/mikibouns/selenium_proj/blob/master/test_pytest_yandex.py) в текущем каталоге будет создант файл `test.log` с результатами выполнения теста.

>Скрипт тестировался только на `ОС Windows 7 Professional x64` для веб-браузера `Google Chrome`

Используемые библиотеки и их зависимости:
+ selenium==3.141.0
+ requests==2.22.0
+ pytest==4.5.0
+ pytest-logger==0.5.0
+ Pillow==6.0.0

Используемое ПО:
+ ОС Windows 7
+ веб-браузера Google Chrome
+ Python 3.6


