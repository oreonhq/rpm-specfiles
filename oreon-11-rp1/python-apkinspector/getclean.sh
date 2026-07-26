#!/bin/bash
wget https://github.com/erev0s/apkInspector/archive/v$1/apkinspector-$1.tar.gz
tar -xf apkinspector-$1.tar.gz 
rm -r apkInspector-$1/tests/
tar -cvf apkInspector-$1-clean.tar apkInspector-$1/
gzip apkInspector-$1-clean.tar 
