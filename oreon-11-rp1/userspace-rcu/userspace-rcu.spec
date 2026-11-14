# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2556b83adc0f9b3ac8024e613e17d014d04c4c49110604ce55fcb14eae32edd3

Name: userspace-rcu
Version: 0.15.7
Release: 1%{?dist}
Summary: Userspace RCU implementation
License: LGPL-2.1-or-later
URL: https://liburcu.org/
Source0: https://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

%description
Userspace RCU provides read-copy-update synchronization and lock-free data
structures for multithreaded applications.

Provides: liburcu = %{version}-%{release}

%package -n liburcu-devel
Summary: Development files for userspace RCU
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n liburcu-devel
Headers, libraries, and pkg-config files for developing with userspace RCU.

%prep
%oreon_sha256
%autosetup

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete

%check
%oreon_make check

%files
%license LICENSE
%doc ChangeLog README.md
%{_libdir}/liburcu*.so.*

%files -n liburcu-devel
%{_includedir}/urcu
%{_includedir}/urcu*.h
%{_libdir}/liburcu*.so
%{_libdir}/pkgconfig/liburcu*.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
