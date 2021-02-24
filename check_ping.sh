#!/bin/bash
x=0
y=0
for i in {1..15}
do
   ping -c 3 -i 0.1 -W 1 192.168.1.$i
   if [ $? -eq 0 ];then
      echo "192.168.1."$i"ping通了"
      let x++
   else
      echo "192.168.1."$i"没ping通"
      let y++
   fi
done
echo $x"台ping通了",$y"台没有ping通"
