# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 684ea53c1f5b71d6d1ac6086bbc96906b1f709ecc7ab536615b0f0c9e1baa3cc

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           asciidoc
Version:        10.2.0
Release:        1%{?dist}
Summary:        Text based document generation
License:        GPL-2.0-or-later
URL:            https://asciidoc-py.github.io/
Source0:        https://github.com/asciidoc-py/asciidoc-py/archive/%{version}/%{name}-py-%{version}.tar.gz
Patch0:         asciidoc-table-separator.patch

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt

Requires:       python3
Requires:       docbook-style-xsl
Requires:       libxslt
Recommends:     graphviz
Recommends:     source-highlight

%description
AsciiDoc is a text document format for writing short documents,
articles, books and UNIX man pages. AsciiDoc files can be translated
to HTML and DocBook markups using the asciidoc(1) command.

%package doc
Summary:        Additional documentation and examples for asciidoc
Requires:       %{name} = %{version}-%{release}

%description doc
Additional documentation and examples for asciidoc.

%package latex
Summary:        Support for asciidoc latex output
Requires:       %{name} = %{version}-%{release}
Requires:       dblatex
Requires:       texlive-dvipng-bin

%description latex
Support for asciidoc latex output.

%prep
%oreon_sha256
%autosetup -n %{name}-py-%{version} -p1

%build
autoreconf -v
%configure
%make_build

%install
make install docs manpages DESTDIR=%{buildroot} PIP_NO_BUILD_ISOLATION=0
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}/share/doc/doc/{asciidoc.1,a2x.1,testasciidoc.1} %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_pkgdocdir}/doc
mv %{buildroot}/share/doc/doc/ %{buildroot}%{_pkgdocdir}/doc
mkdir -p %{buildroot}%{_pkgdocdir}/doc/images
mv %{buildroot}/share/doc/images/ %{buildroot}%{_pkgdocdir}/doc/images
rm %{buildroot}/share/doc/{BUGS.adoc,CHANGELOG.adoc,INSTALL.adoc,README.md,dblatex/dblatex-readme.txt,docbook-xsl/asciidoc-docbook-xsl.txt}

%check
%{__python3} -m pytest -q tests

%files
%license COPYRIGHT
%doc BUGS.adoc CHANGELOG.adoc README.md
%{_mandir}/man1/*.1*
%{_bindir}/a2x
%{_bindir}/asciidoc
%{python3_sitelib}/asciidoc-%{version}.dist-info/
%{python3_sitelib}/asciidoc/
%exclude %{python3_sitelib}/asciidoc/resources/filters/latex
%exclude %{python3_sitelib}/asciidoc/resources/filters/music
%exclude %{_pkgdocdir}/doc

%files doc
%license COPYRIGHT
%{_pkgdocdir}/doc/

%files latex
%license COPYRIGHT
%dir %{python3_sitelib}/asciidoc/resources/filters/latex

%changelog
%autochangelog
