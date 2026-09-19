#! /bin/bash

VERSION=$1

VERSIONEDNAME=pyglet-${VERSION}
ARCHIVENAME=${VERSIONEDNAME}.tar.gz
wget -N https://github.com/pyglet/pyglet/archive/v${VERSION}.tar.gz -O ${ARCHIVENAME}
tar xzvf ${ARCHIVENAME}
pushd ${VERSIONEDNAME}
rm -rvf tools  # random developer tools (*)
rm -rvf contrib  # again, questionable licensing
rm -v pyglet/image/codecs/s3tc.py  # patent-encumbered algorithm (**)
rm -v pyglet/image/codecs/dds.py  # image codec that uses s3tc (**)
rm -rvf examples  # includes non-free artwork
rm -rvf tests/data/fonts  # includes non-free font
rm -rvf tests/data/images/*.dds  # compressed with patent-encumbered algorithm
rm -rvf tests/data/images/dinosaur.gif  # questionable origin

# questionable sound files "retrieved from libpurple":
rm -rvf tests/data/media/{alert,login,logout,receive,send}.wav

popd
tar czvf ${VERSIONEDNAME}-repacked.tar.gz ${VERSIONEDNAME}



# (*) pyglet developers put random utilities in `tools`, without much
# regard to licenses. The development tree at 2012-10-19 included some GPL,
# for example. Given the project's culture, non-free code could be included
# in the future, so it's better to remove the directory to be on the safe side.

# (**) pyglet uses the patented S3 texture compression algorithm to
# encode/decode DirectX texture files (*.dds).
# Removing the two files disables the feature cleanly (see the guarded
# dss import in pyglet/image/codecs/__init__.py).
