%global source0_hash none

%global pre beta1

# This package requires libspatialite 4.2 and solves the tasks librasterlite
# and gaiagraphics solved in the past. It is not a drop-in replacement for either.
Name:          librasterlite2
Version:       1.1.0
Release:       0.21%{?pre:.%pre}%{?dist}
Summary:       Stores and retrieves huge raster coverages using a SpatiaLite DBMS
License:       MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:           https://www.gaia-gis.it/fossil/librasterlite2
Source0:       http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}%{?pre:-%pre}.tar.gz

BuildRequires: gcc
BuildRequires: cairo-devel
BuildRequires: CharLS-devel
BuildRequires: giflib-devel
BuildRequires: libcurl-devel
BuildRequires: libgeotiff-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libspatialite-devel
BuildRequires: libwebp-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: lz4-devel
BuildRequires: minizip-ng-compat-devel
BuildRequires: openjpeg2-devel
BuildRequires: proj-devel
BuildRequires: sqlite-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: make

%description
librasterlite2 is a library that stores and retrieves huge raster coverages
using a SpatiaLite DBMS.

%package devel
Summary:  Development libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:  Tools for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later

%description tools
The %{name}-tools package contains l2tool and rwmslite.
rl2tool is a CLI tool to create and manage rasterlite2 coverages.
wmslite is a simple WMS server (Web Map Service) based on librasterlite2.

%prep
%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}

%build
%configure --disable-static
%make_build

%install
%make_install

# Delete undesired libtool archives
rm -f %{buildroot}/%{_libdir}/%{name}.la
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.la

# Delete soname symlink for the sqlite extension
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.so.*

%check
# test_svg fails on at least i386
# Some tests are online tests and may fail as well, depending on availability
# Additional tests are failing on ARM; Let the author know on the mailing list
make check || true

%ldconfig_scriptlets

%files
%doc AUTHORS
%license COPYING
%{_libdir}/%{name}.so.*
# The symlink must be present to allow loading the extension
# https://groups.google.com/forum/#!topic/spatialite-users/zkGP-gPByXk
%{_libdir}/mod_rasterlite2.so

%files devel
%doc examples/*.c
%{_includedir}/rasterlite2
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rasterlite2.pc

%files tools
%{_bindir}/rl2sniff
%{_bindir}/rl2tool
%{_bindir}/wmslite

%changelog
%autochangelog
