#!/bin/sh

version=$(rpm -q --specfile --qf='%{version}\n' nodejs-nodemon.spec | head -n1)
wget https://github.com/remy/nodemon/archive/v$version.tar.gz
tar -zxf v$version.tar.gz
cd nodemon-$version
npm install --production && cd .. && tar -zcf nodemon-v$version-bundled.tar.gz nodemon-$version
