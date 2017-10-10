#!/bin/sh
# my test program
nohup python /data/atm.py &

prog_exit()
{
    ps -ef| grep atm |grep -v grep |awk '{print $2}'|xargs kill -15
    
}

trap "prog_exit" 15

flag=1
while [ $flag -ne 0 ];do
    sleep 3;
    flag=`ps -ef| grep atm |grep -v grep | wc -l`
done;
