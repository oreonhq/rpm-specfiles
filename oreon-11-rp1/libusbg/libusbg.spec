%global source0_hash 23d72c415ffd80d752efccc9bb5a6afdece6a83a31975344ef31a4967d189e3c

Name:          libusbg
Version:       0.3.0
Release:       4%{?dist}
Summary:       Library for USB gadget-configfs userspace functionality
License:       LGPL-2.1-or-later

URL:           https://github.com/libusbgx/libusbgx
Source0:       %{url}/archive/%{name}x-v%{version}.tar.gz

BuildRequires: doxygen
BuildRequires: gcc gcc-c++
BuildRequires: libtool autoconf automake
BuildRequires: libconfig-devel
BuildRequires: make

%description
libusbg is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

It provides routines for creating and parsing USB gadget devices using
the configfs API. Currently, all USB gadget configfs functions that can
be enabled in kernel release 3.11 (Linux for Workgroups!) are supported.

%package utils
Summary: Utilities for USB gadget devices
# Automatically converted from old format: GPLv2+ - review is highly recommended.
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

%autosetup -p1 -n %{name}x-%{name}x-v%{version}

%build
autoreconf -vif
%configure --disable-static

%{make_build}

%install
%{make_install}

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%check
make check

%files
%license COPYING.LGPL
%doc README AUTHORS ChangeLog
%{_libdir}/libusbgx.so.3*

%files utils
%doc COPYING
%{_bindir}/gadget*
%{_bindir}/show*

%files devel
%{_includedir}/usbg
%{_libdir}/libusbgx.so
%{_libdir}/pkgconfig/libusbgx.pc
%{_libdir}/cmake/LibUsbgx/

%changelog
%autochangelog
