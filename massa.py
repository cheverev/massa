import urllib
import requests
import json
import socket
import time

host_ip = socket.gethostbyname(socket.getfqdn())

telegram_chat = "****"
bot_token = "*****"
send_text =  f"active_rolls = 0 on {host_ip} hosts"
massa_addr = "****"
send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={telegram_chat}&text={send_text}"


url = f"http://127.0.0.1:33033/api/v1/addresses_info?addrs[0]={massa_addr}"
res = urllib.request.urlopen(url).read()
js = json.loads(res)
rolls = js.get(massa_addr).get("active_rolls")

while True:
    if rolls == 0:
        requests.get(send_url)
    else:
        time.sleep(60)
