%global source0_hash e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        A tool for generating scanners (text pattern recognizers)
Name: flex
Version: 2.6.4
Release:        1%{?dist}
License: BSD-3-Clause-flex AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Bison-exception-2.2 AND GPL-3.0-or-later WITH Texinfo-exception AND FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD AND GPL-2.0-or-later AND X11
URL: https://github.com/westes/flex
Source0:        https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz
Patch0: flex-rh1389575.patch
Requires: m4
Obsoletes: flex-doc < 2.6.4-8
Provides: flex-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
# /oreon:deps
%description
The flex program generates scanners.  Scanners are programs which can
recognize lexical patterns in text.  Flex takes pairs of regular
expressions and C code as input and generates a C source file as
output.  The output file is compiled and linked with a library to
produce an executable.  The executable searches through its input for
occurrences of the regular expressions.  When a match is found, it
executes the corresponding C code.  Flex was designed to work with
both Yacc and Bison, and is used by many programs as part of their
build process.

You should install flex if you are going to use your system for
application development.

# We keep the libraries in separate sub-package to allow for multilib
# installations of flex.

%define somajor 2

%package -n libfl%{somajor}
Summary: Libraries for the flex scanner generator
%description -n libfl%{somajor}
flex is a tool for generating scanners.

This package contains the shared library with default implementations of
`main' and `yywrap' functions that binaries using flex can choose to link
against instead of implementing on their own.

%package -n libfl-devel
Summary: Development files for the flex scanner generator
Requires: libfl%{somajor} = %{version}-%{release}
%description -n libfl-devel
flex is a tool for generating scanners.

This package contains files required to build programs that use flex
libraries.

%package -n libfl-static
Summary: Static libraries for the flex scanner generator
Obsoletes: flex-static < 2.5.35-15
Provides: flex-static = %{version}-%{release}
Obsoletes: flex-devel < 2.6.4-6
Provides: flex-devel = %{version}-%{release}
%description -n libfl-static

flex is a tool for generating scanners.

This package contains the static library with default implementations of
`main' and `yywrap' functions that binaries using flex can choose to
statically link against instead of implementing their own.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure --docdir=%{_pkgdocdir} CFLAGS="-fPIC $RPM_OPT_FLAGS"
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/{README.cvs,TODO,AUTHORS,COPYING,ONEWS}
find %{buildroot} -name '*.la' -delete
( cd ${RPM_BUILD_ROOT}
  ln -sf flex .%{_bindir}/lex
  ln -sf flex .%{_bindir}/flex++
  ln -s flex.1 .%{_mandir}/man1/lex.1
  ln -s flex.1 .%{_mandir}/man1/flex++.1
  ln -s libfl.a .%{_libdir}/libl.a
)
%find_lang flex
%oreon_autofiles libfl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libfl-static usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

echo ============TESTING===============
make check
echo ============END TESTING===========
%files -f %{oreon_filedir}/main.list
%files -n libfl2 -f %{oreon_filedir}/libfl2.list
%files -n libfl-devel -f %{oreon_filedir}/libfl-devel.list
%files -n libfl-static -f %{oreon_filedir}/libfl-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.4-24
- Prepare for Oreon 11 (RP1)
