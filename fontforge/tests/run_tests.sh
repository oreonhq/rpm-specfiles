#!/bin/bash

cp /usr/share/fontforge/pixmaps/Cantarell-Regular.ttf .

echo "----------------------------------------------------------"
echo "Executing get-font-metadata.py on Cantarell-Regular.ttf =>"
/usr/bin/python3 get-font-metadata.py ./Cantarell-Regular.ttf

echo "----------------------------------------------------------"
echo "Executing generate-font.py on Cantarell-Regular.ttf =>"
/usr/bin/python3 generate-font.py ./Cantarell-Regular.ttf

echo "----------------------------------------------------------"
cp /usr/share/fontforge/pixmaps/Cantarell-Regular.ttf .
echo "Executing generate-sfd.pe on Cantarell-Regular.ttf =>"
/usr/bin/fontforge -script generate-sfd.pe ./Cantarell-Regular.ttf
rm Cantarell-Regular.ttf

echo "----------------------------------------------------------"
echo "Executing generate-ttf.pe on Cantarell-Regular.sfd =>"
/usr/bin/fontforge -script generate-ttf.pe ./Cantarell-Regular.sfd
echo "----------------------------------------------------------"

