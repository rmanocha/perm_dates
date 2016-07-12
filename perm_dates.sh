#!/bin/bash

output=$(python /home/rmanocha/perm_dates/perm_dates.py)
if [ -n "$output" ]; then
    echo $output | mail -s "perm dates for today" rmanocha@gmail.com
    echo "mail sent"
fi
