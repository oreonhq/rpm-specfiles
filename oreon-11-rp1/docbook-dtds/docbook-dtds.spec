# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 02f159eb88c4254d95e831c51c144b1863b216d909b5ff45743a1ce6f5273090
%global source1_hash 4e4e037a2b83c98c6c94818390d4bdd3f6e10f6ec62dd79188594e26190dc7b4
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: docbook-dtds
Version: 1.0
Release: 1%{?dist}
Summary: DocBook XML DTDs
License: OASIS
URL: https://www.oasis-open.org/docbook/
Source0: https://www.oasis-open.org/docbook/xml/4.4/docbook-xml-4.4.zip
Source1: https://www.oasis-open.org/docbook/xml/4.5/docbook-xml-4.5.zip
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3

%description
DocBook XML 4.4 and 4.5 document type definitions.

%prep
%oreon_sha256
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.4
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.5
python3 -m zipfile -e %{SOURCE0} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.4
python3 -m zipfile -e %{SOURCE1} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.5

%files
%{_datadir}/xml/docbook/
