%global source0_hash 18ec63e28a42073db62e8fb59134b8bd410c29e8eb1d8ec1759efc9501fbf41a
Name:           osmpbf
Version:        1.8.0
Release:        1%{?dist}
Summary:        C library to read and write OpenStreetMap PBF files
License:        LGPL-3.0-or-later
URL:            https://github.com/openstreetmap/OSM-binary
Source0:        https://github.com/openstreetmap/OSM-binary/archive/v%{version}/OSM-binary-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
BuildRequires:  zlib-static
# /oreon:deps
%description
Osmpbf is a Java/C library to read and write OpenStreetMap PBF files.
PBF (Protocol buffer Binary Format) is a binary file format for OpenStreetMap
data that uses Google Protocol Buffers as low-level storage.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
This package contains tools that use %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir OSM-binary-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm %{buildroot}/%{_libdir}/libosmpbf.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n osmpbf-tools -f %{oreon_filedir}/osmpbf-tools.list
%files -n osmpbf-devel -f %{oreon_filedir}/osmpbf-devel.list

%changelog

%autochangelog
