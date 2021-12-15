#!/bin/sh

# script to resize and crop

echo "Please wait while all the spaces are removed from filenames"
for f in *; do mv "$f" `echo $f | tr ' ' '_'`; done

echo "croping Files, Please be patiant"

dir="./"
resume=resume
#orig=_orig
#cd "$dir$orig"
for k in `ls *.jpg`
do	
	h=`identify -format "%h" $k`
	w=`identify -format "%w" $k`
	echo "$k, w:$w, h:$h"
	#If landscape
	if [ $w -ge $h ]
		then
	   	 convert $k -crop 3158x4500+0+90  "$dir/$k"
#	   	 convert $k -crop 2352x3348-110-80  "$dir/$k"
	     #echo "landscape"
		else
		 convert $k -crop 3158x4500+0+90 "$dir/$k"
#	   	 convert $k -crop 2352x3348-110-80  "$dir/$k"
	     #echo "portrait"
	fi
	
done

