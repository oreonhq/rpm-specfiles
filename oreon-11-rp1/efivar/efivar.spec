# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c9edd15f2eeeea63232f3e669a48e992c7be9aff57ee22672ac31f5eca1609a6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           efivar
Version:        39
Release:        1%{?dist}
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1-only
URL:            https://github.com/rhboot/efivar
Requires:       %{name}-libs = %{version}-%{release}
ExclusiveArch:  %{efi}

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  compiler-rt
BuildRequires:  efi-srpm-macros
BuildRequires:  git
BuildRequires:  glibc-static
BuildRequires:  libabigail
BuildRequires:  make
BuildRequires:  mandoc
Source0:        https://github.com/rhboot/efivar/archive/refs/tags/%{version}.tar.gz#/efivar-%{version}.tar.gz

Patch0001: 0001-ABI-update-for-newer-libabigail.patch
Patch0002: 0002-ABI-update-after-glibc-changes.patch
Patch0003: 0003-ABI-update-after-glibc-changes.patch
Patch0004: 0004-efivarfs-Update-a-file-variable-store-On-SetVariable.patch

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package libs
Summary: Library to manage UEFI variables

%description libs
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary: Development headers for libefivar
Requires: %{name}-libs = %{version}-%{release}

%description devel
development headers required to use libefivar.

%prep
%oreon_sha256
%setup -q -n %{name}-%{version}
git init
git config user.email "packaging@oreonhq.com"
git config user.name "Oreon Packaging"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null
git config --unset user.email
git config --unset user.name

%build
%define _lto_cflags %{nil}

make CC=%{__cc} COMPILER=clang HOSTCC=%{__cc} LIBDIR=%{_libdir} BINDIR=%{_bindir} OPTIMIZE="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
%makeinstall CC=%{__cc} COMPILER=clang HOSTCC=%{__cc} OPTIMIZE="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
install -m 0644 src/abignore %{buildroot}%{_includedir}/efivar/.abignore

%check
%ifarch x86_64
make CC=%{__cc} COMPILER=clang HOSTCC=%{__cc} OPTIMIZE="$RPM_OPT_FLAGS" abicheck LDFLAGS="$RPM_LD_FLAGS"
%endif

%ldconfig_scriptlets libs

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md
%{_bindir}/efivar
%{_bindir}/efisecdb
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files libs
%license COPYING
%{_libdir}/*.so.*

%changelog
%autochangelog
