import requests
from .models import TeleSettings


# token = '5296916169:AAHSHwvGNYNT2ij7PankmqFF8YeLUK9rNUE'
# chat_id = '-622600081'
# text = 'Test_2'

def sendTelegram():
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
        })
