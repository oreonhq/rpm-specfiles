#!/usr/bin/bash
set -x
set -e

ORIG_XML=./share/wallpapoz/glade/wallpapoz.glade
NEWTOPDIR=wallpapoz-0.6.2-builder
DIR_XML=$(dirname $ORIG_XML)
BASE_XML=$(basename $ORIG_XML)

mkdir -p $NEWTOPDIR/$DIR_XML || true

cat ./src/wallpapoz | sed -n -e '\@gtk.glade.XML@s|^.*"\(.*\)".*$|\1|p' | while read item
do
	SPLIT_ORIG_XML=${DIR_XML}/wallpapoz-old-${item}.glade
	NEW_BUILDER_XML=${DIR_XML}/wallpapoz-builder-${item}.glade

	> $NEWTOPDIR/$SPLIT_ORIG_XML
	head -n 5 $ORIG_XML >> $NEWTOPDIR/$SPLIT_ORIG_XML
	cat $ORIG_XML | sed -n -e "\@^<widget class.*"${item}"@,\@^</widget>\$@p" >> $NEWTOPDIR/$SPLIT_ORIG_XML
	echo >> $NEWTOPDIR/$SPLIT_ORIG_XML
	tail -n -1 $ORIG_XML >> $NEWTOPDIR/$SPLIT_ORIG_XML

	gtk-builder-convert $NEWTOPDIR/$SPLIT_ORIG_XML $NEWTOPDIR/$NEW_BUILDER_XML
	sed -i $NEWTOPDIR/$NEW_BUILDER_XML \
		-e "\@has_resize_grip@d" \
		-e "\@has_separator@d"
done
