#! /bin/sh

jsname=jquery-ui
version=1.14.2

[ -r ${jsname}-${version}.tar.gz ] && \
    echo ${jsname}-${version}.tar.gz already exists && exit 1
[ -r ${jsname}-${version}-node-modules.tar.gz ] && \
    echo ${jsname}-${version}-node-modules.tar.gz already exists && exit 1

wget -N https://github.com/jquery/${jsname}/archive/${version}/${jsname}-${version}.tar.gz

curdir=$(pwd)
tmpdir=$(mktemp -d)

cd ${tmpdir}

# We need to bundle build dependencies since they are no longer
# available in Fedora. This uses the same technique as the js-jquery
# package.

tar -z -x -f ${curdir}/${jsname}-${version}.tar.gz
cd ${jsname}-${version}

# Reduce the dev dependencies in the package.json file by removing
# stuff not needed for the build. This reduces the size of the bundled
# build dependencies considerably.

patch -p1 <<EOF
--- a/package.json
+++ b/package.json
@@ -52,25 +52,12 @@
 		"test": "grunt && npm run test:unit -- --headless"
 	},
 	"dependencies": {
-		"jquery": ">=1.12.0 <5.0.0"
 	},
 	"devDependencies": {
-		"@swc/core": "1.15.2",
-		"commitplease": "3.2.0",
-		"eslint-config-jquery": "3.0.2",
-		"globals": "16.5.0",
 		"grunt": "1.6.1",
-		"grunt-bowercopy": "1.2.5",
-		"grunt-compare-size": "0.4.2",
 		"grunt-contrib-concat": "2.1.0",
-		"grunt-contrib-csslint": "2.0.0",
 		"grunt-contrib-requirejs": "1.0.0",
-		"grunt-eslint": "26.0.0",
-		"grunt-git-authors": "3.2.0",
-		"grunt-html": "18.0.2",
-		"jquery-test-runner": "0.2.8",
-		"load-grunt-tasks": "5.1.0",
-		"rimraf": "6.1.0"
+		"load-grunt-tasks": "5.1.0"
 	},
 	"keywords": []
 }
EOF

npm install --save-dev

tar -z -c --group root --owner root -f ${curdir}/${jsname}-${version}-node-modules.tar.gz node_modules

cd ${curdir}
rm -rf ${tmpdir}
