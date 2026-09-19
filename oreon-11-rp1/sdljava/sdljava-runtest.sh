#!/bin/sh

# source the jpackage helpers
VERBOSE=1
. /usr/share/java-utils/java-functions

# set JAVA_* environment variables
set_javacmd
check_java_env
set_jvm_dirs

CLASSPATH=`build-classpath sdljava`
MAIN_CLASS="$1"
if [ -x /usr/lib64/sdljava/libsdljava.so ]; then
  set_options "-Djava.library.path="/usr/lib64/sdljava""
else
  set_options "-Djava.library.path="/usr/lib/sdljava""
fi

shift
run "$@"
