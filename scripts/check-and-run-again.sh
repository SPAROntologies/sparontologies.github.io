#!/bin/bash
CUR_DIR="${pwd}"
myv=`curl -s http://www.sparontologies.net`
if [ -z "$myv" ]; then # If the ping does not resolve then run the server again
    ps -ef | grep "python spar.py" | awk '{print $2}' | xargs kill
    cd /home/essepuntato/websites
    python spar.py 80 &
    cd $CUR_DIR
fi
