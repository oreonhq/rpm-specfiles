#!/bin/bash
# Run the script and enter the version as the first command line argument
version=${1}
wget https://github.com/androguard/androguard/archive/v${version}/androguard-v${version}.tar.gz
tar -xf androguard-v${version}.tar.gz
# remove test and exaqmple
rm -r androguard-${version}/tests/ 
rm -r androguard-${version}/examples/
tar -cf androguard-${version}-clean.tar androguard-${version}
gzip androguard-${version}-clean.tar 
