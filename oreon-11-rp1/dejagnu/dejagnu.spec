# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 87daefacd7958b4a69f88c6856dbd1634261963c414079d0c371f589cd66a2e3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: dejagnu
Epoch: 1
Version: 1.6.3
Release: 1%{?dist}
Summary: Front end for testing other programs
License: GPL-3.0-or-later AND GFDL-1.3-or-later
URL: https://www.gnu.org/software/dejagnu/
Source0: https://ftp.gnu.org/gnu/dejagnu/dejagnu-%{version}.tar.gz
Source1: dejagnu-1.6.3.tar.gz.sig
Source2: gpgkey-D231B45ECB0B7BD8F6E7A682CE9D6843AABACC90.gpg
Patch0: rhbz460153.patch
Patch1: tcl9.patch
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: expect
BuildRequires: texinfo
BuildRequires: make
BuildRequires: gnupg2

Requires: expect

%description
DejaGnu is an Expect/Tcl based framework for testing other programs.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure -v
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
chmod a-x %{buildroot}%{_datadir}/dejagnu/runtest.exp
%make_install install-man
install -D -m 644 doc/dejagnu.info %{buildroot}%{_infodir}/%{name}.info

%check
TMP=$(mktemp)
export SCREENDIR=$(mktemp -d)
(make check RUNTESTFLAGS="--ignore pr48155.exp stats.exp"; echo $?) >> $TMP
RESULT=$(tail -n 1 $TMP)
cat $TMP
rm -f $TMP
rm -rf $SCREENDIR
exit $RESULT

%files
%license COPYING
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/runtest
%{_bindir}/dejagnu
%{_datadir}/dejagnu
%{_includedir}/dejagnu.h
%{_mandir}/*/*
%{_infodir}/dejagnu*

%changelog
%autochangelog
