#!/bin/bash
ps -ef | grep "[p]ython spar.py" | awk '{print $2}' | xargs kill
exit 0