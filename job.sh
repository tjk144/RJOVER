#!/bin/sh
echo "Please create/choose a .wav file in the file selection tool. By default the date and time will be placed before any name that you choose." 
filename=$(zenity --file-selection --save --confirm-overwrite);echo "Your filepath is: $filename"
flag="False"
removedate=$(zenity --entry --width=400 --title="Please enter 0 if no dates will be prefixed." --text="Enter a number to continue" )
if [ $removedate != "0" ]
then
	echo "Default dating will be applied"
else
	echo "No default dating will be applied"
	flag="True"
fi

days=$(zenity --entry --width=400 --title="How many days would you like to run for?" --text="Please insert an integer atleast 1")

for i in $(seq 1 1 $( printf "%.0f" $days )) 
do
	timeout 1m python3 TestV5.py "${filename}" "${flag}"
	echo "finished $i time at $(date)" 
	echo " "
done

