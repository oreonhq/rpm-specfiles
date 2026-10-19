%global source0_hash 88b30feace372c4a61e6adb2534791c0cfba6123ebcca7f59bbb76580d4a6915
Name:		can-utils
Version:	2025.01
Release:        5%{?dist}
Summary:        SocketCAN user space utilities and tools
License:	GPL-2.0-only AND (GPL-2.0-only OR LicenseRef-Callaway-BSD)
URL:		https://github.com/linux-can/can-utils
Source0:        https://github.com/linux-can/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glibc-devel
# /oreon:deps
%description
CAN is a message-based network protocol designed for vehicles originally
created by Robert Bosch GmbH. SocketCAN is a set of open source CAN
drivers and a networking stack contributed by Volkswagen Research to
the Linux kernel.

This package contains some user space utilities for Linux SocketCAN subsystem.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build
head -39 asc2log.c | tail -37 | cut -c4- > COPYING
%install
%cmake_install
%oreon_autofiles can-utils-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n can-utils-devel -f %{oreon_filedir}/can-utils-devel.list

%changelog

%autochangelog
