# idea soources have 280MB
# decompiler itself is 375kB now, including test classes...
VERSION=211.7442.40
INPUT=$VERSION.tar.gz
TOP_DIR=intellij-community-idea-$VERSION
DECOMPILER_DIR=$TOP_DIR/plugins/java-decompiler
NAME=fernflower
OUT_NAME=$NAME-$VERSION
OUTPUT=$OUT_NAME.tar.gz

if [ -e $OUTPUT ] ; then
  echo "$OUTPUT already exists"
else
  if [ -e $INPUT ] ; then
    echo "$INPUT already exists, not downloading"
    set -ex
  else
    set -ex
    wget https://github.com/JetBrains/intellij-community/archive/idea/$INPUT
  fi
  tar tzf $INPUT | grep -e decompiler -e LICENSE
  tar -xvf $INPUT  $DECOMPILER_DIR/engine
  tar -xvf $INPUT  $TOP_DIR/LICENSE.txt
  mv $TOP_DIR/LICENSE.txt $DECOMPILER_DIR/engine
  pushd $DECOMPILER_DIR/
    mv engine $OUT_NAME
    tar -cJf $OUTPUT $OUT_NAME 
  popd
  mv $DECOMPILER_DIR/$OUTPUT .
  rm -rf $TOP_DIR
fi
