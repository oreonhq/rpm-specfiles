# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 02f159eb88c4254d95e831c51c144b1863b216d909b5ff45743a1ce6f5273090
%global source1_hash 4e4e037a2b83c98c6c94818390d4bdd3f6e10f6ec62dd79188594e26190dc7b4
%global source2_hash 20261d2771b9a052abfa3d8fab1aa62be05791a010281c566f9073bf0e644538
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: docbook-dtds
Version: 1.0
Release: 2%{?dist}
Summary: DocBook document type definitions
License: OASIS
URL: https://www.oasis-open.org/docbook/
Source0: https://www.oasis-open.org/docbook/xml/4.4/docbook-xml-4.4.zip
Source1: https://www.oasis-open.org/docbook/xml/4.5/docbook-xml-4.5.zip
Source2: https://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
Requires(post): sgml-common
Requires(preun): sgml-common

%description
DocBook XML 4.4 and 4.5, and DocBook SGML 3.1 document type definitions.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.4
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.5
python3 -m zipfile -e %{SOURCE0} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.4
python3 -m zipfile -e %{SOURCE1} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.5
mkdir -p %{buildroot}%{_datadir}/sgml/docbook/sgml-dtd-3.1
python3 -m zipfile -e %{SOURCE2} %{buildroot}%{_datadir}/sgml/docbook/sgml-dtd-3.1

%post
%{_bindir}/install-catalog --add %{_sysconfdir}/sgml/sgml-docbook-3.1.cat \
  %{_datadir}/sgml/docbook/sgml-dtd-3.1/docbook.cat >/dev/null 2>&1 || :

%preun
if [ "$1" -eq 0 ]; then
  %{_bindir}/install-catalog --remove %{_sysconfdir}/sgml/sgml-docbook-3.1.cat \
    %{_datadir}/sgml/docbook/sgml-dtd-3.1/docbook.cat >/dev/null 2>&1 || :
fi

%files
%{_datadir}/xml/docbook/
%{_datadir}/sgml/docbook/sgml-dtd-3.1/

%changelog
%autochangelog
