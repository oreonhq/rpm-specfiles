# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 669ee27120ae71589f638fe3a167d6ea54f8633f5ab1b282551bd7a7c9510dfa
%global source1_hash 446a8bd3d417a6c1d332a261abe9c7ae41501dfbd8a7e800e388032868c7f876
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Text file format converters
Name: dos2unix
Version: 7.5.7
Release: 1%{?dist}
License: BSD-3-Clause
URL: https://waterlander.net/dos2unix/
Source: https://waterlander.net/dos2unix/files/%{name}-%{version}.tar.gz
Source: https://waterlander.net/dos2unix/files/%{name}-%{version}.tar.gz.asc
Source: 38C1F572B12725BE.asc

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gettext
BuildRequires: make
BuildRequires: perl-Test-Harness
BuildRequires: perl-Test-Simple
BuildRequires: gnupg2

Provides: unix2dos = %{version}-%{release}
Obsoletes: unix2dos < 5.1-1

%description
Convert text files with DOS or Mac line endings to Unix line endings and
vice versa.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%make_build LDFLAGS="%{build_ldflags}" prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

rm -rf %{buildroot}%{_docdir}

%find_lang %{name} --with-man --all-name

%check
make test

%files -f %{name}.lang
%license COPYING.txt
%doc man/man1/dos2unix.htm ChangeLog.txt
%doc NEWS.txt README.txt TODO.txt
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2dos
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*

%changelog
%autochangelog
