%global source0_hash e9355e021b82dacb260ac98218b53c9ea8010d83bc538f67b0b623890780b97e
%global debug_package %{nil}
Name:           dtkcommon
Version:        6.7.50
Release:        1%{?dist}
Summary:        A public project for building DTK Library
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
A public project for building DTK Library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtkcommon-devel -f %{oreon_filedir}/dtkcommon-devel.list

%changelog

%autochangelog
