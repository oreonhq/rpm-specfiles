#! /bin/sh

jsname=MathJax-src
version=3.2.2

[ -r ${jsname}-${version}.tar.gz ] && \
    echo ${jsname}-${version}.tar.gz already exists && exit 1
[ -r ${jsname}-${version}-node-modules.tar.gz ] && \
    echo ${jsname}-${version}-node-modules.tar.gz already exists && exit 1

wget -N https://github.com/mathjax/${jsname}/archive/${version}/${jsname}-${version}.tar.gz

curdir=$(pwd)
tmpdir=$(mktemp -d)

cd ${tmpdir}

tar -z -x -f ${curdir}/${jsname}-${version}.tar.gz
cd ${jsname}-${version}

npm install --save-dev

tar -z -c --group root --owner root -f ${curdir}/${jsname}-${version}-node-modules.tar.gz node_modules

cd ${curdir}
rm -rf ${tmpdir}
