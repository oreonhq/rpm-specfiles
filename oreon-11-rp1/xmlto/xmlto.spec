%bcond_with xmlto_tex 0

Name: xmlto
Version: 0.0.29
Release: 5%{?dist}
Summary: A tool for converting XML files to various formats

License: GPL-2.0-or-later
URL: https://pagure.io/xmlto/
Source0: https://pagure.io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: docbook-xsl
BuildRequires: libxslt
BuildRequires: util-linux, flex
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake

# We rely heavily on the DocBook XSL stylesheets!
Requires: docbook-xsl
Requires: libxslt
Requires: docbook-dtds
Requires: util-linux, flex

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%if %{with xmlto_tex}
%package tex
License: GPL-2.0-or-later
Summary: A set of xmlto backends with TeX requirements
# For full functionality, we need passivetex.
Requires: texlive-passivetex
# We require main package
Requires: xmlto = %{version}-%{release}
BuildArch: noarch

%description tex
This subpackage contains xmlto backend scripts which do require
PassiveTeX/TeX for functionality.
%endif

%package xhtml
License: GPL-2.0-or-later
Summary: A set of xmlto backends for xhtml1 source format
# For functionality we need stylesheets xhtml2fo-style-xsl
Requires: xhtml2fo-style-xsl
# We require main package
Requires: xmlto = %{version}-%{release}
BuildArch: noarch

%description xhtml
This subpackage contains xmlto backend scripts for processing
xhtml1 source format.

%prep
%autosetup -n %{name}-%{version} -p1

autoreconf -i -v

%build
%configure BASH=/bin/bash
%make_build

%check
make check

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md AUTHORS.md NEWS.md
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto
%exclude %{_datadir}/xmlto/format/fo/dvi
%exclude %{_datadir}/xmlto/format/fo/ps
%exclude %{_datadir}/xmlto/format/fo/pdf
%exclude %dir %{_datadir}/xmlto/format/xhtml1/
%exclude %{_datadir}/xmlto/format/xhtml1

%if %{with xmlto_tex}
%files tex
%{_datadir}/xmlto/format/fo/dvi
%{_datadir}/xmlto/format/fo/ps
%{_datadir}/xmlto/format/fo/pdf
%endif

%files xhtml
%dir %{_datadir}/xmlto/format/xhtml1/
%{_datadir}/xmlto/format/xhtml1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.29-5
- Prepare for Oreon 11 (RP1)
