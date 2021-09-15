# massa
Simple python script to check active rolls and send notification in telegram when activ rolls are 0

# Install dependencies
```
apt update && apt install python3 python3-pip -y && pip3 install requests
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
1. Run wia systemd
```
sudo tee <<EOF >/dev/null /etc/systemd/system/checkmassa.service
[Unit]
Description=Check massa rolls
After=network-online.target
[Service]
User=$USER
Restart=always
RestartSec=3
ExecStart=$(which python3) $HOME/massa.py
[Install]
WantedBy=multi-user.target
EOF

udo systemctl enable checkmassa
sudo systemctl daemon-reload
sudo systemctl restart checkmassa
```
2. Run wia tmux
install tmux
- apt instlall tmux
- tmux new -s massa
- $(which python3) $HOME/massa.py
- Press ```Ctrl+b d``` do deatach tmux
- to atach ```tmux attach -t massa```
