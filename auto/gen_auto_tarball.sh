#!/bin/bash -e

VAL_TAG=auto-value-1.6.1
COM_TAG=auto-common-0.10
SER_TAG=auto-service-1.0-rc4
PARENT_TAG=auto-parent-6

mkdir $VAL_TAG/
pushd $VAL_TAG/
wget https://github.com/google/auto/archive/$VAL_TAG.tar.gz
tar xvf $VAL_TAG.tar.gz --strip-components=1
rm -rf pom.xml factory/ common/ service/
wget https://github.com/google/auto/archive/$COM_TAG.tar.gz
tar xvf $COM_TAG.tar.gz --strip-components=1 auto-$COM_TAG/common
wget https://github.com/google/auto/archive/$SER_TAG.tar.gz
tar xvf $SER_TAG.tar.gz --strip-components=1 auto-$SER_TAG/service
wget https://github.com/google/auto/archive/$PARENT_TAG.tar.gz
tar xvf $PARENT_TAG.tar.gz --strip-components=1 auto-$PARENT_TAG/pom.xml
rm *.tar.gz
popd

tar caf $VAL_TAG.tar.gz $VAL_TAG/
rm -rf $VAL_TAG/

