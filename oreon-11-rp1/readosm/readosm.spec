%global source0_hash db7c051d256cec7ecd4c3775ab9bc820da5a4bf72ffd4e9f40b911d79770f145
%bcond autoreconf 1
Name:           readosm
Version:        1.1.0a
%global so_version 1
Release:        1%{?dist}
Summary:        Library to extract valid data from within an Open Street Map input file
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
SourceLicense:  %{shrink:
                (%{license}) AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Libtool-exception AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                X11
                }
Source0:        https://www.gaia-gis.it/gaia-sins/readosm-sources/readosm-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/readosm
%if %{with autoreconf}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
ReadOSM is a simple library intended for extracting the contents from 
Open Street Map files: both input formats (.osm XML based and .osm.pbf based
on Google's Protocol Buffer serialization) are indifferently supported.

%package devel
Summary:        Development libraries and headers for ReadOSM
Requires:       readosm%{?_isa} = %{version}-%{release}
%description devel
The readosm-devel package contains libraries and header files for
developing applications that use ReadOSM.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static

%build

%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n readosm-devel -f %{oreon_filedir}/readosm-devel.list

%changelog

%autochangelog
