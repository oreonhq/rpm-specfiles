%define libselinuxver 3.10-1
%define libsepolver 3.10-1

Summary: SELinux policy compiler
Name: checkpolicy
Version: 3.10
Release: 1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz.asc
Source2: https://github.com/perfinion.gpg
# oreon url source checksums begin
%global source0_sha256 2d92951dfcb090d6179e7a23856622e0fcbc32be03bf1e60ace9dc9cbda11e59
%global source0_file checkpolicy-3.10.tar.gz
# oreon url source checksums end
# $ git clone https://github.com/fedora-selinux/selinux.git
# $ cd selinux
# $ git format-patch -N 3.10 -- checkpolicy
# $ i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
# Patch list end
BuildRequires: gcc
BuildRequires: make
BuildRequires: byacc bison flex flex-static libsepol-static >= %{libsepolver} libselinux-devel  >= %{libselinuxver}
BuildRequires: gnupg2

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/checkpolicy-3.10.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2d92951dfcb090d6179e7a23856622e0fcbc32be03bf1e60ace9dc9cbda11e59" || { echo "oreon: Source0 SHA256 mismatch for checkpolicy-3.10.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10-1
- Prepare for Oreon 11 (RP1)
