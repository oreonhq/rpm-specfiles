# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e41af2d7d36a6ab67639ecbd5c1012aa20b2b464bf5cfbdac60e7eb37bfe58de
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Cornelis PSM2 Libraries
Name: libpsm2
Version: 12.0.1
Release:        %{autorelease}
License: BSD-3-Clause OR GPL-2.0-only
URL: https://github.com/cornelisnetworks/opa-psm2/

Source0: https://github.com/cornelisnetworks/opa-psm2/archive/refs/tags/PSM2_%{version}.tar.gz

ExclusiveArch: x86_64
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: libuuid-devel
BuildRequires: numactl-devel
BuildRequires: systemd
BuildRequires: make
Obsoletes: hfi1-psm < 1.0.0

%package devel
Summary: Development files for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel

%package compat
Summary: Compat library for Cornelis PSM2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd-udev

%global _privatelibs libpsm_infinipath[.]so[.]1.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
The PSM2 messaging API is a low-level user-level communications interface for
the Cornelis Omni-Path family of products.
PSM2 users are enabled with mechanisms necessary to implement higher level
communications interfaces in parallel environments.

%description devel
Development files for the Cornelis PSM2 library

%description compat
Support for MPIs linked with PSM versions < 2

%patchlist
0001-Fix-strlcat-multiple-definition-build-error.patch
0002-Fix-unaligned-heap-allocations-of-aligned-structs.patch
0003-Fix-missing-memset-zero-caused-by-unaligned-heap-all.patch
0004-Update-copyright-URL-branding-in-libpsm2-specfile.patch
9000-Apply-CFLAGS-to-assembly-file-compilation.patch

%prep
%oreon_sha256
%autosetup -p1 -n opa-psm2-PSM2_%{version}

%build
%{set_build_flags}
%{make_build} WERROR=

%install
%make_install DISTRO=%{?rhel:rhel}%{!?rhel:fedora}
rm -f %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libpsm2.so.2.*
%{_libdir}/libpsm2.so.2
%if 0%{?rhel} >= 8
%{_udevrulesdir}/40-psm.rules
%endif

%files devel
%{_libdir}/libpsm2.so
%{_includedir}/psm2.h
%{_includedir}/psm2_mq.h
%{_includedir}/psm2_am.h
%{_includedir}/hfi1diag

%files compat
%{_libdir}/psm2-compat
%{_udevrulesdir}/40-psm-compat.rules
%{_prefix}/lib/libpsm2
%if 0%{?fedora} || 0%{?oreon}
%{_prefix}/lib/modprobe.d/libpsm2-compat.conf
%endif
%if 0%{?rhel} >= 8
%{_sysconfdir}/modprobe.d/libpsm2-compat.conf
%endif

%changelog
%autochangelog
