%global source0_hash 0bd1d8be8ff0a4ca43f947f95750d34f64eda93c9e2ca79100fd60140b7c6331

Summary: Generates function prototypes and variable declarations from C code
Name: cproto
Version: 4.7y
Release: 1%{?dist}
License: LicenseRef-Fedora-Public-Domain
Source: https://invisible-island.net/archives/cproto/cproto-%{version}.tgz
URL: http://invisible-island.net/
BuildRequires: gcc-c++
BuildRequires: byacc, flex
BuildRequires: make

%description
Cproto generates function prototypes and variable declarations from C
source code. Cproto can also convert function definitions between the
old style and the ANSI C style. This conversion will overwrite the
original files, however, so be sure to make a backup copy of your
original files in case something goes wrong. Cproto uses a Yacc
generated parser, so it should not be confused by complex function
definitions as much as other prototype generators.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%doc AUTHORS CHANGES MANIFEST README
%{_bindir}/cproto
%{_mandir}/man1/cproto.1*

%changelog
%autochangelog
