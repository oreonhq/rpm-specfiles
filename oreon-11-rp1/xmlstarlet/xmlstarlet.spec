# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 15d838c4f3375332fd95554619179b69e4ec91418a3a5296e7c631b7ed19e7ca
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: xmlstarlet
Version: 1.6.1
Release: 29%{?dist}
Summary: Command Line XML Toolkit
License: MIT
URL: http://xmlstar.sourceforge.net/
Source0: http://downloads.sourceforge.net/xmlstar/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/xmlstar/bugs/109/
Patch0: xmlstarlet-1.6.1-nogit.patch
# http://sourceforge.net/tracker/?func=detail&aid=3266898&group_id=66612&atid=515106

BuildRequires: make
BuildRequires: gcc
BuildRequires: xmlto automake autoconf libxslt-devel
BuildRequires: libxml2-devel >= 2.6.23


%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
%oreon_verify_sources
%autosetup -p1


%build
autoreconf -i
%configure --disable-static-libs --with-libxml-include-prefix=%{_includedir}/libxml2 --docdir=%{_pkgdocdir} # --libdir=%{_libdir}
%make_build


%install
%make_install
# Avoid name kludging in autotools
mv %{buildroot}%{_bindir}/xml %{buildroot}%{_bindir}/xmlstarlet


%check
make check



%files
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc %{_pkgdocdir}/*
%{_mandir}/man1/xmlstarlet.1*
%{_bindir}/xmlstarlet


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.1-29
- Prepare for Oreon 11 (RP1)
