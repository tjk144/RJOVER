#/bin/sh
echo "This script assumes that the file you are editing is complex and has a variable called filename. This would be used for storing .txt files ."
filename=$(zenity --file-selection --save --confirm-overwrite);echo "Your filepath is: $filename"
sed -i "s/'filename'/filename/" $filename
loc=$(grep -n 'import time' $filename | cut -d: -f 1)
sed -i "${loc}i import numpy as np\nimport datetime" $filename

sed -i "s|main()|filename=sys.argv[1]\n    flag=sys.argv[2]\n    if flag== \"False\":\n        loc=np.zeros(len(filename));\n        for d in range(0,len(filename)):\n            loc[d]=filename.find(\"/\",d,len(filename));\n        indexslash=int(max(loc));\n        dtime=datetime.datetime.utcnow() #Collects the UTC time\n        filename=filename[:indexslash+1] +dtime.strftime(\"%Y%m%d%H%M%S\") +filename[indexslash+1:]; # Year,Month,Day,Hour,Minute,Second is 14 digits\n    main()|" $filename
