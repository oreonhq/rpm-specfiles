#!/bin/bash

# freecol does not work with gcj
JAVA_HOME=/usr/lib/jvm/jre-openjdk

# source the jpackage helpers
VERBOSE=1
. /usr/share/java-utils/java-functions

# set JAVA_* environment variables
set_javacmd
check_java_env
set_jvm_dirs

CLASSPATH=`build-classpath freecol commons-cli cortado jogg jorbis miglayout-core miglayout-swing`
MAIN_CLASS="net.sf.freecol.FreeCol"
set_options -Xmx2000M -Dsun.java2d.pmoffscreen=false

run --freecol-data /usr/share/freecol/data "$@"
