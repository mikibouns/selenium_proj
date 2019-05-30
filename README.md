# Selenium_proj

## Установка и настройка:

Установить python версией не ниже 3.6 ==> https://www.python.org/downloads/ далее, запустить файл установки виртуальной среды [presetting.py](https://github.com/mikibouns/selenium_proj/blob/master/presetting.py), для этого необходимо находиться в каталоге проекта (selenium_proj):
  + *Windows*  
     ```python install_env.py```
  + *Linux*  
     ```python3 install_env.py```   
     или  
     ```chmod +x install_env.py && ./install_env.py```  
  + *MacOS*  
     ```python3 install_env.py```  

### Активация виртуальной среды
Активировать виртуальную можно следующим способом, для этого необходимо находиться в текущем (selenium_proj):  
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

### Пояснение к заданию

> Следующие команды необходимо выполнять в [виртуальной среде](#Активация-виртуальной-среды). 

`python test_pytest_yandex.py` - запуск теста

В результате выполнения скрипта [test_pytest_yandex.py](https://github.com/mikibouns/selenium_proj/blob/master/test_pytest_yandex.py) в текущем каталоге будет создант файл `test.log` с результатами выполнения теста.

>Скрипт был написан для веб-браузера `Google Chrome` и `OC Windows`, тестировался только на `ОС Windows 7 Professional x64`
