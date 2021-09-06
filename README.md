# Yandex Cloud billing

Примитивный подсчет затрат на Яндекс Облако из ежедневной выгрузки затрат в
бакет Yandex Object Storage.

Ежедневно сумма затрат за сутки вносится в таблицу Google Sheet, при
достижении порога в 20 тысяч рублей высылается уведомление в Telegram, после
чего счетчик обнуляется.

##1. Быстрый старт
1.1. Заполните файл *.env* своими данными.

1.2. Положите в папку с проектом файл с кредами для Google Sheet, переименуйте
его в *gsheet_cred.json*

1.3. В папке с проектом запустите команду
```shell
docker-compose up -d
```

Используемые переменные окружения:

- AWS_ACCESS_KEY_ID_BILLING - access key для Yandex Object Storage.
- AWS_SECRET_ACCESS_KEY_BILLING - secret key для Yandex Object Storage.
- BUCKET - имя бакета где хранятся выгрузки.
- TG_BOT_API_KEY - API key Telegram бота для отправки уведомлений.
- TG_BOT_CHAT_ID - ID чата, куда бот будет слать уведомления, необходимо
добавить бота в чат.
- SHEET_ID - ID таблицы Google Sheet