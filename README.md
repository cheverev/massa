# massa
Simple python script to check final balance and buy rolls

# Install dependencies
```
apt update && apt install python3 python3-pip -y && pip3 install requests jsonrpcclient 
```
# Settings
enter your address in massa.py 

'''
address = "iPwUxhRdcZB16FksEv5K8Xe2LFTWDMtAYwdjQZLMCEAWEvbCr"
'''

# Run script
1. Run wia tmux
install tmux
- apt instlall tmux
- tmux new -s massa
- $(which python3) $HOME/massa.py
- Press ```Ctrl+b d``` do deatach tmux
- to atach ```tmux attach -t massa```
