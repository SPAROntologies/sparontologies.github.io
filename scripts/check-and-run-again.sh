#!/bin/bash
CUR_DIR="${pwd}"
myv=`curl -s http://www.sparontologies.net`
if [[ -z "$myv" ]] || [[ $myv = "Traceback"*  ]]; then # If the ping does not resolve then run the server again
    ps -ef | grep "python spar.py" | awk '{print $2}' | xargs kill
    cd /home/essepuntato/websites
    nohup python spar.py 80 &
    date >> log.txt
    cd $CUR_DIR
fi