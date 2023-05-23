import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '5876951218:AAHjecSKkQPJdF-dW5VUGIsQXE3i1C03dBk'

offset: int = -2
timeout: int = 50
update: dict



def do_something() -> None:
    print('был апдейт')

while True:
    print('wait')
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'время между запросами к Telegram Bot API: {end_time - start_time}')