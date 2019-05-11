#!/bin/bash
myv=`curl -s http://www.sparontologies.net`

if [[ -z "$myv" ]] || [[ $myv = "Traceback"*  ]]; then
    /etc/init.d/lighttpd stop
    pkill -f "python3 /var/www/"
    /etc/init.d/lighttpd start
    exit 0
fi

exit 1
