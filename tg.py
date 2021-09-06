import requests
import os


def send_tg_message(bot_message):
    bot_token = os.environ['TG_BOT_API_KEY']
    bot_chat_id = os.environ['TG_BOT_CHAT_ID']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + \
                '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

