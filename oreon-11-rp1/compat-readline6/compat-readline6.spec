%global source0_hash 56ba6071b9462f980c5a72ab0023893b65ba6debb4eeb475d7a563dc65cafd43
Summary:        A library for editing typed command lines
Name: compat-readline6
Version: 6.3
Release:        1%{?dist}
License: GPLv3+
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source0:        https://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Patch5: readline6.3-upstream-patches1-6.patch
Patch8: readline-6.2-gdb.patch
Patch9: readline-6.2-shlib.patch
Patch10: readline-6.3-config.patch
Patch11: compat-readline6-wcwidth.patch
Patch12: compat-readline6-configure-c99.patch
Requires(post): info
Requires(preun): info
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git
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
Requires: ncurses-devel%{?_isa}
Requires(post): info
Requires(preun): info
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
%global oreon_srcdir readline-%{version}
%oreon_prep
%build

export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%make_build
%install
%make_install
mkdir %{buildroot}%{_libdir}/readline6
mv %{buildroot}%{_libdir}/*.{a,so} %{buildroot}%{_libdir}/readline6/
pushd %{buildroot}%{_libdir}/readline6
  for f in *.so; do
    ln -sf ../$f.6 $f
  done
popd
mv %{buildroot}%{_includedir}/readline{,6}
rm -rf %{buildroot}%{_datadir}/readline
rm -rf %{buildroot}%{_docdir}/readline
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_mandir}
%ldconfig_scriptlets
%oreon_autofiles compat-readline6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles compat-readline6-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n compat-readline6-devel -f %{oreon_filedir}/compat-readline6-devel.list
%files -n compat-readline6-static -f %{oreon_filedir}/compat-readline6-static.list

%changelog

%autochangelog
