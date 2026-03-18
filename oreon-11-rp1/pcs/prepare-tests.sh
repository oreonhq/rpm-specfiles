#!/bin/sh

set -eo xtrace
cd $TMT_SOURCE_DIR
# Use stamp file to abort if this script already ran
if [ -e tests-prepared-stamp ]; then exit 0; fi
# RPM 4.20 changed the builddir structure - unpacked sources go to *-build but
# tmt copies them back to pcs-*, so the pcs-*-build folder is empty
# Remove pcs-web-ui, pcs-*-build for "cd pcs-*" to have exactly one match
rm -rf pcs-web-ui-* pcs-*-build
cd pcs-*/
# Run autotools, use bundled dependencies from the system
export PYTHONPATH=/usr/lib/pcs/pcs_bundled/packages/
export GEM_HOME=/usr/lib/pcsd/vendor/bundle/
# We need to use cd pcs-* because when pcs-web-ui starts using autotools, running
# autogen and configure with expanded TMT_SOURCE_DIR will match that too
./autogen.sh
./configure --enable-webui --enable-local-build --enable-use-local-cache-only \
  --enable-individual-bundling --with-pcs-lib-dir=/usr/lib
# Remove pcs sources to make sure tests are not using any of those files
rm -rf pcs
touch ../tests-prepared-stamp
