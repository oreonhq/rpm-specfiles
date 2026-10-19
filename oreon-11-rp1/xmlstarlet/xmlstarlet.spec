%global source0_hash 15d838c4f3375332fd95554619179b69e4ec91418a3a5296e7c631b7ed19e7ca
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name: xmlstarlet
Version: 1.6.1
Release:        1%{?dist}
Summary:        Command Line XML Toolkit
License: MIT
URL: http://xmlstar.sourceforge.net/
Source0:        https://downloads.sourceforge.net/xmlstar/%{name}-%{version}.tar.gz
Patch0: xmlstarlet-1.6.1-nogit.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  xmlto
# /oreon:deps
%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure --disable-static-libs --with-libxml-include-prefix=%{_includedir}/libxml2 --docdir=%{_pkgdocdir} # --libdir=%{_libdir}
%make_build
%install
%make_install
mv %{buildroot}%{_bindir}/xml %{buildroot}%{_bindir}/xmlstarlet
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.1-29
- Prepare for Oreon 11 (RP1)
