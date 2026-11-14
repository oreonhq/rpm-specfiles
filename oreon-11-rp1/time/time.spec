# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fbacf0c81e62429df3e33bda4cee38756604f18e01d977338e23306a3e3b521e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: time
Version: 1.9
Release: 1%{?dist}
Summary: GNU time utility
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/time/
Source0: https://ftp.gnu.org/gnu/time/time-%{version}.tar.gz
Source1: time-1.9.tar.gz.sig
Source2: gpgkey-F576AAAC1B0FF849792D8CB129A794FD2272BC86.gpg
Patch0: time-1.8-Prefer-clock_gettime-CLOCK_MONOTONIC.patch
Patch1: time-1.9-Close-outfp-before-exec.patch
Patch2: time-1.9-drop-flawed-rss-test.patch
Patch3: time-1.9-Fix-compiling-with-GCC15.patch
Patch4: time-1.9-Fix-formatting-a-trailing-backslash-and-a-percent-si.patch
Patch5: time-1.9-Improve-info-directory-index-entry-description.patch
Patch6: time-1.9-Use-kibibytes-instead-of-kilobytes-in-a-documentatio.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: gnupg2
BuildRequires: texinfo

%description
GNU time measures how long a command takes.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/time
%{_infodir}/time.info*
%{_mandir}/man1/time.1*

%changelog
%autochangelog
