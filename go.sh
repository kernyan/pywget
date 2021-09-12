#! /bin/bash

./pywget.py > out.html

if [ -f "index.html" ];
then
  echo "file exist"
  rm "index.html"
fi

wget "neverssl.com"
DIFF=$(diff out.html index.html)
if [ "$DIFF" == "" ];
then
  echo "pywget and wget on neverssl.com pass"
fi
