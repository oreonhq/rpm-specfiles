%global source0_hash e91cc201c79456b923b45cfa779da62f5ca91824d11c545167ee7bb33a9fb810
Name: cdecl
Summary:        Translator for C gibberish
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LicenseRef-Fedora-PublicDomain
Version: 18.7.2
Release:        1%{?dist}
URL: https://github.com/paul-j-lucas/cdecl/
Source0:        https://github.com/paul-j-lucas/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0: cterm-no-such-dev.patch
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  readline-devel
# /oreon:deps
%description
Cdecl is a program which will turn English-like phrases such as "declare
foo as array 5 of pointer to function returning int" into C declarations
such as "int (*foo[5])()". It can also do the opposite, translating C
into the pseudo-English. And it handles typecasts, too. Plus C++.
This version also has command line editing and history.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make -C test/ check || { cat test/test-suite.log; exit 1; }
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
