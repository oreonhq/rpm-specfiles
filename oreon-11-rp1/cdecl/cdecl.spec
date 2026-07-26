%global source0_hash e91cc201c79456b923b45cfa779da62f5ca91824d11c545167ee7bb33a9fb810

Name: cdecl
Summary: Translator for C gibberish

# The original cdecl has been released in May 1988, into the public domain.
# The fork used in this package re-licenses the code under GPLv3.
# It also includes some code taken from Gnulib, licensed under the LGPL.
#
# Check the discussion on the legal mailing list regarding suitability for Fedora:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/QBYRCIMQDXAD2ZKUWKKYSTDB6T6GW2SO/
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LicenseRef-Fedora-PublicDomain

Version: 18.7.2
Release: 1%{?dist}

URL: https://github.com/paul-j-lucas/cdecl/
Source0: %{URL}releases/download/cdecl-%{version}/cdecl-%{version}.tar.gz

# cdecl tries a couple of different methods of getting terminal information.
# One of them involves getting the terminal path via ctermid(3) and then
# opening the file. This works in a regular user session and seems to
# work in upstream's CI environment. However, in mock & koji, the file
# is not accessible, causing some tests to fail.
Patch0: cterm-no-such-dev.patch

BuildRequires: diffutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses
BuildRequires: readline-devel

%description
Cdecl is a program which will turn English-like phrases such as "declare
foo as array 5 of pointer to function returning int" into C declarations
such as "int (*foo[5])()". It can also do the opposite, translating C
into the pseudo-English. And it handles typecasts, too. Plus C++.
This version also has command line editing and history.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
make -C test/ check || { cat test/test-suite.log; exit 1; }

%files
%doc AUTHORS README.md README-2.5.txt
%license COPYING
%{_bindir}/cdecl
%{_bindir}/c++decl
%{_mandir}/man1/cdecl.1*
%{_mandir}/man1/c++decl.1*

%{_datadir}/bash-completions/
# bash-completions/completions/_cdecl
%{_datadir}/zsh/
# zsh/site-functions/_cdecl

%changelog
%autochangelog
