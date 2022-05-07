from jsonrpcclient import request
import requests
import os
import time

address = "iPwUxhRdcZB16FksEv5K8Xe2LFTWDMtAYwdjQZLMCEAWEvbCr"

while True:
    try:https://github.com/cheverev/massa/blob/main/massa.py
        res = requests.post("http://127.0.0.1:33035/", json=request("get_addresses",params=[[address]]))
        ActiveRolls = int(res.json().get("result")[0].get("rolls").get("active_rolls"))
        CandidateRolls = int(res.json().get("result")[0].get("rolls").get("candidate_rolls"))
        if(ActiveRolls >= 1 or CandidateRolls == 1):
            break
        os.system("date >> /root/massa.log")
        os.system(f"cd /root/massa/massa-client && /root/massa/target/release/massa-client --wallet wallet.dat buy_rolls {address} 1 0 >> /root/massa.log")
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(300)
