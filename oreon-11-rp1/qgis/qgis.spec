%global source0_hash none

#TODO: Run test suite (see debian/rules)

Name:           qgis
Version:        3.44.8
Release:        1%{?dist}
Summary:        A user friendly Open Source Geographic Information System

# http://issues.qgis.org/issues/3789
#               QGIS license         the bundled JS code (see %%{name}-%%{version}-vendor-licenses.txt)
License:        GPL-2.0-or-later AND MIT AND ISC AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND MIT AND (MIT OR CC0-1.0) AND Unlicense AND (MIT OR Apache-2.0) AND CC0-1.0 AND (MIT AND CC-BY-3.0) AND Python-2.0.1 AND CC-BY-4.0 AND (BSD-3-Clause OR GPL-2.0-only) AND (WTFPL OR MIT) AND (MIT AND BSD-3-Clause) AND CC-BY-3.0 AND MPL-2.0
URL:            http://www.qgis.org

Source0:        http://qgis.org/downloads/%{name}-%{version}.tar.bz2
# ./prepare_vendor.sh
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        %{name}-%{version}-vendor-licenses.txt
Source3:        %{name}-%{version}-yarn.lock
# Sample configuration files for QGIS server
Source4:        %{name}-server-httpd.conf
Source5:        %{name}-server-README.fedora

# Fix QGIS Server prefix calculation
Patch0:         %{name}-serverprefix.patch
# Pass --offline to yarn, plus replace deprecated md4 with sha256 in webpack sources
Patch1:         %{name}-yarn-offline.patch

# Applied by prepare_vendor.sh
# CVE-2024-55565.prebundle.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  draco-devel
BuildRequires:  exiv2-devel
BuildRequires:  expat-devel
BuildRequires:  fcgi-devel
BuildRequires:  flex bison
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  grass-devel
BuildRequires:  gsl-devel
BuildRequires:  laszip-devel
BuildRequires:  libdxfrw-devel
BuildRequires:  libpq-devel
BuildRequires:  libspatialite-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  ninja-build
BuildRequires:  netcdf-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
# PDAL detection relies on pdal executable
BuildRequires:  PDAL
BuildRequires:  PDAL-devel
BuildRequires:  poly2tri-devel
BuildRequires:  proj-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  python3-devel
BuildRequires:  python3-qscintilla-qt5
BuildRequires:  python3-qscintilla-qt5-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  %{py3_dist sip} >= 5.3
BuildRequires:  %{py3_dist PyQt-builder} >= 1
BuildRequires:  qca-qt5-devel
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  qwt-qt5-devel
%if 0%{?fedora} >= 43
BuildRequires:  spatialindex2.0-devel
%else
BuildRequires:  spatialindex-devel
%endif
BuildRequires:  sqlite-devel
BuildRequires:  libzstd-devel
BuildRequires:  yarnpkg

# Enable for tests
#BuildRequires:  xorg-x11-server-Xvfb

Requires:       gpsbabel
# As found in BZ#1396818
#TODO: Not picked up by build system? Relevant?
Requires:       qca-qt5-ossl

# We don't want to provide private Python extension libs
%global __provides_exclude_from ^(%{python3_sitearch}|%{_libdir}/%{name}/plugins)/.*\.so(\.%{version})?$

%description
Geographic Information System (GIS) manages, analyzes, and displays
databases of geographic information. QGIS supports shape file
viewing and editing, spatial data storage with PostgreSQL/PostGIS, projection
on-the-fly, map composition, and a number of other features via a plugin
interface. QGIS also supports display of various geo-referenced raster and
Digital Elevation Model (DEM) formats including GeoTIFF, Arc/Info ASCII Grid,
and USGS ASCII DEM.

%package devel
Summary:        Development Libraries for the QGIS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development packages for QGIS including the C header files.

%package grass
Summary:        GRASS Support Libraries for QGIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       grass%{?_isa}

%description grass
GRASS plugin for QGIS required to interface with the GRASS system.

%package -n python3-qgis
%{?python_provide:%python_provide python3-qgis}
Summary:        Python integration and plug-ins for QGIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gdal
Requires:       python3-httplib2
Requires:       python3-jinja2
Requires:       python3-matplotlib
Requires:       python3-OWSLib
Requires:       python3-psycopg2
Requires:       python3-pygments
Requires:       python3-PyYAML
Requires:       python3-qscintilla-qt5
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Supplements:    %{name}%{?_isa} = %{version}-%{release}

%description -n python3-qgis
Python integration and plug-ins for QGIS.

%package server
Summary:        FCGI-based OGC web map server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mod_fcgid

%description server
This FastCGI OGC web map server implements OGC WMS 1.3.0 and 1.1.1.
The services are prepared as regular projects in QGIS. They're rendered using
the QGIS libraries. The server also supports SLD (Styled Layer Descriptor)
for styling. Sample configurations for Httpd and Lighttpd are included.

Please refer to %{name}-server-README.fedora for details!

%prep
%autosetup -p1 -a1

# %%{name}-%%{version}-vendor-licenses.txt
cp -a %{SOURCE2} .
# %%{name}-%%{version}-yarn.lock
cp -a %{SOURCE3} resources/server/src/landingpage/yarn.lock

# Readme file for QGIS server configuration and Lighttpd example
install -pm0644 %{SOURCE5} .

gzip ChangeLog

sed -i 's/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19 || 20 || 21 || 22"/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19 || 20 || 22 || 23 || 24"/' $(find "$PWD/.package-cache" | grep 'node_modules/@achrinza/node-ipc/package.json')
sed -i 's/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19 || 20 || 21 || 22"/"node": "8 || 9 || 10 || 11 || 12 || 13 || 14 || 15 || 16 || 17 || 18 || 19 || 20 || 22 || 23 || 24"/' $(find "$PWD/.package-cache" | grep 'node_modules/@achrinza/node-ipc/.yarn-metadata.json')

%build
%cmake \
      %{_cmake_skip_rpath} \
      %["%{?_lib}" == "lib64" ? "-D LIB_SUFFIX=64" : ""] \
      -D QGIS_LIB_SUBDIR=%{_lib} \
      -D QGIS_MANUAL_SUBDIR=/share/man \
      -D QGIS_CGIBIN_SUBDIR=%{_libexecdir}/%{name} \
      -D WITH_BINDINGS:BOOL=TRUE \
      -D BINDINGS_GLOBAL_INSTALL:BOOL=TRUE \
      -D WITH_GRASS8:BOOL=TRUE \
      -D GRASS_PREFIX8=`pkg-config --variable=prefix grass` \
      -D WITH_CUSTOM_WIDGETS:BOOL=TRUE \
      -D BUILD_TESTING:BOOL=FALSE \
      -D ENABLE_TESTS:BOOL=FALSE \
      -D WITH_EPT:BOOL=TRUE \
      -D WITH_PDAL:BOOL=TRUE \
      -D WITH_QSPATIALITE:BOOL=TRUE \
      -D WITH_QWTPOLAR:BOOL=TRUE \
      -D WITH_INTERNAL_QWTPOLAR:BOOL=FALSE \
      -D WITH_SERVER:BOOL=TRUE \
      -D WITH_3D:BOOL=TRUE \
      -D WITH_QSPATIALITE:BOOL=TRUE \
      -D WITH_SERVER_LANDINGPAGE_WEBAPP=ON \
      -G Ninja
export YARN_CACHE_FOLDER="$PWD/.package-cache"
%cmake_build

%install
%cmake_install

# Install desktop file without connecting proprietary file types
desktop-file-edit \
    --remove-mime-type="application/x-raster-ecw" \
    --remove-mime-type="application/x-raster-mrsid" \
    %{buildroot}%{_datadir}/applications/org.qgis.qgis.desktop

# Install MIME type definitions
install -d %{buildroot}%{_datadir}/mime/packages
install -pm0644 rpm/sources/qgis-mime.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

install -pd %{buildroot}%{_datadir}/pixmaps
install -pm0644 images/icons/%{name}-icon-512x512.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pm0644 images/icons/%{name}_icon.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -pm0644 images/icons/%{name}-mime-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}-mime.png

# Install basic QGIS Mapserver configuration for Apache
install -pd %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/httpd/conf.d/qgis-server.conf

# Remove install instructions
rm -f %{buildroot}%{_datadir}/%{name}/doc/INSTALL*

# Drop static library
rm -f %{buildroot}%{_prefix}/lib/liboauth2authmethod_static.a

%find_lang %{name} --with-qt

%check
# All tests basically run fine, but one fails using mock, while a different one fails when building with rpmbuild alone
#export LD_LIBRARY_PATH=%%{buildroot}%%{_libdir}
#xvfb-run -a -n 1 -s "-screen 0 1280x1024x24 -dpi 96" make Experimental
#rm -f %%{_bindir}%%{name}_bench

%files -f %{name}.lang
%license COPYING %{name}-%{version}-vendor-licenses.txt
%doc BUGS NEWS.md README.md Exception_to_GPL_for_Qt.txt ChangeLog.gz
# QGIS shows the following files in the GUI, including the license text
%doc %{_datadir}/%{name}/doc/
%dir %{_datadir}/%{name}/i18n/
%{_datadir}/%{name}/i18n/qgis_zh-Hans.qm
%{_datadir}/%{name}/i18n/qgis_zh-Hant.qm
%{_libdir}/lib%{name}_native.so.*
%{_libdir}/lib%{name}_app.so.*
%{_libdir}/lib%{name}_analysis.so.*
%{_libdir}/lib%{name}_core.so.*
%{_libdir}/lib%{name}_gui.so.*
%{_libdir}/lib%{name}_3d.so.*
%{_libdir}/%{name}/
%{_qt5_plugindir}/sqldrivers/libqsqlspatialite.so
%{_bindir}/%{name}
%{_bindir}/%{name}_process
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}/
%{_datadir}/mime/packages/qgis.xml
%{_metainfodir}/*.appdata.xml
%{_datadir}/pixmaps/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}/images/
%{_datadir}/%{name}/resources/
%{_datadir}/%{name}/svg/
%exclude %{_libdir}/libqgisgrass*.so.*
%exclude %{_libdir}/%{name}/plugins/libplugin_grass8.so
%exclude %{_libdir}/%{name}/plugins/libprovider_grass8.so
%exclude %{_libdir}/%{name}/plugins/libprovider_grassraster8.so
%exclude %{_libdir}/%{name}/server/
%exclude %{_libdir}/%{name}/grass/
%exclude %{_datadir}/%{name}/resources/server/

%files devel
%{_datadir}/%{name}/FindQGIS.cmake
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*.so
%{?_qt5_plugindir}/designer/libqgis_customwidgets.so*

%files grass
%{_libdir}/lib%{name}grass*.so.*
%{_libdir}/%{name}/plugins/libplugin_grass8.so
%{_libdir}/%{name}/plugins/libprovider_grass8.so
%{_libdir}/%{name}/plugins/libprovider_grassraster8.so
%{_libdir}/%{name}/grass/
%{_datadir}/%{name}/grass/

%files -n python3-qgis
%{_libdir}/libqgispython.so.*
%{_datadir}/%{name}/python/
%{python3_sitearch}/%{name}/
%{python3_sitearch}/PyQt5/uic/widget-plugins/
%exclude %{python3_sitearch}/%{name}/server/
%exclude %{python3_sitearch}/%{name}/_server.so

%files server
%doc %{name}-server-README.fedora
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}-server.conf
%{_bindir}/qgis_mapserver
%{_libdir}/%{name}/server/
%{_libdir}/lib%{name}_server.so.*
%{_libexecdir}/%{name}/
%{python3_sitearch}/%{name}/server/
%{python3_sitearch}/%{name}/_server.so
%{_datadir}/%{name}/resources/server/

%changelog
%autochangelog
