#!/bin/bash
myv=`curl -s http://www.sparontologies.net`

if [[ -z "$myv" ]] || [[ $myv = "Traceback"*  ]]; then
    /etc/init.d/lighttpd restart
    exit 0
fi

exit 1
