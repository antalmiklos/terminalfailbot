if [[ $SHELL == '/usr/bin/zsh' ]];
then
    LASTCOMMAND=''

    function preexec () {
        LASTCOMMAND="$1"
    }
    function command_not_found_handler() {
        python3 $HOME/repos/terminalfailbot/app.py "${LASTCOMMAND};127"
    }
    function precmd() {
        lastcode=$?
        if [[ $lastcode -ne 0 ]];
            then
                python3 $HOME/repos/terminalfailbot/app.py "${LASTCOMMAND};${lastcode}"
            fi
        }
fi