%global source0_hash 6000d8e8f0f9040426c4f85d7ad86789bc88d4aeaef585c4d4110adb0b214f21
Name: xmlto
Version: 0.0.29
Release:        1%{?dist}
Summary:        A tool for converting XML files to various formats
License: GPL-2.0-or-later
URL: https://pagure.io/xmlto/
Source0:        https://deb.debian.org/debian/pool/main/x/xmlto/xmlto_%{version}.orig.tar.bz2#/xmlto-%{version}.tar.gz
Requires: docbook-xsl
Requires: libxslt
Requires: docbook-dtds
Requires: util-linux, flex
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  util-linux
# /oreon:deps
%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%package tex
License: GPL-2.0-or-later
Summary: A set of xmlto backends with TeX requirements
Requires: texlive-passivetex
Requires: xmlto = %{version}-%{release}
BuildArch: noarch
%description tex
This subpackage contains xmlto backend scripts which do require
PassiveTeX/TeX for functionality.

%package xhtml
License: GPL-2.0-or-later
Summary: A set of xmlto backends for xhtml1 source format
Requires: xhtml2fo-style-xsl
Requires: xmlto = %{version}-%{release}
BuildArch: noarch
%description xhtml
This subpackage contains xmlto backend scripts for processing
xhtml1 source format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

autoreconf -i -v

%build

%configure BASH=/bin/bash
%make_build
%check

make check
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xmlto-tex -f %{oreon_filedir}/xmlto-tex.list
%files -n xmlto-xhtml -f %{oreon_filedir}/xmlto-xhtml.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.29-5
- Import
