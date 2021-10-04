LASTCOMMAND=''

function preexec () {
    LASTCOMMAND="$1"
}
function command_not_found_handler() {
    python3 $HOME/repos/terminalfailbot/app.py "${LASTCOMMAND};127"
}
function precmd() {
    lastcode=$?
    cmd=${history[$HISTCMD]}
    echo ${cmd}
    if [[ $lastcode -ne 0 ]];
    then
        python3 $HOME/repos/terminalfailbot/app.py "${LASTCOMMAND};${lastcode}"
    fi
}
