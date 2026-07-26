%global source0_hash 3be2444ab6ea0042a640e8f3282c7931e2570cd8d41af80ba583a14d8088b84b

Name:		libsysstat
Version:	1.1.0
Release:	4%{?dist}
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:	Library used to query system info and statistics
Url:		http://www.lxde.org
Source0:	https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  lxqt-build-tools >= 0.6.0

%description
Library used to query system info and statistics

%package devel
Summary:	Devel files for libsysstat
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Sysstat libraries for development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS COPYING
%{_libdir}/libsysstat-qt6.so.1
%{_libdir}/libsysstat-qt6.so.%{version}

%files devel
%dir %{_includedir}/sysstat-qt6/
%dir %{_datadir}/cmake/sysstat-qt6/
%{_includedir}/sysstat-qt6/*
%{_datadir}/cmake/sysstat-qt6/*
%{_libdir}/pkgconfig/sysstat-qt6.pc
%{_libdir}/libsysstat-qt6.so

%changelog
%autochangelog
