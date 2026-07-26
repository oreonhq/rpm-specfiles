#!/bin/sh

#TAG=HEAD
TAG=OPENBSD_7_6
SERVER=anoncvs4.usa.openbsd.org

PATH=/usr/bin
CWD=$(pwd)

if ! grep "${SERVER}" ~/.ssh/config ; then
    echo "*** Configuration block for ${SERVER} not found in ~/.ssh/config" >&2
    echo "*** Make sure this block exists in ~/.ssh/config:" >&2
    echo >&2
    echo "Host ${SERVER}" >&2
    echo "    Port 2022" >&2
    exit 1
fi

CVS_RSH=ssh ; export CVS_RSH

rm -rf calendar calendar-${VER}
mkdir calendar
cvs -d :ext:anoncvs@${SERVER}:/cvs co -d calendar -r ${TAG} src/usr.bin/calendar

cd calendar
VER="$(cvs status calendar.c | grep 'Working revision:' | awk '{ print $3; }')"
SNAPSHOT="$(date +%Y%m%d)cvs"
cd ..
find calendar -type d -name CVS | xargs rm -rf

mv calendar calendar-${VER}-${SNAPSHOT}
tar -cvf - calendar-${VER}-${SNAPSHOT} | gzip -9c > calendar-${VER}-${SNAPSHOT}.tar.gz
rm -rf calendar-${VER}-${SNAPSHOT}
