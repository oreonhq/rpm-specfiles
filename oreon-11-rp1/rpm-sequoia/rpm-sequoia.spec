# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 64de2578534e2d46079050ba79d4c1a462d7aa2cde01e619ecf99b7084e58044
%global source1_hash d2d190011cd3f33c6ad270ff23bf05586c7c9063ff0ad9c790272407f173e2d6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: rpm-sequoia
Version: 1.10.3
Release: 1%{?dist}
Summary: RPM OpenPGP backend
License: LGPL-2.0-or-later
URL: https://github.com/rpm-software-management/rpm-sequoia
Source0: https://github.com/rpm-software-management/rpm-sequoia/archive/refs/tags/v%{version}.tar.gz
Source1: rpm-sequoia-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: rustc
BuildRequires: cargo
BuildRequires: pkgconf
BuildRequires: clang
BuildRequires: openssl-devel >= 1:4.0
BuildRequires: patchelf

%description
rpm-sequoia is the OpenPGP backend used by rpm.

%package devel
Summary: RPM OpenPGP backend
Requires: rpm-sequoia%{?_isa} = %{version}-%{release}

%description devel
rpm-sequoia is the OpenPGP backend used by rpm.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n rpm-sequoia-%{version} -p1
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
PREFIX=%{_prefix} LIBDIR=%{_libdir} %oreon_cargo_build --no-default-features --features crypto-openssl

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
so=$(find target/release -name 'librpm_sequoia.so' -type f | head -1)
install -p -m 755 "$so" %{buildroot}%{_libdir}/librpm_sequoia.so.1
ln -sf librpm_sequoia.so.1 %{buildroot}%{_libdir}/librpm_sequoia.so
patchelf --set-soname librpm_sequoia.so.1 %{buildroot}%{_libdir}/librpm_sequoia.so.1
install -p -m 644 target/release/rpm-sequoia.pc %{buildroot}%{_libdir}/pkgconfig/rpm-sequoia.pc
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt

%files devel -f %{_builddir}/%{name}-devel.files
