%global source0_hash fe5383204467828cd495ee8d1d3c037a7eba1389c22bc6a041f627976f9061cc
Summary:        A library for editing typed command lines
Name: readline
Version: 8.3
Release:        1%{?dist}
License: GPL-3.0-or-later AND GPL-2.0-or-later AND GFDL-1.3-no-invariants-or-later
URL: https://tiswww.case.edu/php/chet/readline/rltop.html
Source0:        https://mirrors.kernel.org/gnu/readline/readline-%{version}.tar.gz
Patch1: readline-8.3-patch-1.patch
Patch2: readline-8.3-patch-2.patch
Patch3: readline-8.3-patch-3.patch
Patch101: readline-8.0-shlib.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package static
Summary: Static libraries for the readline library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
The readline-static package contains the static version of the readline
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --with-curses --disable-install-examples
%make_build
%install
%make_install
rm -vrf %{buildroot}%{_docdir}/readline
rm -vf %{buildroot}%{_infodir}/dir*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n readline-devel -f %{oreon_filedir}/readline-devel.list
%files -n readline-static -f %{oreon_filedir}/readline-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.3-4
- Prepare for Oreon 11 (RP1)
