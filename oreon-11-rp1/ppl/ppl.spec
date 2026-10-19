%global source0_hash 2d470b0c262904f190a19eac57fb5c2387b1bfc3510de25a08f3c958df62fdf1
Name:			ppl
Version:		1.2
Release:        39%{?dist}
Summary:        The Parma Polyhedra Library: a library of numerical abstractions
License:		GPL-3.0-or-later
URL:			http://www.bugseng.com/ppl
Source0:        http://www.bugseng.com/products/ppl/download/ftp/releases/%{version}/%{name}-%{version}.tar.bz2
Source1:		ppl.hh
Source2:		ppl_c.h
Patch0:			configure.patch
Patch1:			%{name}-pl82.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
BuildRequires:  sharutils
BuildRequires:  swi-prolog-core
# /oreon:deps
%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%package devel
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Requires:	%{name}%{?_isa} = %{version}-%{release}, gmp-devel%{?_isa}
%description devel
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%package static
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description static
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%package utils
Summary:	Utilities using the Parma Polyhedra Library
Requires:	%{name}%{?_isa} = %{version}-%{release}
BuildRequires:	glpk-devel >= 4.13
%description utils
This package contains the mixed integer linear programming solver ppl_lpsol.
the program ppl_lcdd for vertex/facet enumeration of convex polyhedra,
and the parametric integer programming solver ppl_pips.

# This is the explicit list of arches gprolog supports
%ifarch x86_64 %{ix86} ppc alpha aarch64
%package gprolog
Summary:	The GNU Prolog interface of the Parma Polyhedra Library
BuildRequires:	gprolog >= 1.3.2
Requires:	%{name}%{?_isa} = %{version}-%{release}, gprolog%{?_isa} >= 1.3.2
%description gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library (PPL).
Install this package if you want to use the library in GNU Prolog programs.
%endif

# This is the explicit list of arches gprolog supports
%ifarch x86_64 %{ix86} ppc alpha aarch64
%package gprolog-static
Summary:	The static archive for the GNU Prolog interface of the Parma Polyhedra Library
Requires:	%{name}-gprolog%{?_isa} = %{version}-%{release}
%description gprolog-static
This package contains the static archive for the GNU Prolog interface
of the Parma Polyhedra Library.
%endif

%package swiprolog
Summary:	The SWI-Prolog interface of the Parma Polyhedra Library
BuildRequires:	swi-prolog-core >= 5.10.2-3
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	swi-prolog-core%{?_isa} >= 5.10.2-3
%description swiprolog
This package adds SWI-Prolog support to the Parma Polyhedra Library.
Install this package if you want to use the library in SWI-Prolog programs.

%ifarch %{java_arches}
%package java
Summary:	The Java interface of the Parma Polyhedra Library
BuildRequires:	java-25-devel
BuildRequires:	javapackages-tools
Requires:	java-25-headless
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description java
This package adds Java support to the Parma Polyhedra Library.
Install this package if you want to use the library in Java programs.

%package java-javadoc
Summary:	Javadocs for %{name}-java
Requires:	%{name}-java%{?_isa} = %{version}-%{release}
%description java-javadoc
This package contains the API documentation for Java interface
of the Parma Polyhedra Library.
%endif

%package docs
License:	GFDL-1.2-no-invariants-or-later
Summary:	Documentation for the Parma Polyhedra Library
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL).
Install this package if you want to program with the PPL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Fix detection of C++11 features
sed -i 's,== 201103L,>= 201103L,g' m4/ac_check_cxx11.m4

# Regenerate configure
autoreconf -fiv

%build

CPPFLAGS="-I`swipl --dump-runtime-variables | grep PLBASE= | sed 's/PLBASE="\(.*\)";/\1/'`/include"
%ifarch x86_64 %{ix86} ppc alpha aarch64
CPPFLAGS="$CPPFLAGS -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
%ifarch %{java_arches}
if [ ! -e %{_bindir}/javah ]; then
  export JAVAH="%{_bindir}/javac"
  sed -e 's/\$(JAVAC)/& -h . -source 1.8 -target 1.8/' \
      -e '/^java_cxx_headers\.stamp$/d' \
      -i interfaces/Java/parma_polyhedra_library/Makefile.in
fi
CPPFLAGS="$CPPFLAGS -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux -DNDEBUG"
%endif
%configure --docdir=%{_datadir}/doc/%{name} --enable-shared --disable-rpath \
%ifarch %{java_arches}
  --enable-interfaces="cxx c gnu_prolog swi_prolog java" \
%else
  --enable-interfaces="cxx c gnu_prolog swi_prolog" \
%endif
  CPPFLAGS="$CPPFLAGS"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install INSTALL="%{__install} -p"
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/%{name}/*.la
rm -f %{buildroot}%{_libdir}/%{name}/libppl_swiprolog.a
normalized_arch=%{_arch}
%ifarch %{ix86}
normalized_arch=i386
%endif
%ifarch %{arm}
normalized_arch=arm
%endif
%ifarch sh3 sh4
normalized_arch=sh
%endif
mv %{buildroot}/%{_includedir}/ppl.hh %{buildroot}/%{_includedir}/ppl-${normalized_arch}.hh
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/ppl.hh
mv %{buildroot}/%{_includedir}/ppl_c.h %{buildroot}/%{_includedir}/ppl_c-${normalized_arch}.h
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/ppl_c.h
%ifarch %{java_arches}
mkdir -p %{buildroot}%{_javadocdir}
mv \
%{buildroot}/%{_datadir}/doc/%{name}/ppl-user-java-interface-%{version}-html \
%{buildroot}%{_javadocdir}/%{name}-java
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n ppl-devel -f %{oreon_filedir}/ppl-devel.list
%files -n ppl-static -f %{oreon_filedir}/ppl-static.list
%files -n ppl-utils -f %{oreon_filedir}/ppl-utils.list
%files -n ppl-swiprolog -f %{oreon_filedir}/ppl-swiprolog.list
%files -n ppl-docs -f %{oreon_filedir}/ppl-docs.list

%changelog

%autochangelog
