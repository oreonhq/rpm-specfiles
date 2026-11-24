# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9b81bfceef7fa9d02f9872e56a786f343dc58ef4b5713dce0d5c416e5b84cefa
%global source1_hash ac9f615c661372d32c83819b4302c1478910a26ae11dbaf2bead07d7e9ac982d
%global source2_hash 3ac69dbb7dfcd4f5e1898596f966586786c7a943574955256f51aea3613855e2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define libselinuxver 3.11-1
%define libsepolver 3.11-1

Summary: SELinux policy compiler
Name: checkpolicy
Version: 3.11
Release: 1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
VCS: git:https://github.com/SELinuxProject/selinux.git
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: bison
BuildRequires: flex
BuildRequires: libsepol-static >= %{libsepolver}
BuildRequires: openpgpverify

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.  
Only required for building policies.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n checkpolicy-%{version}

%build

%set_build_flags

%make_build LIBDIR="%{_libdir}"
cd test
%make_build LIBDIR="%{_libdir}"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%make_install LIBDIR="%{_libdir}"
install test/dismod ${RPM_BUILD_ROOT}%{_bindir}/sedismod
install test/dispol ${RPM_BUILD_ROOT}%{_bindir}/sedispol

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_mandir}/man8/checkpolicy.8*
%{_mandir}/man8/checkmodule.8*
%{_bindir}/sedismod
%{_bindir}/sedispol

%changelog
%autochangelog
