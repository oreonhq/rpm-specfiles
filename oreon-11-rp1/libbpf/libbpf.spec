# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b7a1e685f90f6a63ead0dd85d053694b222975da8d09c1a966041cff6f0055ff

Name:           libbpf
Version:        1.8.0
Release:        1%{?dist}
Summary:        Library for loading and managing eBPF programs
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://github.com/libbpf/libbpf
Source0:        https://github.com/libbpf/libbpf/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel

%description
libbpf provides a stable userspace API for loading, verifying, and managing
eBPF programs and maps.

%package devel
Summary:        Development files for libbpf
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kernel-headers
Requires:       pkgconfig(libelf)
Requires:       pkgconfig(zlib)

%description devel
Headers and libraries for developing applications that use libbpf.

%package static
Summary:        Static library for libbpf
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static library for developing applications that use libbpf.

%global make_flags PREFIX=%{_prefix} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir} \
    DESTDIR=%{buildroot} OBJDIR=%{_vpath_builddir} \
    CFLAGS="%{build_cflags} -fPIC" LDFLAGS="%{build_ldflags}" NO_PKG_CONFIG=1

%prep
%oreon_sha256
%autosetup

%build
%make_build -C src %{make_flags}

%install
%make_install -C src %{make_flags}

%check
test -s %{_vpath_builddir}/libbpf.so
readelf -d %{_vpath_builddir}/libbpf.so | grep -q 'SONAME.*libbpf.so.1'

%ldconfig_scriptlets

%files
%license LICENSE LICENSE.BSD-2-Clause LICENSE.LGPL-2.1
%{_libdir}/libbpf.so.1*

%files devel
%{_includedir}/bpf/
%{_libdir}/libbpf.so
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%changelog
%autochangelog
