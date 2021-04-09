#/bin/sh
echo "This script assumes that the file you are editing has a real and imaginary variables labeled filename_real and filename_imag. This would be used for storing .wav files ."
filename=$(zenity --file-selection --save --confirm-overwrite);echo "Your filepath is: $filename"
sed -i "s/'filename_imag'/filename_imag/" $filename
sed -i "s/'filename_real'/filename_real/" $filename
loc=$(grep -n 'import time' $filename | cut -d: -f 1)
sed -i "${loc}i import numpy as np\nimport datetime" $filename

sed -i "s|main()|filename=sys.argv[1]\n    flag=sys.argv[2]\n    if flag== \"False\":\n        loc=np.zeros(len(filename));\n        for d in range(0,len(filename)):\n            loc[d]=filename.find(\"/\",d,len(filename));\n        indexslash=int(max(loc));\n        dtime=datetime.datetime.utcnow() #Collects the UTC time\n        filename=filename[:indexslash+1] +dtime.strftime(\"%Y%m%d%H%M%S\") +filename[indexslash+1:]; # Year,Month,Day,Hour,Minute,Second is 14 digits\n    ind=filename.find(\".\")\n    filename_real=filename[:ind] + \"_real\"+filename[ind:];\n    filename_imag=filename[:ind] + \"_imag\"+filename[ind:];\n    main()|" $filename
