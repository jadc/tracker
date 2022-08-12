#!/bin/sh
# ./genmd.sh <file name>
# this script sucks at the moment
read -p 'Page name: ' pagename
file=content/$(echo $pagename | tr ' ' '-').md

echo '---' >> $file
echo "title: $pagename" >> $file
echo 'aka: []' >> $file
echo 'artists: []' >> $file
echo 'producers: []' >> $file
echo 'tags: []' >> $file
echo "file_name: $(exiftool "$1" -a -s -s -s -FileName)" >> $file
echo "file_title: $(exiftool "$1" -a -s -s -s -Title)" >> $file
echo "file_comment: $(exiftool "$1" -a -s -s -s -Comment)" >> $file
echo 'recorded: ' >> $file
echo 'leaked: ' >> $file
echo "length: $(exiftool "$1" -a -s -s -s -Duration)" >> $file
md5=($(md5sum "$1"))
echo "md5: $md5" >> $file
echo 'mirrors: []' >> $file
echo '---' >> $file
