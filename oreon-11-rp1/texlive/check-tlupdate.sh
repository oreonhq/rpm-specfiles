#!/bin/bash
# Probably should redo this in python ... but lazy
# Copyright 2020 Tom Callaway <spot@fedoraproject.org>

# MIRROR="http://ctan.math.illinois.edu/systems/texlive/tlnet/archive/"
MIRROR="https://mirror.math.princeton.edu/pub/CTAN/systems/texlive/tlnet/archive/"

function validate_url(){
	if [[ `wget -S --spider $1  2>&1 | grep 'HTTP/1.1 200 OK'` ]]; then 
		echo "true";
	else
		echo "false";
	fi
}

for i in `grep "^%package" texlive.spec | cut -d " " -f 2-`; do 
	PACKAGENAME="$i"; 
	COMPONENTNAME=`echo $i | sed 's|-doc$|.doc|g'`; 
	# Some of the older versions have trailing .NNN.NNN values. Strip em.
	CURRVERSION=`grep -A10 "%package $i$" texlive.spec | grep -m 1 "^Version:" | cut -d " " -f 2- | cut -d "." -f 1 | sed 's|^svn|r|g'`; 
	# printf "$COMPONENTNAME "
	# echo "$COMPONENTNAME @ $CURRVERSION";
	MY_URL=`echo $MIRROR$COMPONENTNAME.$CURRVERSION.tar.xz`
	# echo $MY_URL
	OUTPUT=`validate_url $MY_URL`
	# echo $OUTPUT
	if $OUTPUT; then
		# echo "[$PACKAGENAME] same as upstream"
		continue
	else
		echo "$PACKAGENAME"
	fi
done
