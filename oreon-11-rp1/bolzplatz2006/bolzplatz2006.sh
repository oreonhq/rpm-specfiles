#!/bin/sh
# startscript for bolzplatz2006
#
# written by oc2pus and Hans de Goede <hdegoede@redhat.com>
#
# Changelog:
# 18.06.2007 initial version (oc2pus)
# 08.09.2007 Don't symlink entire data dir, instead copy over a few dirs which
#   need to be writable and symlink the rest, make the script work on systems
#   which have lib64 dirs (Hans).

# activate for debugging
#set -x

# exit on error
set -e

# base settings
myShareDir=/usr/share/bolzplatz2006
myHomeDir=~/.bolzplatz2006

. $myShareDir/bolzplatz2006-functions.sh

echo ""
echo "starting bolzplatz2006 ..."

# creates a local working directory in user-home
createLocalDir

cd $myHomeDir

# bolzplatz2006 does not work with gcj
JAVA_HOME=/usr/lib/jvm/jre-openjdk

# source the jpackage helpers
VERBOSE=1
. /usr/share/java-utils/java-functions
# set JAVA_* environment variables
set_javacmd
check_java_env
set_jvm_dirs
if [ -x /usr/lib64/bolzplatz2006/libirrlicht_wrap.so ]; then
  set_options "-Djava.library.path="/usr/lib64/bolzplatz2006:/usr/lib64/sdljava""
else
  set_options "-Djava.library.path="/usr/lib/bolzplatz2006:/usr/lib/sdljava""
fi

CLASSPATH=`build-classpath sdljava dom4j vecmath1.2 bolzplatz2006`
MAIN_CLASS="com.xenoage.bp2k6.Main"

export LD_LIBRARY_PATH=$JAVA_HOME/lib
run $@ > bolzplatz2006.log 2>&1
