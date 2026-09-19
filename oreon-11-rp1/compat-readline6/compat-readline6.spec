%global source0_hash 56ba6071b9462f980c5a72ab0023893b65ba6debb4eeb475d7a563dc65cafd43

Summary: A library for editing typed command lines
Name: compat-readline6
Version: 6.3
Release: 30%{?dist}
License: GPLv3+
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz

Patch5: readline6.3-upstream-patches1-6.patch
# add workaround for problem in gdb
# in new version of readline needs to be deleted
# bz701131
Patch8: readline-6.2-gdb.patch
# fix file permissions, remove RPATH, use CFLAGS
Patch9: readline-6.2-shlib.patch
Patch10: readline-6.3-config.patch
Patch11: compat-readline6-wcwidth.patch
Patch12: compat-readline6-configure-c99.patch

Requires(post): info
Requires(preun): info
BuildRequires:  gcc
BuildRequires: ncurses-devel
BuildRequires: git
BuildRequires: make

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

%autosetup -n readline-%{version} -p1

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%make_build

%install
%make_install

# Move stuff under private dirs to not conflict with original subpackage
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

%files
%license COPYING
%doc CHANGES NEWS README USAGE
%{_libdir}/libreadline.so.6*
%{_libdir}/libhistory.so.6*

%files devel
%{_includedir}/readline6/
%{_libdir}/readline6/libreadline.so
%{_libdir}/readline6/libhistory.so

%files static
%{_libdir}/readline6/libreadline.a
%{_libdir}/readline6/libhistory.a

%changelog
%autochangelog
