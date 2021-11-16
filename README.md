# massa
Simple python script to check final balance and byt rolls

# Install dependencies
```
apt update && apt install python3 python3-pip -y && pip3 install requests jsonrpcclient 
```
# Settings
first edit massa.py and enter your data
```
telegram_chat = "" 
bot_token = ""
send_text =  ""
massa_addr = ""
```
Example
```
telegram_chat = "-5251235214"
bot_token = "1916857502:AAFcWcuyuasbbastIn_-8sM_7SwbJo9T0"
send_text =  "Activ rolls is 0 check your massa node"
massa_addr = "2oNMsFA82Jqb8Bktoc9rVtQMcdmgB8w3tRGUWdZkyWJdTETSnD"
```
# Run script
1. Run wia tmux
install tmux
- apt instlall tmux
- tmux new -s massa
- $(which python3) $HOME/massa.py
- Press ```Ctrl+b d``` do deatach tmux
- to atach ```tmux attach -t massa```
