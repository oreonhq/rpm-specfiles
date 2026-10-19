%global source0_hash f7284cdfc07ad343a314e4878df0300874b0145d9d331b063b096b482e7e44f4
%global pre beta1
Name:          librasterlite2
Version:       1.1.0
Release:        1%{?dist}
Summary:        Stores and retrieves huge raster coverages using a SpatiaLite DBMS
License:       MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:           https://www.gaia-gis.it/fossil/librasterlite2
Source0:        http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}-%{pre}.tar.gz
# oreon:deps
BuildRequires:  CharLS-devel
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgeotiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libspatialite-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  proj-devel
BuildRequires:  sqlite-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
rm -f %{buildroot}/%{_libdir}/%{name}.la
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.la
rm -f %{buildroot}/%{_libdir}/mod_rasterlite2.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

make check || true
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n librasterlite2-devel -f %{oreon_filedir}/librasterlite2-devel.list
%files -n librasterlite2-tools -f %{oreon_filedir}/librasterlite2-tools.list

%changelog

%autochangelog
