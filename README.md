# terminalfailbot

## .env file

### CTOKEN

Consumer Key API token


### CSECRET

Consumer Key API token secret

### ATOKEN

Access token


### ASECRET

Access token secret


## install

```
mkdir repos
cd repos
git clone https://github.com/antalmiklos/terminalfailbot

pip3 install -r terminalfailbot/requirements.txt

# ZSH
echo 'function command_not_found_handler() {python3 $HOME/repos/terminalfailbot/terminalfail.py "$@"}' >> ~/.zshrc

# BASH
echo 'function command_not_found_handle() {python3 $HOME/repos/terminalfailbot/terminalfail.py "$@"}' >> ~/.bashrc

```


## zshrc

function command_not_found_handler() {python3 $HOME/repos/terminalfailbot/terminalfail.py "$@"}
