%global source0_hash 5dcb4db3b2340f81f601ce86d8d76b69e34d70f84f804192c901e4b7f84d5fb0
Name:      libnumbertext
Version:   1.0.11
Release:        1%{?dist}
Summary:        Number to number name and money text conversion library
License:   ( LGPL-3.0-or-later OR BSD-3-Clause ) AND ( LGPL-3.0-or-later OR CC-BY-SA-3.0 )
URL:       https://github.com/Numbertext/libnumbertext
Source0:        https://github.com/Numbertext/libnumbertext/releases/download/%{version}/libnumbertext-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package devel
Requires: libnumbertext = %{version}-%{release}
Summary: Files for developing with libnumbertext
%description devel
Includes and definitions for developing with libnumbertext

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libnumbertext-1.0.11
%oreon_prep
%build

autoreconf -v --install --force
%configure --disable-silent-rules --disable-static --disable-werror --with-pic
%make_build
%check

make check
%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnumbertext-devel -f %{oreon_filedir}/libnumbertext-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.11-10
- Import
