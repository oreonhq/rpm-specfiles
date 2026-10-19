%global source0_hash e41af2d7d36a6ab67639ecbd5c1012aa20b2b464bf5cfbdac60e7eb37bfe58de
Summary:        Intel PSM Libraries
Name: libpsm2
Version: 12.0.1
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD OR GPL-2.0-only
URL: https://github.com/cornelisnetworks/opa-psm2/
Source0:        https://github.com/cornelisnetworks/opa-psm2/archive/refs/tags/PSM2_%{version}.tar.gz#/libpsm2-12.0.1.tar.gz
ExclusiveArch: x86_64
Obsoletes: hfi1-psm < 1.0.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  systemd
# /oreon:deps
%package devel
Summary: Development files for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel
%package compat
Summary: Compat library for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd-udev
%global _privatelibs libpsm_infinipath[.]so[.]1.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
%description
The PSM Messaging API, or PSM API, is the low-level
user-level communications interface for the Intel OPA
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%description devel
Development files for the Intel PSM library

%description compat
Support for MPIs linked with PSM versions < 2

%patchlist
# upstream commits PSM2_12.0.1..master
0001-Fix-strlcat-multiple-definition-build-error.patch
0002-Fix-unaligned-heap-allocations-of-aligned-structs.patch

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir opa-psm2-PSM2_%{version}
%oreon_prep
%build

%{set_build_flags}
%{make_build} WERROR=
%install
%make_install DISTRO=%{?rhel:rhel}%{!?rhel:fedora}
rm -f %{buildroot}%{_libdir}/*.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libpsm2-devel -f %{oreon_filedir}/libpsm2-devel.list
%files -n libpsm2-compat -f %{oreon_filedir}/libpsm2-compat.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.0.1-1
- Import
