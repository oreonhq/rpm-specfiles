%global source0_hash none

# Without this the build time baloons from 1 hour to more than 46 on i686
# https://bugzilla.redhat.com/show_bug.cgi?id=2390105
%undefine _preserve_static_debuginfo
%define _find_debuginfo_opts --no-ar-files

%global run_tests 1

%global bashcompletiondir %(pkg-config --variable=compatdir bash-completion)

# We have multilib triage
%if "%{_lib}" == "lib"
  %global cpuarch 32
%else
  %global cpuarch 64
%endif


%if 0%{?bootstrap}
%global with_mysql 0
%global mysql --without-mysql
%global with_poppler 0
%global poppler --without-poppler
%global with_spatialite 0
%global spatialite --without-spatialite
%else
# https://bugzilla.redhat.com/show_bug.cgi?id=1490492
%global with_mysql 1
%global mysql --with-mysql
# https://bugzilla.redhat.com/show_bug.cgi?id=1490492
%global with_poppler 1
%global poppler --with-poppler
%global with_spatialite 1
%global spatialite "--with-spatialite"
%endif

%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without mingw
%bcond_without python3
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%else
%bcond_with mingw
%bcond_with python3
%bcond_with java
%endif

#global pre beta1


Name:          gdal
Version:       3.12.4
Release:       1%{?dist}
Summary:       GIS file format library
License:       MIT
URL:           http://www.gdal.org
# Source0:   http://download.osgeo.org/gdal/%%{version}/gdal-%%{version}.tar.xz
# See PROVENANCE.TXT-fedora and the cleaner script for details!

Source0:       %{name}-%{version}%{?pre:%pre}-fedora.tar.xz
Source1:        http://download.osgeo.org/gdal/3.12.4/gdalautotest-3.12.4%{?pre:%pre}.zip
# Multilib compatible cpl-config.h header
Source2:       cpl-config.h
# Multilib compatible gdal-config script
Source3:       gdal-config
Source4:       PROVENANCE.TXT-fedora

# Cleaner script for the tarball
Source5:       %{name}-cleaner.sh

# Add some utils to the default install target
Patch0:        gdal_utils.patch

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: bison
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: geos-devel
BuildRequires: json-c-devel
BuildRequires: libarchive-devel
BuildRequires: libpng-devel
BuildRequires: libpq-devel
BuildRequires: libtiff-devel
BuildRequires: libtirpc-devel
BuildRequires: mariadb-connector-c-devel
BuildRequires: openjpeg2-devel
BuildRequires: pcre2-devel
BuildRequires: proj-devel >= 5.2.0
BuildRequires: sqlite-devel
BuildRequires: swig
BuildRequires: unixODBC-devel
BuildRequires: unzip
BuildRequires: xz-devel
BuildRequires: zlib-devel

%if 0%{?fedora} || (0%{?oreon} >= 11)
# Fedora dependencies
BuildRequires: armadillo-devel
BuildRequires: blosc-devel
BuildRequires: cfitsio-devel
BuildRequires: CharLS-devel
BuildRequires: freexl-devel
BuildRequires: giflib-devel
BuildRequires: gtest-devel
BuildRequires: hdf-devel
BuildRequires: hdf5-devel
%ifnarch %{ix86} %{arm}
BuildRequires: libarrow-devel
BuildRequires: libarrow-dataset-devel
%endif
BuildRequires: libdap-devel
BuildRequires: libdeflate-devel
BuildRequires: libgeotiff-devel
BuildRequires: libgta-devel
BuildRequires: libjpeg-devel
BuildRequires: libkml-devel
BuildRequires: liblerc-devel
%if %{with_spatialite}
BuildRequires: libspatialite-devel
%endif
BuildRequires: libwebp-devel
BuildRequires: libzstd-devel
%if 0%{?with_mysql}
BuildRequires: mariadb-connector-c-devel
%endif
BuildRequires: muParser-devel
BuildRequires: netcdf-devel
BuildRequires: openexr-devel
BuildRequires: openssl-devel-engine
%ifnarch %{ix86} %{arm}
BuildRequires: parquet-libs-devel
%endif
%if 0%{?with_poppler}
BuildRequires: poppler-devel
%endif
BuildRequires: qhull-devel
BuildRequires: xerces-c-devel
%else
# RHEL dependencies
BuildRequires: libjpeg-turbo-devel
BuildRequires: openssl-devel
%endif

# Python
%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-filelock
BuildRequires: python3-numpy
BuildRequires: python3-setuptools
BuildRequires: python3dist(pytest) >= 3.6
BuildRequires: python3dist(lxml) >= 4.5.1
%endif

# Java
%if %{with java}
# For 'mvn_artifact' and 'mvn_install'
BuildRequires: ant-openjdk25
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: javapackages-local-openjdk25
BuildRequires: jpackage-utils
%endif

# MinGW
%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-cfitsio
BuildRequires: mingw32-curl
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-expat
BuildRequires: mingw32-freexl
BuildRequires: mingw32-geos
BuildRequires: mingw32-giflib
BuildRequires: mingw32-json-c
BuildRequires: mingw32-libarchive
BuildRequires: mingw32-libgeotiff
BuildRequires: mingw32-libgta
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libkml
BuildRequires: mingw32-liblerc
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libspatialite
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libwebp
BuildRequires: mingw32-openexr
BuildRequires: mingw32-openjpeg2
BuildRequires: mingw32-pcre2
BuildRequires: mingw32-poppler
BuildRequires: mingw32-postgresql
BuildRequires: mingw32-proj
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-xerces-c
BuildRequires: mingw32-xz-libs
BuildRequires: mingw32-zlib
BuildRequires: mingw32-zstd
%if %{with python3}
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-numpy
BuildRequires: mingw32-python3-setuptools
%endif

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-cfitsio
BuildRequires: mingw64-curl
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-expat
BuildRequires: mingw64-freexl
BuildRequires: mingw64-geos
BuildRequires: mingw64-giflib
BuildRequires: mingw64-json-c
BuildRequires: mingw64-libarchive
BuildRequires: mingw64-libgeotiff
BuildRequires: mingw64-libgta
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libkml
BuildRequires: mingw64-liblerc
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libspatialite
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libwebp
BuildRequires: mingw64-openexr
BuildRequires: mingw64-openjpeg2
BuildRequires: mingw64-pcre2
BuildRequires: mingw64-poppler
BuildRequires: mingw64-postgresql
BuildRequires: mingw64-proj
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-xerces-c
BuildRequires: mingw64-xz-libs
BuildRequires: mingw64-zlib
BuildRequires: mingw64-zstd
%if %{with python3}
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-numpy
BuildRequires: mingw64-python3-setuptools
%endif
%endif

%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:      gpsbabel
%endif
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}


%description
Geospatial Data Abstraction Library (GDAL/OGR) is a cross platform
C++ translator library for raster and vector geospatial data formats.
As a library, it presents a single abstract data model to the calling
application for all supported formats. It also comes with a variety of
useful commandline utilities for data translation and processing.

It provides the primary data access engine for many applications.
GDAL/OGR is the most widely used geospatial data access library.


%package devel
Summary:       Development files for the GDAL file format library
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for GDAL.


%package libs
Summary:       GDAL file format library
# See frmts/grib/degrib/README.TXT
Provides:      bundled(g2lib) = 1.6.0
Provides:      bundled(degrib) = 2.14

%description libs
This package contains the GDAL file format library.


%if %{with java}
%package java
Summary:        Java modules for the GDAL file format library
Requires:       jpackage-utils
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description java
The GDAL Java modules provide support to handle multiple GIS file formats.


%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.
%endif


%if %{with python3}
%package -n python3-gdal
%{?python_provide:%python_provide python3-gdal}
Summary:        Python modules for the GDAL file format library
Requires:       python3-numpy
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-gdal
The GDAL Python 3 modules provide support to handle multiple GIS file formats.


%package python-tools
Summary:        Python tools for the GDAL file format library
Requires:       python3-gdal

%description python-tools
The GDAL Python package provides number of tools for programming and
manipulating GDAL file format library

# We don't want to provide private Python extension libs
%global __provides_exclude_from ^%{python3_sitearch}/.*\.so$
%endif


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows GDAL library
# GDAL bundles a modified copy of g2clib and degrib
# See frmts/grib/degrib/README.TXT
Provides:      bundled(g2lib) = 1.6.0
Provides:      bundled(degrib) = 2.14
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows GDAL library.


%package -n mingw32-%{name}-tools
Summary:       MinGW Windows GDAL library tools
BuildArch:     noarch

%description -n mingw32-%{name}-tools
MinGW Windows GDAL library tools.


%if %{with python3}
%package -n mingw32-python3-%{name}
Summary:       MinGW Windows Python3 GDAL bindings

%description -n mingw32-python3-%{name}
MinGW Windows Python3 GDAL bindings.
%endif


%package -n mingw64-%{name}
Summary:       MinGW Windows GDAL library
# GDAL bundles a modified copy of g2clib and degrib
# See frmts/grib/degrib/README.TXT
Provides:      bundled(g2lib) = 1.6.0
Provides:      bundled(degrib) = 2.14
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows GDAL library.


%package -n mingw64-%{name}-tools
Summary:       MinGW Windows GDAL library tools
BuildArch:     noarch

%description -n mingw64-%{name}-tools
MinGW Windows GDAL library tools.


%if %{with python3}
%package -n mingw64-python3-%{name}
Summary:       MinGW Windows Python3 GDAL bindings

%description -n mingw64-python3-%{name}
MinGW Windows Python3 GDAL bindings.
%endif

%{?mingw_debug_package}
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -N -p1 -n %{name}-%{version}%{?pre:%pre}-fedora

# Delete bundled libraries
# rm -rf frmts/zlib
rm -rf frmts/png/libpng
rm -rf frmts/gif/giflib
rm -rf frmts/jpeg/libjpeg
rm -rf frmts/jpeg/libjpeg12
rm -rf frmts/gtiff/libgeotiff
# FIXME: frmts/libertiff/libtiff_codecs.h requires tif_lzw.c, tif_packbits.c, tif_lerc.c
# rm -rf frmts/gtiff/libtiff
rm -rf mrf/LERCV1
rm -rf third_party/LercLib

# Setup autotest directory
unzip %{SOURCE1}
mv %{name}autotest-%{version}%{?pre:%pre} autotest

# Need to patch autotest
%autopatch -p1

# Copy in PROVENANCE.TXT-fedora
cp -a %{SOURCE4} .


%build
%cmake \
  -DCMAKE_INSTALL_INCLUDEDIR=include/gdal \
  -DGDAL_USE_EXTERNAL_LIB=ON \
  -DGDAL_USE_INTERNAL_LIBS=OFF \
%if %{with java}
  -DGDAL_JAVA_INSTALL_DIR=%{_jnidir}/%{name} \
  -DGDAL_JAVA_JNI_INSTALL_DIR=%{_jnidir}/%{name} \
%endif
%if ! 0%{?fedora} || (0%{?oreon} >= 11)
  -DGDAL_BUILD_OPTIONAL_DRIVERS=OFF \
  -DOGR_BUILD_OPTIONAL_DRIVERS=OFF \
  -DBUILD_PYTHON_BINDINGS=OFF \
  -DBUILD_TESTING=OFF
%endif
%cmake_build

%if %{with mingw}
%mingw_cmake \
  -DBUILD_TESTING=OFF \
  -DCMAKE_INSTALL_INCLUDEDIR=include/gdal \
  -DGDAL_USE_EXTERNAL_LIB=ON \
  -DGDAL_USE_INTERNAL_LIBS=OFF
%mingw_make_build
%endif


%install
%cmake_install

%if %{with mingw}
%mingw_make_install
# Delete data from cross packages
rm -r %{buildroot}%{mingw32_datadir}
rm -r %{buildroot}%{mingw64_datadir}
%endif

# Multilib
# - cpl_config.h is arch-dependent (contains various SIZEOF defines)
# - gdal-config stores arch-specific information
mv %{buildroot}%{_includedir}/%{name}/cpl_config.h %{buildroot}%{_includedir}/%{name}/cpl_config-%{cpuarch}.h
cp -a %{SOURCE2} %{buildroot}%{_includedir}/%{name}/cpl_config.h
mv %{buildroot}%{_bindir}/%{name}-config %{buildroot}%{_bindir}/%{name}-config-%{cpuarch}
cp -a %{SOURCE3} %{buildroot}%{_bindir}/%{name}-config

# FIXME Fix shebangs
find %{buildroot} -name '*.py' -exec sed -i 's|^#!python$|#!/usr/bin/python3|g' {} \;

%if %{without python3}
# completions and manpages for python scripts regardless of BUILD_PYTHON_BINDINGS
for p in gdal2tiles gdal2xyz gdal_calc gdal_edit gdal_fillnodata gdal_merge gdal_pansharpen \
         gdal_polygonize gdal_proximity gdal_retile gdal_sieve gdalchksum gdalcompare \
         gdalident gdalimport gdalmove ogr_layer_algebra ogrmerge pct2rgb rgb2pct ; do
    rm -f %{buildroot}%{_datadir}/bash-completion/completions/${p}.py
    rm -f %{buildroot}%{_mandir}/man1/${p}.1*
done
%endif

%if %{with mingw}
%mingw_debug_install_post
%endif


%if 0%{run_tests}
%check
# FIXME Tests hang on s390x ppc64le
%ifnarch s390x ppc64le
%ctest || :
%endif
%endif


%files
%{_bindir}/gdal
%{_bindir}/gdal_contour
%{_bindir}/gdal_create
%{_bindir}/gdal_footprint
%{_bindir}/gdal_grid
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_translate
%{_bindir}/gdal_viewshed
%{_bindir}/gdaladdo
%{_bindir}/gdalbuildvrt
%{_bindir}/gdaldem
%{_bindir}/gdalenhance
%{_bindir}/gdalinfo
%{_bindir}/gdallocationinfo
%{_bindir}/gdalmanage
%{_bindir}/gdalmdiminfo
%{_bindir}/gdalmdimtranslate
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltindex
%{_bindir}/gdaltransform
%{_bindir}/gdalwarp
%{_bindir}/gnmanalyse
%{_bindir}/gnmmanage
%{_bindir}/nearblack
%{_bindir}/ogr2ogr
%{_bindir}/ogrinfo
%{_bindir}/ogrlineref
%{_bindir}/ogrtindex
%{_bindir}/sozip
%if 0%{?fedora} || (0%{?oreon} >= 11)
%{_bindir}/8211*
%{_bindir}/s57dump
%endif
%{_datadir}/bash-completion/completions/gdal
%{_datadir}/bash-completion/completions/gdal_contour
%{_datadir}/bash-completion/completions/gdal_create
%{_datadir}/bash-completion/completions/gdal_footprint
%{_datadir}/bash-completion/completions/gdal_grid
%{_datadir}/bash-completion/completions/gdal_rasterize
%{_datadir}/bash-completion/completions/gdal_translate
%{_datadir}/bash-completion/completions/gdal_viewshed
%{_datadir}/bash-completion/completions/gdaladdo
%{_datadir}/bash-completion/completions/gdalbuildvrt
%{_datadir}/bash-completion/completions/gdaldem
%{_datadir}/bash-completion/completions/gdalenhance
%{_datadir}/bash-completion/completions/gdalinfo
%{_datadir}/bash-completion/completions/gdallocationinfo
%{_datadir}/bash-completion/completions/gdalmanage
%{_datadir}/bash-completion/completions/gdalsrsinfo
%{_datadir}/bash-completion/completions/gdaltindex
%{_datadir}/bash-completion/completions/gdaltransform
%{_datadir}/bash-completion/completions/gdalwarp
%{_datadir}/bash-completion/completions/ogr2ogr
%{_datadir}/bash-completion/completions/ogrinfo
%{_datadir}/bash-completion/completions/ogrlineref
%{_datadir}/bash-completion/completions/ogrtindex
%{_datadir}/bash-completion/completions/sozip
%{_mandir}/man1/gdal.1*
%{_mandir}/man1/gdaladdo.1*
%{_mandir}/man1/gdalbuildvrt.1*
%{_mandir}/man1/gdal_contour.1*
%{_mandir}/man1/gdal-convert.1*
%{_mandir}/man1/gdal_create.1*
%{_mandir}/man1/gdal-dataset.1.gz
%{_mandir}/man1/gdal-dataset-copy.1.gz
%{_mandir}/man1/gdal-dataset-delete.1.gz
%{_mandir}/man1/gdal-dataset-identify.1.gz
%{_mandir}/man1/gdal-dataset-rename.1.gz
%{_mandir}/man1/gdaldem.1*
%{_mandir}/man1/gdal_footprint.1*
%{_mandir}/man1/gdal_grid.1*
%{_mandir}/man1/gdal-info.1*
%{_mandir}/man1/gdalinfo.1*
%{_mandir}/man1/gdallocationinfo.1*
%{_mandir}/man1/gdalmanage.1*
%{_mandir}/man1/gdal-mdim.1*
%{_mandir}/man1/gdal-mdim-convert.1*
%{_mandir}/man1/gdal-mdim-info.1*
%{_mandir}/man1/gdalmdiminfo.1*
%{_mandir}/man1/gdal-mdim-mosaic.1.gz
%{_mandir}/man1/gdalmdimtranslate.1*
%{_mandir}/man1/gdal-pipeline.1.gz
%{_mandir}/man1/gdal-raster.1*
%{_mandir}/man1/gdal-raster-as-features.1.gz
%{_mandir}/man1/gdal-raster-aspect.1.gz
%{_mandir}/man1/gdal-raster-calc.1*
%{_mandir}/man1/gdal-raster-clean-collar.1*
%{_mandir}/man1/gdal-raster-clip.1*
%{_mandir}/man1/gdal-raster-color-blend.1.gz
%{_mandir}/man1/gdal-raster-color-map.1*
%{_mandir}/man1/gdal-raster-compare.1.gz
%{_mandir}/man1/gdal-raster-contour.1*
%{_mandir}/man1/gdal-raster-convert.1*
%{_mandir}/man1/gdal-raster-create.1*
%{_mandir}/man1/gdal-raster-edit.1*
%{_mandir}/man1/gdal-raster-fill-nodata.1*
%{_mandir}/man1/gdal-raster-footprint.1*
%{_mandir}/man1/gdal-raster-hillshade.1*
%{_mandir}/man1/gdal-raster-index.1*
%{_mandir}/man1/gdal-raster-info.1*
%{_mandir}/man1/gdal_rasterize.1*
%{_mandir}/man1/gdal-raster-mosaic.1*
%{_mandir}/man1/gdal-raster-neighbors.1.gz
%{_mandir}/man1/gdal-raster-nodata-to-alpha.1.gz
%{_mandir}/man1/gdal-raster-overview-add.1*
%{_mandir}/man1/gdal-raster-overview-delete.1*
%{_mandir}/man1/gdal-raster-overview-refresh.1.gz
%{_mandir}/man1/gdal-raster-pansharpen.1.gz
%{_mandir}/man1/gdal-raster-pipeline.1*
%{_mandir}/man1/gdal-raster-pixel-info.1*
%{_mandir}/man1/gdal-raster-polygonize.1*
%{_mandir}/man1/gdal-raster-proximity.1.gz
%{_mandir}/man1/gdal-raster-reclassify.1*
%{_mandir}/man1/gdal-raster-reproject.1*
%{_mandir}/man1/gdal-raster-resize.1*
%{_mandir}/man1/gdal-raster-rgb-to-palette.1.gz
%{_mandir}/man1/gdal-raster-roughness.1*
%{_mandir}/man1/gdal-raster-scale.1*
%{_mandir}/man1/gdal-raster-select.1*
%{_mandir}/man1/gdal-raster-set-type.1*
%{_mandir}/man1/gdal-raster-sieve.1*
%{_mandir}/man1/gdal-raster-slope.1*
%{_mandir}/man1/gdal-raster-stack.1*
%{_mandir}/man1/gdal-raster-tile.1*
%{_mandir}/man1/gdal-raster-tpi.1*
%{_mandir}/man1/gdal-raster-tri.1*
%{_mandir}/man1/gdal-raster-unscale.1*
%{_mandir}/man1/gdal-raster-update.1.gz
%{_mandir}/man1/gdal-raster-viewshed.1*
%{_mandir}/man1/gdal-raster-zonal-stats.1.gz
%{_mandir}/man1/gdalsrsinfo.1*
%{_mandir}/man1/gdaltindex.1*
%{_mandir}/man1/gdaltransform.1*
%{_mandir}/man1/gdal_translate.1*
%{_mandir}/man1/gdal-vector.1*
%{_mandir}/man1/gdal-vector-buffer.1.gz
%{_mandir}/man1/gdal-vector-check-coverage.1.gz
%{_mandir}/man1/gdal-vector-check-geometry.1.gz
%{_mandir}/man1/gdal-vector-clean-coverage.1.gz
%{_mandir}/man1/gdal-vector-clip.1*
%{_mandir}/man1/gdal-vector-concat.1*
%{_mandir}/man1/gdal-vector-convert.1*
%{_mandir}/man1/gdal-vector-edit.1*
%{_mandir}/man1/gdal-vector-explode-collections.1.gz
%{_mandir}/man1/gdal-vector-filter.1*
%{_mandir}/man1/gdal-vector-grid.1*
%{_mandir}/man1/gdal-vector-index.1.gz
%{_mandir}/man1/gdal-vector-info.1*
%{_mandir}/man1/gdal-vector-layer-algebra.1.gz
%{_mandir}/man1/gdal-vector-make-point.1.gz
%{_mandir}/man1/gdal-vector-make-valid.1.gz
%{_mandir}/man1/gdal-vector-partition.1.gz
%{_mandir}/man1/gdal-vector-pipeline.1*
%{_mandir}/man1/gdal-vector-rasterize.1*
%{_mandir}/man1/gdal-vector-segmentize.1.gz
%{_mandir}/man1/gdal-vector-select.1*
%{_mandir}/man1/gdal-vector-set-field-type.1.gz
%{_mandir}/man1/gdal-vector-set-geom-type.1.gz
%{_mandir}/man1/gdal-vector-simplify.1.gz
%{_mandir}/man1/gdal-vector-sql.1*
%{_mandir}/man1/gdal-vector-swap-xy.1.gz
%{_mandir}/man1/gdal_viewshed.1*
%{_mandir}/man1/gdal-vsi.1*
%{_mandir}/man1/gdal-vsi-copy.1*
%{_mandir}/man1/gdal-vsi-delete.1*
%{_mandir}/man1/gdal-vsi-list.1*
%{_mandir}/man1/gdal-vsi-move.1*
%{_mandir}/man1/gdal-vsi-sozip.1*
%{_mandir}/man1/gdal-vsi-sync.1*
%{_mandir}/man1/gdalwarp.1*
%{_mandir}/man1/gnmanalyse.1*
%{_mandir}/man1/gnmmanage.1*
%{_mandir}/man1/nearblack.1*
%{_mandir}/man1/ogr2ogr.1*
%{_mandir}/man1/ogrinfo.1*
%{_mandir}/man1/ogrlineref.1*
%{_mandir}/man1/ogrtindex.1*
%{_mandir}/man1/sozip.1*

%files libs
%license LICENSE.TXT
%doc NEWS.md PROVENANCE.TXT COMMITTERS PROVENANCE.TXT-fedora
%{_libdir}/libgdal.so.38
%{_libdir}/libgdal.so.38.*
%{_datadir}/%{name}/
%{_libdir}/gdalplugins/

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-config-%{cpuarch}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/gdal/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/bash-completion/completions/gdal-config
%{_mandir}/man1/gdal-config.1*

%if %{with java}
%files java
%{_jnidir}/%{name}/gdal-%{version}-sources.jar
%{_jnidir}/%{name}/gdal-%{version}.jar
%{_jnidir}/%{name}/gdal-%{version}.pom
%{_jnidir}/%{name}/libgdalalljni.so

%files javadoc
%{_jnidir}/%{name}/gdal-%{version}-javadoc.jar
%endif

%if %{with python3}
%files -n python3-gdal
%doc swig/python/README.rst
%{python3_sitearch}/GDAL-%{version}-py*.egg-info/
%{python3_sitearch}/osgeo/
%{python3_sitearch}/osgeo_utils/

%files python-tools
%{_bindir}/gdal2tiles
%{_bindir}/gdal2tiles.py
%{_bindir}/gdal2xyz
%{_bindir}/gdal2xyz.py
%{_bindir}/gdalattachpct
%{_bindir}/gdalattachpct.py
%{_bindir}/gdal_calc
%{_bindir}/gdal_calc.py
%{_bindir}/gdalcompare
%{_bindir}/gdalcompare.py
%{_bindir}/gdal_edit
%{_bindir}/gdal_edit.py
%{_bindir}/gdal_fillnodata
%{_bindir}/gdal_fillnodata.py
%{_bindir}/gdal_merge
%{_bindir}/gdal_merge.py
%{_bindir}/gdalmove
%{_bindir}/gdalmove.py
%{_bindir}/gdal_pansharpen
%{_bindir}/gdal_pansharpen.py
%{_bindir}/gdal_polygonize
%{_bindir}/gdal_polygonize.py
%{_bindir}/gdal_proximity
%{_bindir}/gdal_proximity.py
%{_bindir}/gdal_retile
%{_bindir}/gdal_retile.py
%{_bindir}/gdal_sieve
%{_bindir}/gdal_sieve.py
%{_bindir}/ogr_layer_algebra
%{_bindir}/ogr_layer_algebra.py
%{_bindir}/ogrmerge
%{_bindir}/ogrmerge.py
%{_bindir}/pct2rgb
%{_bindir}/pct2rgb.py
%{_bindir}/rgb2pct
%{_bindir}/rgb2pct.py
%{_datadir}/bash-completion/completions/gdal2tiles.py
%{_datadir}/bash-completion/completions/gdal2xyz.py
%{_datadir}/bash-completion/completions/gdalcompare.py
%{_datadir}/bash-completion/completions/gdalmove.py
%{_datadir}/bash-completion/completions/gdal_calc.py
%{_datadir}/bash-completion/completions/gdal_edit.py
%{_datadir}/bash-completion/completions/gdal_fillnodata.py
%{_datadir}/bash-completion/completions/gdal_merge.py
%{_datadir}/bash-completion/completions/gdal_polygonize.py
%{_datadir}/bash-completion/completions/gdal_proximity.py
%{_datadir}/bash-completion/completions/gdal_retile.py
%{_datadir}/bash-completion/completions/gdal_sieve.py
%{_datadir}/bash-completion/completions/ogrmerge.py
%{_datadir}/bash-completion/completions/ogr_layer_algebra.py
%{_mandir}/man1/gdal2tiles.1*
%{_mandir}/man1/gdal_calc.1*
%{_mandir}/man1/gdalcompare.1*
%{_mandir}/man1/gdal_edit.1*
%{_mandir}/man1/gdal_fillnodata.1*
%{_mandir}/man1/gdal_merge.1*
%{_mandir}/man1/gdalmove.1*
%{_mandir}/man1/gdal_pansharpen.1*
%{_mandir}/man1/gdal_polygonize.1*
%{_mandir}/man1/gdal_proximity.1*
%{_mandir}/man1/gdal_retile.1*
%{_mandir}/man1/gdal_sieve.1*
%{_mandir}/man1/ogr_layer_algebra.1*
%{_mandir}/man1/ogrmerge.1*
%{_mandir}/man1/pct2rgb.1*
%{_mandir}/man1/rgb2pct.1*
%endif

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE.TXT
%{mingw32_bindir}/libgdal-38.dll
%{mingw32_bindir}/gdal-config
%{mingw32_libdir}/libgdal.dll.a
%{mingw32_libdir}/cmake/gdal/
%{mingw32_libdir}/pkgconfig/gdal.pc
%{mingw32_libdir}/gdalplugins/
%{mingw32_includedir}/%{name}/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%if %{with python3}
%files -n mingw32-python3-%{name}
%{mingw32_bindir}/gdal2tiles
%{mingw32_bindir}/gdal2tiles.py
%{mingw32_bindir}/gdal2xyz
%{mingw32_bindir}/gdal2xyz.py
%{mingw32_bindir}/gdal_calc
%{mingw32_bindir}/gdal_calc.py
%{mingw32_bindir}/gdal_edit
%{mingw32_bindir}/gdal_edit.py
%{mingw32_bindir}/gdal_fillnodata
%{mingw32_bindir}/gdal_fillnodata.py
%{mingw32_bindir}/gdal_merge
%{mingw32_bindir}/gdal_merge.py
%{mingw32_bindir}/gdal_pansharpen
%{mingw32_bindir}/gdal_pansharpen.py
%{mingw32_bindir}/gdal_polygonize
%{mingw32_bindir}/gdal_polygonize.py
%{mingw32_bindir}/gdal_proximity
%{mingw32_bindir}/gdal_proximity.py
%{mingw32_bindir}/gdal_retile
%{mingw32_bindir}/gdal_retile.py
%{mingw32_bindir}/gdal_sieve
%{mingw32_bindir}/gdal_sieve.py
%{mingw32_bindir}/gdalattachpct
%{mingw32_bindir}/gdalattachpct.py
%{mingw32_bindir}/gdalcompare
%{mingw32_bindir}/gdalcompare.py
%{mingw32_bindir}/gdalmove
%{mingw32_bindir}/gdalmove.py
%{mingw32_bindir}/ogr_layer_algebra
%{mingw32_bindir}/ogr_layer_algebra.py
%{mingw32_bindir}/ogrmerge
%{mingw32_bindir}/ogrmerge.py
%{mingw32_bindir}/pct2rgb
%{mingw32_bindir}/pct2rgb.py
%{mingw32_bindir}/rgb2pct
%{mingw32_bindir}/rgb2pct.py
%{mingw32_python3_sitearch}/GDAL-%{version}-py%{mingw32_python3_version}.egg-info/
%{mingw32_python3_sitearch}/osgeo/
%{mingw32_python3_sitearch}/osgeo_utils/
%endif

%files -n mingw64-%{name}
%license LICENSE.TXT
%{mingw64_bindir}/libgdal-38.dll
%{mingw64_bindir}/gdal-config
%{mingw64_libdir}/libgdal.dll.a
%{mingw64_libdir}/cmake/gdal/
%{mingw64_libdir}/pkgconfig/gdal.pc
%{mingw64_libdir}/gdalplugins/
%{mingw64_includedir}/%{name}/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe

%if %{with python3}
%files -n mingw64-python3-%{name}
%{mingw64_bindir}/gdal2tiles
%{mingw64_bindir}/gdal2tiles.py
%{mingw64_bindir}/gdal2xyz
%{mingw64_bindir}/gdal2xyz.py
%{mingw64_bindir}/gdal_calc
%{mingw64_bindir}/gdal_calc.py
%{mingw64_bindir}/gdal_edit
%{mingw64_bindir}/gdal_edit.py
%{mingw64_bindir}/gdal_fillnodata
%{mingw64_bindir}/gdal_fillnodata.py
%{mingw64_bindir}/gdal_merge
%{mingw64_bindir}/gdal_merge.py
%{mingw64_bindir}/gdal_pansharpen
%{mingw64_bindir}/gdal_pansharpen.py
%{mingw64_bindir}/gdal_polygonize
%{mingw64_bindir}/gdal_polygonize.py
%{mingw64_bindir}/gdal_proximity
%{mingw64_bindir}/gdal_proximity.py
%{mingw64_bindir}/gdal_retile
%{mingw64_bindir}/gdal_retile.py
%{mingw64_bindir}/gdal_sieve
%{mingw64_bindir}/gdal_sieve.py
%{mingw64_bindir}/gdalattachpct
%{mingw64_bindir}/gdalattachpct.py
%{mingw64_bindir}/gdalcompare
%{mingw64_bindir}/gdalcompare.py
%{mingw64_bindir}/gdalmove
%{mingw64_bindir}/gdalmove.py
%{mingw64_bindir}/ogr_layer_algebra
%{mingw64_bindir}/ogr_layer_algebra.py
%{mingw64_bindir}/ogrmerge
%{mingw64_bindir}/ogrmerge.py
%{mingw64_bindir}/pct2rgb
%{mingw64_bindir}/pct2rgb.py
%{mingw64_bindir}/rgb2pct
%{mingw64_bindir}/rgb2pct.py
%{mingw64_python3_sitearch}/GDAL-%{version}-py%{mingw32_python3_version}.egg-info/
%{mingw64_python3_sitearch}/osgeo/
%{mingw64_python3_sitearch}/osgeo_utils/
%endif
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.4-1
- Import
