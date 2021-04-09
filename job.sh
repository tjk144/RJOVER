#!/bin/sh
echo "Insert desired filename and filepath below. It must start from where this script is located (By default the date and time will be placed before any name chosen, to disable this enter 0):"
read filename
echo "The filename you chose is:$filename"
flag="False"

if [ $filename != "0" ]
then
	echo "Filename accepted"
else
	echo "No default dating will be applied"
	echo "Insert desired filename and file path below. It must start from where this is located:"
	flag="True"
	read filename
	echo "Filename accepted"
fi

echo "How many days would you like to run for? Please insert an integer atleast 1 below"
read days

for i in $(seq 1 1 $( printf "%.0f" $days )) 
do
	timeout 24h python3 V3.py "${filename}" "${flag}"
	echo "finished $i times"
done

