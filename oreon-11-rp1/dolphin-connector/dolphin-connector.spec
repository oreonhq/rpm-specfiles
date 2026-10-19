%global source0_hash b7d9ad1d73b4a33b86dc8e7af5749d33b5e121588ad8bbf499bb63e7901aa5a2
Name:           dolphin-connector
Version:        1.2
Release:        1%{?dist}
Summary:        Simple MySQL C API wrapper for C++
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/poetinha/dolphin-connector
Source0:        https://github.com/poetinha/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
# /oreon:deps
%description
Dolphin Connector is a simple MySQL C API wrapper for C++.

It is originally designed to be as efficient as is possible,
and makes no use of exceptions.

%package devel
Summary: Development files for Dolphin Connector
Requires: %{name} = %{version}-%{release}
Requires: mariadb-connector-c-devel
Requires: boost-devel
%description devel
Dolphin Connector development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

./autogen.sh
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f sample/Makefile*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dolphin-connector-devel -f %{oreon_filedir}/dolphin-connector-devel.list

%changelog

%autochangelog
