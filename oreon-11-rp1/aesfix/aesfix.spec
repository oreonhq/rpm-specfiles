%global source1_hash 9f61cce3cdd3d6aed6d5096303361317a9ecc2294fc44680a6db0dcebc2eda9e
%global source0_hash 7b177e876caee6aae48f0123102f11df6594a738483f9a47f2c76fe81cc045d4
Name:           aesfix
Version:        1.0.1
Release:        10%{?dist}
License:        BSD-3-Clause
Summary:        Correct bit errors in AES-128 key schedule
URL:            https://citp.princeton.edu/our-work/memory/
Source0:        https://citpsite.s3.amazonaws.com/memory-content/src/%{name}-%{version}.tar.gz
Source1:        https://citpsite.s3.amazonaws.com/memory-content/src/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-12E404FFD3C931F934052D06B8841A919D0FACE4.gpg
Source3:        aesfix.1
Patch1:         aesfix-10_add-GCC-hardening.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
The aesfix tool illustrates a technique for correcting bit errors in an
AES key schedule. This program is limited to AES-128 key schedules
and it can only correct unidirectional 1->0 bit errors.
For the most part it has been optimized for readability rather than
performance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#check signature
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}

%build

%set_build_flags
%make_build
%install
install -Dp -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m644 %{SOURCE3} %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
