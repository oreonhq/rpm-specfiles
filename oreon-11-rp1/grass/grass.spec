%global source0_hash none

%global shortver 84
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:		grass
Version:	8.4.2
Release:	4%{?dist}
Summary:	GRASS GIS - Geographic Resources Analysis Support System

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

%if 0%{?rhel} >= 7
%define __python %{__python3}
%global python3_version_nodots 36
%global main_python3 1
%endif

# Note that the bcond macros are named for the CLI option they create.
# "%%bcond_without" means "ENABLE by default and create a --without option"
%bcond_without python3

# GRASS GIS addon reuses the compiler flags originating from rpmbuild environment,
# hence disabling package-notes plugin
%undefine _package_note_file

License:	GPL-2.0-or-later
URL:		https://grass.osgeo.org
Source0:	https://grass.osgeo.org/%{name}%{shortver}/source/%{name}-%{version}.tar.gz

# fix pkgconfig file
Patch 0:	grass-pkgconfig.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:	bison
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel, lapack-devel
%endif
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	fftw-devel
BuildRequires:	flex
BuildRequires:	freetype-devel
BuildRequires:	gcc-c++
BuildRequires:	gdal-devel
BuildRequires:	geos-devel
BuildRequires:	gettext
BuildRequires:	laszip-devel
BuildRequires:	libappstream-glib
BuildRequires:	libpng-devel
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires:	postgresql-devel
%else
BuildRequires:	libpq-devel
%endif
BuildRequires:	libtiff-devel
BuildRequires:	libXmu-devel
BuildRequires:	libzstd-devel
BuildRequires:	make
BuildRequires:	mariadb-connector-c-devel openssl-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	mesa-libGLU-devel
BuildRequires:	netcdf-devel
BuildRequires:	PDAL
BuildRequires:	PDAL-devel
BuildRequires:	PDAL-libs
BuildRequires:	proj-devel
BuildRequires:	python3
%if 0%{?rhel} == 7
# EPEL7
BuildRequires:	python%{python3_version_nodots}-dateutil
%else
BuildRequires:	python3-dateutil
%endif
BuildRequires:	python3-devel
%if 0%{?rhel} == 7
# EPEL7
BuildRequires:	python%{python3_version_nodots}-numpy
%else
BuildRequires:	python3-numpy
%endif
BuildRequires:	python3-pillow
BuildRequires:	readline-devel
BuildRequires:	sqlite-devel
BuildRequires:	subversion
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel

Requires:	bzip2-libs
Requires:	geos
Requires:	libzstd
Requires:	PDAL
Requires:	PDAL-libs
Requires:	python3
%if 0%{?rhel} == 7
# EPEL7
Requires:	python%{python3_version_nodots}-dateutil
%else
Requires:	python3-dateutil
%endif
%if 0%{?rhel} == 7
# EPEL7
Requires:	python%{python3_version_nodots}-numpy
%else
Requires:	python3-numpy
%endif
Requires:	python3-wxpython4

%if "%{_lib}" == "lib"
%global cpuarch 32
%else
%global cpuarch 64
%endif
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
GRASS (Geographic Resources Analysis Support System) is a Geographic
Information System (GIS) used for geospatial data management and
analysis, image processing, graphics/maps production, spatial
modeling, and visualization. GRASS is currently used in academic and
commercial settings around the world, as well as by many governmental
agencies and environmental consulting companies.

%package libs
Summary:	GRASS GIS runtime libraries

%description libs
GRASS GIS runtime libraries

%package gui
Summary:	GRASS GIS GUI
Requires:	%{name}%{?isa} = %{version}-%{release}

%description gui
GRASS GIS GUI

%package devel
Summary:	GRASS GIS development headers
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
GRASS GIS development headers

%prep
%setup -q
%patch 0 -p1 -b.libdir

# Correct mysql_config query
sed -i -e 's/--libmysqld-libs/--libs/g' configure

%if %{with flexiblas}
sed -i -e 's/-lblas/-lflexiblas/g' -e 's/-llapack/-lflexiblas/g' configure
%endif

# Fixup shebangs
find -name \*.pl | xargs sed -i -e 's,#!/usr/bin/env perl,#!%{__perl},'

%build
%configure \
	--prefix=%{_libdir} \
	--with-blas \
%if %{with flexiblas}
	--with-blas-includes=%{_includedir}/flexiblas \
%endif
	--with-bzlib \
	--with-cairo \
	--with-cairo-ldflags=-lfontconfig \
	--with-cxx \
	--with-fftw \
	--with-freetype \
	--with-freetype-includes=%{_includedir}/freetype2 \
	--with-gdal=%{_bindir}/gdal-config \
	--with-geos=%{_bindir}/geos-config \
	--with-lapack \
%if %{with flexiblas}
	--with-lapack-includes=%{_includedir}/flexiblas \
%endif
%if 0%{?rhel} > 7
	--with-mysql=no \
%else
	--with-mysql \
%endif
	--with-mysql-includes=%{_includedir}/mysql \
%if (0%{?fedora} >= 27)
	--with-mysql-libs=%{_libdir} \
%else
	--with-mysql-libs=%{_libdir}/mysql \
%endif
	--with-netcdf=%{_bindir}/nc-config \
	--with-nls \
	--with-odbc \
	--with-opengl \
	--with-openmp \
	--with-pdal \
	--with-png \
	--with-postgres \
	--with-postgres-includes=%{_includedir}/pgsql \
	--with-proj-share=%{_datadir}/proj \
	--with-readline \
	--with-regex \
	--with-tiff \
	--with-wxwidgets=%{_bindir}/wx-config \
	--with-zstd

# .package_note hack for RHBZ #2084342 and RHBZ #2102895
sed -i "s+ -Wl,-dT,${RPM_BUILD_DIR}/grass-%{version}/.package_note-grass-%{version}-%{release}.%{_arch}.ld++g" include/Make/Platform.make

make %{?_smp_mflags}

# by default, grass will be installed to /usr/grass-%%{version}
# this is not FHS compliant: hide grass-%%{version} in %%{libdir}
%install
%make_install \
	DESTDIR=%{buildroot} \
	prefix=%{_libdir} \
	UNIX_BIN=%{_bindir} \
	GISBASE_RUNTIME=%{_libdir}/%{name}%{shortver}

# libraries and headers are in GISBASE = %%{_libdir}/%%{name}
# keep them in GISBASE

# fix paths in grass.pc
sed -i -e 's|%{_libdir}/%{name}-%{version}|%{_libdir}/%{name}%{shortver}|g' \
	%{name}.pc

mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -p -m 644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig

# Create multilib header
mv %{buildroot}%{_libdir}/%{name}%{shortver}/include/%{name}/config.h \
   %{buildroot}%{_libdir}/%{name}%{shortver}/include/%{name}/config-%{cpuarch}.h
echo '#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "grass/config-32.h"
#else
#if __WORDSIZE == 64
#include "grass/config-64.h"
#else
#error "Unknown word size"
#endif
#endif' > %{buildroot}%{_libdir}/%{name}%{shortver}/include/%{name}/config.h
chmod 644 %{buildroot}%{_libdir}/%{name}%{shortver}/include/%{name}/config.h

# Make man pages available on the system, convert to utf8 and avoid name conflict
mkdir -p %{buildroot}%{_mandir}/man1
for man in $(ls %{buildroot}%{_libdir}/%{name}%{shortver}/docs/man/man1/*.1)
do
	iconv -f iso8859-1 -t utf8 $man > %{buildroot}%{_mandir}/man1/$(basename $man)"%{name}"
done

# symlink docs from GISBASE to standard system location
mkdir -p %{buildroot}%{_docdir}
# append shortver to destination since man pages are unversioned
ln -s %{_libdir}/%{name}%{shortver}/docs %{buildroot}%{_docdir}/%{name}%{shortver}

# Make desktop, appdata and icon files available on the system
mv %{buildroot}%{_libdir}/%{name}%{shortver}/share/* %{buildroot}%{_datadir}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.osgeo.%{name}.appdata.xml

# Cleanup: nothing to do
#rm -rf %%{buildroot}%%{_prefix}/%%{name}-%%{version}

# Finally move entire tree to shortver subdir
#mv %%{buildroot}%%{_libdir}/%%{name}-%%{version} %%{buildroot}%%{_libdir}/%%{name}%%{shortver}

# rpm macro for version checking (not from buildroot!)
mkdir -p ${RPM_BUILD_ROOT}%{macrosdir}
cat > ${RPM_BUILD_ROOT}%{macrosdir}/macros.%{name} <<EOF
%%%{name}_version %{version}
EOF

# Add custom lib path to ld.conf.so.d
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >  %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf<<EOF
%{_libdir}/%{name}%{shortver}/lib
EOF

%if 0%{?rhel} && 0%{?rhel} == 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
	/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
	/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%exclude %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%exclude %{_libdir}/%{name}%{shortver}/driver/db/*
%exclude %{_libdir}/%{name}%{shortver}/lib
%exclude %{_libdir}/%{name}%{shortver}/include
%exclude %{_libdir}/%{name}%{shortver}/gui
%{_libdir}/%{name}%{shortver}
%{_bindir}/*
%{_datadir}/metainfo/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*
%{_docdir}/%{name}%{shortver}

%files libs
%license AUTHORS COPYING GPL.TXT
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%{_libdir}/%{name}%{shortver}/lib/*.so
%dir %{_libdir}/%{name}%{shortver}/driver
%dir %{_libdir}/%{name}%{shortver}/driver/db
%{_libdir}/%{name}%{shortver}/driver/db/*

%files gui
%{_libdir}/%{name}%{shortver}/gui

%files devel
%doc TODO doc/* CONTRIBUTING.md
%{macrosdir}/macros.%{name}
%{_libdir}/pkgconfig/*
%dir %{_libdir}/%{name}%{shortver}/lib
%{_libdir}/%{name}%{shortver}/include

%changelog
%autochangelog
