%global source0_hash be1fd8e35599cb7de179decbd0633c121d11a2dcb9cc193ff5c590bd0d480483
%global debug_package %{nil}
Name: mdns
Version: 1.4.3
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
Summary:        Cross-platform mDNS/DNS-SD library in C
URL: https://github.com/mjansson/mdns
Source0:        https://github.com/mjansson/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1: mdns-1.4-cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description

%package devel
Summary: Header-only mDNS/DNS-SD library in C
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__cmake_builddir}/bin/mdns_example
%files -f %{oreon_filedir}/main.list
%files -n mdns-devel -f %{oreon_filedir}/mdns-devel.list

%changelog

%autochangelog
