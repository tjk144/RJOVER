#!/bin/sh
echo "Please choose the filename for the python script that will be used for the data collection. Make sure that this script has already been ran through editor.sh to make sure that the looping code has been implemented properly."
file=$(zenity --file-selection --confirm-overwrite)
echo "Your file you will be using for collection is: $file"
echo "Please create/choose a .dat file in the file selection tool. By default the date and time will be placed before any name that you choose." 

filename=$(zenity --file-selection --save --confirm-overwrite)
echo "Your filepath is: $filename"
flag="False"
removedate=$(zenity --entry --width=400 --title="Please enter 0 if no dates will be prefixed." --text="Enter a number to continue" )
if [ $removedate != "0" ]
then
	echo "Default dating will be applied"
else
	echo "No default dating will be applied"
	flag="True"
fi

days=$(zenity --entry --width=400 --title="How many half-days would you like to run for?" --text="Please insert an integer atleast 1")

for i in $(seq 1 1 $( printf "%.0f" $days )) 
do
	timeout 60s python3 $file "${filename}" "${flag}"
	echo "finished $i time at $(date)" 
	echo " "
done

