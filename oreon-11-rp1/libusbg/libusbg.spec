%global source0_hash 23d72c415ffd80d752efccc9bb5a6afdece6a83a31975344ef31a4967d189e3c
Name:          libusbg
Version:       0.3.0
Release:        1%{?dist}
Summary:        Library for USB gadget-configfs userspace functionality
License:       LGPL-2.1-or-later
URL:           https://github.com/libusbgx/libusbgx
Source0:        https://github.com/%{name}x/%{name}x/archive/%{name}x-v%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libusbg is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

It provides routines for creating and parsing USB gadget devices using
the configfs API. Currently, all USB gadget configfs functions that can
be enabled in kernel release 3.11 (Linux for Workgroups!) are supported.

%package utils
Summary: Utilities for USB gadget devices
License: GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Utilities for USB gadget devices

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}x-%{name}x-v%{version}
%oreon_prep
%build

autoreconf -vif
%configure --disable-static
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name "*.la" -delete
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libusbg-utils -f %{oreon_filedir}/libusbg-utils.list
%files -n libusbg-devel -f %{oreon_filedir}/libusbg-devel.list

%changelog

%autochangelog
