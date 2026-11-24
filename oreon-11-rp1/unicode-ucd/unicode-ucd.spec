# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b3e555514060b92290d154f53655c5eb0fa62b16eb04c03434ff72d1a66a0d8
%global source1_hash 4c93ea9c1f636451729a840978f1667a53886af37ba854fdcce109721c63d43e
%global source2_hash e7a93b009565cfce55919a381437ac4db883e9da2126fa28b91d12732bc53d96
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global unicodedir %{_datadir}/unicode
%global ucddir %{unicodedir}/ucd

Name:           unicode-ucd
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode Character Database

License:        Unicode-3.0
URL:            http://www.unicode.org/ucd/
Source0:        https://www.unicode.org/Public/%{version}/ucd/UCD.zip
Source1:        https://www.unicode.org/Public/%{version}/ucd/Unihan.zip
Source2:        https://www.unicode.org/license.txt
Source3:        test.py
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.

%package unihan
Summary:        Unicode Han Database
Requires:       %{name} = %{version}-%{release}

%description unihan
This package contains Unihan.zip which contains the data files for the Unified
Han database of Hanzi/Kanji/Hanja Chinese characters.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%setup -q -c

grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)

%build
%{nil}

%install
mkdir -p %{buildroot}%{ucddir}
cp -ar . %{buildroot}%{ucddir}
cp -p %{SOURCE1} %{buildroot}%{ucddir}
cp %{SOURCE2} .

%check
%{SOURCE3} %{buildroot}%{ucddir}/UnicodeData.txt

%files
%license license.txt
%dir %{unicodedir}
%{ucddir}
%exclude %{ucddir}/Unihan.zip

%files unihan
%{ucddir}/Unihan.zip

%changelog
%autochangelog
