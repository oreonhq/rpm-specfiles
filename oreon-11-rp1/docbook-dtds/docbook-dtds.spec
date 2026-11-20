# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 02f159eb88c4254d95e831c51c144b1863b216d909b5ff45743a1ce6f5273090
%global source1_hash 4e4e037a2b83c98c6c94818390d4bdd3f6e10f6ec62dd79188594e26190dc7b4
%global source2_hash 20261d2771b9a052abfa3d8fab1aa62be05791a010281c566f9073bf0e644538
%global source3_hash 30f0644064e0ea71751438251940b1431f46acada814a062870f486c772e7772
%global source4_hash acc4601e4f97a196076b7e64b368d9248b07c7abf26b34a02cca40eeebe60fa2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: docbook-dtds
Version: 1.0
Release: 6%{?dist}
Summary: DocBook document type definitions
License: OASIS
URL: https://www.oasis-open.org/docbook/
Source0: https://www.oasis-open.org/docbook/xml/4.4/docbook-xml-4.4.zip
Source1: https://www.oasis-open.org/docbook/xml/4.5/docbook-xml-4.5.zip
Source2: https://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
Source3: https://www.oasis-open.org/docbook/xml/4.1.2/docbkx412.zip
Source4: https://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: libxml2
Requires: xml-common
Requires(post): sgml-common
Requires(post): xml-common
Requires(post): libxml2
Requires(postun): libxml2
Requires(preun): sgml-common

%description
DocBook XML 4.1.2, 4.2, 4.4 and 4.5, and DocBook SGML 3.1 document type definitions.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.1.2
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.2
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.4
mkdir -p %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.5
python3 -m zipfile -e %{SOURCE3} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.1.2
python3 -m zipfile -e %{SOURCE4} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.2
python3 -m zipfile -e %{SOURCE0} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.4
python3 -m zipfile -e %{SOURCE1} %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.5
mkdir -p %{buildroot}%{_datadir}/sgml/docbook/sgml-dtd-3.1
python3 -m zipfile -e %{SOURCE2} %{buildroot}%{_datadir}/sgml/docbook/sgml-dtd-3.1

mkdir -p %{buildroot}%{_sysconfdir}/sgml/docbook
CAT=%{buildroot}%{_sysconfdir}/sgml/docbook/docbook-dtds.xml
%{_bindir}/xmlcatalog --noout --create "$CAT"
for ver in 4.1.2 4.2 4.4 4.5; do
  %{_bindir}/xmlcatalog --noout --add public \
    "-//OASIS//DTD DocBook XML V${ver}//EN" \
    "file://%{_datadir}/xml/docbook/xml-dtd-${ver}/docbookx.dtd" "$CAT"
  %{_bindir}/xmlcatalog --noout --add system \
    "http://www.oasis-open.org/docbook/xml/${ver}/docbookx.dtd" \
    "file://%{_datadir}/xml/docbook/xml-dtd-${ver}/docbookx.dtd" "$CAT"
done

%check
xmlcatalog %{buildroot}%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
  http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd | grep -q docbookx.dtd
xmlcatalog %{buildroot}%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
  http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd | grep -q docbookx.dtd
test -f %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.1.2/docbookx.dtd
test -f %{buildroot}%{_datadir}/xml/docbook/xml-dtd-4.2/docbookx.dtd

%post
%{_bindir}/install-catalog --add %{_sysconfdir}/sgml/sgml-docbook-3.1.cat \
  %{_datadir}/sgml/docbook/sgml-dtd-3.1/docbook.cat >/dev/null 2>&1 || :
%{_bindir}/xmlcatalog --noout --del \
  file://%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
  %{_sysconfdir}/sgml/docbook/xmlcatalog >/dev/null 2>&1 || :
%{_bindir}/xmlcatalog --noout --add nextCatalog "" \
  file://%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
  %{_sysconfdir}/sgml/docbook/xmlcatalog
%{_bindir}/xmlcatalog --noout --del \
  file://%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
  %{_sysconfdir}/xml/catalog >/dev/null 2>&1 || :
%{_bindir}/xmlcatalog --noout --add nextCatalog "" \
  file://%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
  %{_sysconfdir}/xml/catalog

%preun
if [ "$1" -eq 0 ]; then
  %{_bindir}/install-catalog --remove %{_sysconfdir}/sgml/sgml-docbook-3.1.cat \
    %{_datadir}/sgml/docbook/sgml-dtd-3.1/docbook.cat >/dev/null 2>&1 || :
fi

%postun
if [ "$1" -eq 0 ]; then
  %{_bindir}/xmlcatalog --noout --del \
    file://%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
    %{_sysconfdir}/sgml/docbook/xmlcatalog || :
  %{_bindir}/xmlcatalog --noout --del \
    file://%{_sysconfdir}/sgml/docbook/docbook-dtds.xml \
    %{_sysconfdir}/xml/catalog || :
fi

%files
%{_sysconfdir}/sgml/docbook/docbook-dtds.xml
%{_datadir}/xml/docbook/
%{_datadir}/sgml/docbook/sgml-dtd-3.1/

%changelog
%autochangelog
