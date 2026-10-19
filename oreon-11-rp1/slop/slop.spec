%global source0_hash a69a6e5c41d7fff1c6aa35b367a5c5a6dc98e621fa9a1908808d6308c2b40f4e
Name:       slop
Version:    7.7
Release:        4%{?dist}
Summary:        Command line tool to perform region SeLect OPeration with mouse
URL:        https://github.com/naelstrof/slop
License:    GPL-3.0-only
Source0:        https://github.com/naelstrof/slop/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%endif
Requires: libslopy = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libicu-devel
BuildRequires:  mesa-libEGL-devel
# /oreon:deps
%description
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

%package -n libslopy
Summary: Library to perform region SeLect OPeration with mouse
%description -n libslopy
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

This sub-package contains libslopy library.

%package -n libslopy-devel
Summary: Library to perform region SeLect OPeration with mouse
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n libslopy-devel
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

This sub-package contains development files for libslopy library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets -n libslopy
%oreon_autofiles libslopy usr/*/lib*.so.*
%oreon_autofiles libslopy-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libslopy -f %{oreon_filedir}/libslopy.list
%files -n libslopy-devel -f %{oreon_filedir}/libslopy-devel.list

%changelog

%autochangelog
