# api-amo
API AMO
Скрипты написаны с целью интеграции к амо срм, получения данных и отправки на почту.

## newreg.py
скрипт первичной регистрации к амо. Используется библиотека "AmoCRM python API. V2"
Необходимо будет внести ряд параметров (согласно инструкции к библиотеке). Все параметры копируются из интеграции в амо.
Библиотека создает два .txt файла access_token и refresh_token

## ref_reg.py
access_token действителен в течении суток, для создания нового требутся refresh_token. Данный скрипт направлен на создание нового access_token.
Скрипт получает новые данные из API и перезаписывает в txt

## mail.py
Отправляет письмо с вложением

## getUser.py
Делаю request запрос на получение данных контакт

## createExcel.py
Создаю excel, куда записываю данные по лидам и связанным контактам

## getLeadExcel.py
Записываю данные в эксель

## getInfoLead.py
Запрос на получении информации о конкретном лиде


