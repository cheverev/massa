from jsonrpcclient import request
import requests
import os
import time

address = "iPwUxhRdcZB16FksEv5K8Xe2LFTWDMtAYwdjQZLMCEAWEvbCr"
res = requests.post("http://127.0.0.1:33035/", json=request("get_addresses",params=[[address]]))
massa = int(float(res.json().get("result")[0].get("balance").get("final_balance")))

while True:
    if(massa // 100 > 0 ):
        os.system("date >> /root/massa.log")
        count = massa // 100
        os.system(f"cd /root/massa/massa-client && /root/massa/target/release/massa-client --wallet wallet.dat buy_rolls {address} {count} 0 >> /root/massa.log")
        time.sleep(60)
    else:
        os.system("date >> /root/massa.log")
        time.sleep(60)
