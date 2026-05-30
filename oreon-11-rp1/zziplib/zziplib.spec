%global source0_hash feaeee7c34f18aa27bd3da643cc6a47d04d2c41753a59369d09102d79b9b0a31

# FTBFS with GCC 14, reported upstream, no fix yet
# https://bugzilla.redhat.com/show_bug.cgi?id=2256917

Summary: Lightweight library to easily extract data from zip files
Name: zziplib
Version: 0.13.78
Release: 4%{?dist}
License: LGPL-2.0-or-later OR MPL-1.1
URL: http://zziplib.sourceforge.net/
Source:        https://github.com/gdraheim/zziplib/archive/v%{version}.tar.gz#/zziplib-%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-interpreter
BuildRequires: python3
BuildRequires: python3-rpm-macros
BuildRequires: zip
BuildRequires: xmlto
BuildRequires: zlib-devel
BuildRequires: SDL-devel
BuildRequires: pkgconfig
BuildRequires: cmake

%description
The zziplib library is intentionally lightweight, it offers the ability to
easily extract data from files archived in a single zip file. Applications
can bundle files into a single zip archive and access them. The implementation
is based only on the (free) subset of compression with the zlib algorithm
which is actually used by the zip/unzip tools.

%package utils
Summary: Utilities for the zziplib library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
The zziplib library is intentionally lightweight, it offers the ability to
easily extract data from files archived in a single zip file. Applications
can bundle files into a single zip archive and access them. The implementation
is based only on the (free) subset of compression with the zlib algorithm
which is actually used by the zip/unzip tools.

This packages contains all the utilities that come with the zziplib library.

%package devel
Summary: Development files for the zziplib library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: zlib-devel
Requires: SDL-devel

%description devel
The zziplib library is intentionally lightweight, it offers the ability to
easily extract data from files archived in a single zip file. Applications
can bundle files into a single zip archive and access them. The implementation
is based only on the (free) subset of compression with the zlib algorithm
which is actually used by the zip/unzip tools.

This package contains files required to build applications that will use the
zziplib library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
# TODO: Please submit an issue to upstream (rhbz#2381654)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -B "%{_vpath_builddir}"

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc docs/COPYING* ChangeLog README TODO
%{_libdir}/*.so.*
%exclude %{_datadir}/zziplib/*.cmake
%exclude %{_libdir}/cmake/zziplib/*.cmake

%files utils
%{_bindir}/*

%files devel
%doc docs/README.SDL docs/*.htm
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.78-4
- Import
