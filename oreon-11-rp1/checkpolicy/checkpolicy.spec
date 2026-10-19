%global source1_hash ac9f615c661372d32c83819b4302c1478910a26ae11dbaf2bead07d7e9ac982d
%global source0_hash 9b81bfceef7fa9d02f9872e56a786f343dc58ef4b5713dce0d5c416e5b84cefa
%global source2_key_fpr 63191CE94183098689CAB8DB7EF137EC935B0EAF
%define libselinuxver 3.11-1
%define libsepolver 3.11-1
Summary:        SELinux policy compiler
Name: checkpolicy
Version: 3.11
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/checkpolicy-%{version}.tar.gz.asc
Source2:        bachradsusi.gpg
# oreon:deps
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-static
BuildRequires:  make
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10-1
- Prepare for Oreon 11 (RP1)
