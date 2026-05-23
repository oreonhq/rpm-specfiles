%define byaccdate 20241231

Summary: Berkeley Yacc, a parser generator
Name: byacc
Version: 2.0.%{byaccdate}
Release: 3%{?dist}

# An SPDX license string check done against byacc-20230521 using fossology
# found strings corresponding to the licenses noted below across the byacc
# source tree.  byacc is in the public domain, and the "public domain
# declaration" was documented in fedora-license-data as per Fedora policy
# via the following commit:
# https://gitlab.com/fedora/legal/fedora-license-data/-/commit/04ec53689413bb
License: LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND X11 AND X11-distribute-modifications-variant AND FSFUL

URL: https://invisible-island.net/byacc/byacc.html
Source: https://invisible-island.net/archives/byacc/byacc-%{byaccdate}.tgz

BuildRequires:  gcc
BuildRequires: make

%description
This package provides a parser generator utility that reads a grammar
specification from a file and generates an LR(1) parser for it.  The
parsers consist of a set of LALR(1) parsing tables and a driver
routine written in the C programming language.  It has a public domain
license which includes the generated C.

If you are going to do development on your system, you will want to install
this package.

%prep
%setup -q -n byacc-%{byaccdate}

# Revert default stack size back to 10000
# https://bugzilla.redhat.com/show_bug.cgi?id=743343
find . -type f -name \*.c -print0 |
  xargs -0 sed -i 's/YYSTACKSIZE 500/YYSTACKSIZE 10000/g'

%build
%configure --disable-dependency-tracking
%make_build

%install
%make_install
ln -s yacc %{buildroot}%{_bindir}/byacc
ln -s yacc.1 %{buildroot}%{_mandir}/man1/byacc.1

%check
echo ====================TESTING=========================
make check
echo ====================TESTING END=====================

%files
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%{_bindir}/yacc
%{_bindir}/byacc
%{_mandir}/man1/yacc.1*
%{_mandir}/man1/byacc.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.%{byaccdate}-3
- Prepare for Oreon 11 (RP1)
