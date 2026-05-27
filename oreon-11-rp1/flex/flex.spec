%global source0_hash e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: A tool for generating scanners (text pattern recognizers)
Name: flex
Version: 2.6.4
Release: 24%{?dist}

# An SPDX license string check done against flex-2.6.4 using fossology
# found strings corresponding to the licenses noted below across the flex
# source tree.
License: BSD-3-Clause-flex AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Bison-exception-2.2 AND GPL-3.0-or-later WITH Texinfo-exception AND FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD AND GPL-2.0-or-later AND X11

URL: https://github.com/westes/flex
Source: https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz

Patch0: flex-rh1389575.patch

Requires: m4
BuildRequires: gettext gettext-devel bison m4 help2man gcc gcc-c++ automake libtool
BuildRequires: make

Obsoletes: flex-doc < 2.6.4-8
Provides: flex-doc = %{version}-%{release}

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
# We renamed flex-static to flex-devel in version 2.5.35-15:
Obsoletes: flex-static < 2.5.35-15
Provides: flex-static = %{version}-%{release}
# We renamed flex-devel to libfl-static in version 2.6.4-6.  This clarifies
# the nature of the package and brings us in line with naming used by SUSE
# and Debian:
Obsoletes: flex-devel < 2.6.4-6
Provides: flex-devel = %{version}-%{release}

%description -n libfl-static

flex is a tool for generating scanners.

This package contains the static library with default implementations of
`main' and `yywrap' functions that binaries using flex can choose to
statically link against instead of implementing their own.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
autoreconf -i
%configure --docdir=%{_pkgdocdir} CFLAGS="-fPIC $RPM_OPT_FLAGS"
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/{README.cvs,TODO,AUTHORS,COPYING,ONEWS}
# Exclude libtool archives (.la) as per Fedora packaging guidelines
find %{buildroot} -name '*.la' -delete

( cd ${RPM_BUILD_ROOT}
  ln -sf flex .%{_bindir}/lex
  ln -sf flex .%{_bindir}/flex++
  ln -s flex.1 .%{_mandir}/man1/lex.1
  ln -s flex.1 .%{_mandir}/man1/flex++.1
  ln -s libfl.a .%{_libdir}/libl.a
)

%find_lang flex

%check
echo ============TESTING===============
make check
echo ============END TESTING===========

%files -f flex.lang
%dir %{_pkgdocdir}
%license COPYING
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_includedir}/FlexLexer.h
%{_infodir}/flex.info*

%files -n libfl%{somajor}
%{_libdir}/libfl.so.%{somajor}*

%files -n libfl-devel
%{_includedir}/FlexLexer.h
%{_libdir}/libfl.so

%files -n libfl-static
%dir %{_pkgdocdir}
%license COPYING
%{_libdir}/*.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.4-24
- Prepare for Oreon 11 (RP1)
