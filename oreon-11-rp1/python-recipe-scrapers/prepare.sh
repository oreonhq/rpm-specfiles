#!/bin/bash
VERSION=$1
wget https://github.com/hhursev/recipe-scrapers/archive/${VERSION}/recipe-scrapers-${VERSION}.tar.gz
tar -xf recipe-scrapers-${VERSION}.tar.gz 
cd recipe-scrapers-${VERSION}/
rm -r tests/test_data/
cd ..
tar -cvf recipe-scrapers-${VERSION}-clean.tar recipe-scrapers-${VERSION}
gzip recipe-scrapers-${VERSION}-clean.tar 
