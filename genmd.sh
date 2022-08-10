#!/bin/sh
# ./genmd.sh <file name>
# this script sucks at the moment
read -p 'Page name: ' pagename
pagename=content/$(echo $pagename | tr ' ' '-').md

echo '---' >> $pagename
echo 'aka: []' >> $pagename
echo 'artists: []' >> $pagename
echo 'producers: []' >> $pagename
echo 'tags: []' >> $pagename
echo "file_name: $(exiftool "$1" -a -s -s -s -FileName)" >> $pagename
echo "file_title: $(exiftool "$1" -a -s -s -s -Title)" >> $pagename
echo "file_comment: $(exiftool "$1" -a -s -s -s -Comment)" >> $pagename
echo 'recorded: ' >> $pagename
echo 'leaked: ' >> $pagename
echo "length: $(exiftool "$1" -a -s -s -s -Duration)" >> $pagename
md5=($(md5sum "$1"))
echo "md5: $md5" >> $pagename
echo 'mirrors: []' >> $pagename
echo '---' >> $pagename
