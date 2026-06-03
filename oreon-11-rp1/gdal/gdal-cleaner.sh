#!/bin/bash
set -e

VERSION="${1:?version required}"
PRE="${2:-}"
srcdir="${3:-.}"
cd "$srcdir"

UPSTREAM="gdal-${VERSION}${PRE}.tar.xz"
if ! test -f "$UPSTREAM"; then
  curl --fail --silent --location \
    "https://download.osgeo.org/gdal/${VERSION}/gdal-${VERSION}${PRE}.tar.xz" \
    -o "$UPSTREAM"
fi

if test -d "gdal-${VERSION}${PRE}" || test -d "gdal-${VERSION}${PRE}-fedora"; then
  echo "gdal-${VERSION}${PRE} or gdal-${VERSION}${PRE}-fedora in the way" >&2
  exit 1
fi

tar -xf "$UPSTREAM"
mv "gdal-${VERSION}${PRE}"{,-fedora}
pushd "gdal-${VERSION}${PRE}-fedora"

rm -f ogr/data/cubewerx_extra.wkt ogr/data/esri_StatePlane_extra.wkt ogr/data/ecw_cs.wkt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/data/cubewerx_extra.wkt||' ogr/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/data/esri_StatePlane_extra.wkt||' ogr/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/data/ecw_cs.wkt||' ogr/CMakeLists.txt

popd
tar -cJf "gdal-${VERSION}${PRE}-fedora.tar.xz" "gdal-${VERSION}${PRE}-fedora"
