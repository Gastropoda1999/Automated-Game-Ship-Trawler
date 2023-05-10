import subprocess
import requests

token = 'c2mYbYkMhCMm7ymTlRJQdqZinCCxJS8kZ3sL4uIqqVy'   #line token

filename = 'code_part.py'
while True:
    p = subprocess.Popen('python '+filename, shell=True).wait()

    if p != 0:
        payload = {'message' : '''
Bot Error ❗❗❗ 
Restarting...'''}
        r = requests.post('https://notify-api.line.me/api/notify'
            , headers={'Authorization' : 'Bearer {}'.format(token)}
            , params = payload)
        continue
    else:
        break