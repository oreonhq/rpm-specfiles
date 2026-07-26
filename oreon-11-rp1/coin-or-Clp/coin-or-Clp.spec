%global source0_hash 0d79ece896cdaa4a3855c37f1c28e6c26285f74d45f635046ca0b6d68a509885

%global		module		Clp

# On a bootstrap build, without coin-or-Cbc in the buildroot, a number of
# parameters are not defined.  This leads to invalid vector accesses later
# when we build packages that depend on coin-or-Cbc (such as coin-or-CoinMP).
# We first build coin-or-Clp in bootstrap mode, then build coin-or-Cgl,
# followed by coin-or-Cbc.  At that point we can rebuild this package in
# non-bootstrap mode to get the Cbc parameter definitions.
#
# Attempting to cheat by defining COIN_HAS_CBC while building this package
# just leads to other compiler errors due to missing coin-or-Cbc headers.
# As painful as it is, this really is the best approach.
%bcond bootstrap 0

Name:		coin-or-%{module}
Summary:	Coin-or linear programming
Version:	1.17.10
Release:	11%{?dist}

# The project as a whole is licensed EPL-2.0.  However, many source files still
# claim to be licensed EPL-1.0.  This is probably an upstream oversight.
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	asl-devel
BuildRequires:	coin-or-Data-Netlib
BuildRequires:	coin-or-Osi-doc
BuildRequires:	gcc-c++
BuildRequires:	doxygen
BuildRequires:	make
BuildRequires:	MUMPS-devel
%if %{without bootstrap}
BuildRequires:	pkgconfig(cbc)
%endif
BuildRequires:	pkgconfig(osi)
BuildRequires:	pkgconfig(readline)
BuildRequires:	suitesparse-devel

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix a bad static cast
Patch1:		%{name}-bad-cast.patch

# Fix a parameter which is not defined when building with Cbc support.
Patch2:		%{name}-param.patch

# Catch polymorphic errors by reference rathern than by value
Patch3:		%{name}-catch.patch

# Increase buffer sizes to avoid sprintf overflow
Patch4:		%{name}-overflow.patch

# Fix mixed signed-unsigned comparisons
Patch5:		%{name}-signed.patch

# Do not use the AVX2 instructions
Patch6:		%{name}-no-avx.patch

Patch7: coin-or-Clp-configure-c99.patch
Patch8: coin-or-Clp-configure-amd_defaults-c99.patch

%description
Clp (Coin-or linear programming) is an open-source linear programming
solver written in C++. It is primarily meant to be used as a callable
library, but a basic, stand-alone executable version is also available.

%package	devel
Summary:	Development files for %{name}
%if %{without bootstrap}
Requires:	coin-or-Cbc-devel%{?_isa}
%endif
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	readline-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Osi-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @CLPLIB_PCLIBS@/\nLibs.private:&/' Clp/clp.pc.in

%build
# Make sure Cbc parameters are initialized too
export CPPFLAGS='-DNDEBUG -DCOIN_HAS_NTY'
%if %{without bootstrap}
export CPPFLAGS="$CPPFLAGS -DCOIN_HAS_CBC -DCBC_THREAD -I$PWD/src/OsiClp"
%endif
%configure \
  --with-amd-incdir=%{_includedir}/suitesparse \
  --with-amd-lib=-lamd \
  --with-asl-incdir=%{_includedir}/asl \
  --with-asl-lib=-lasl \
  --with-cholmod-incdir=%{_includedir}/suitesparse \
  --with-cholmod-lib=-lcholmod \
  --with-glpk_incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
  --with-mumps-incdir=%{_includedir}/MUMPS \
  --with-mumps-lib="-ldmumps -lmpiseq" \
%if %{without bootstrap}
  LIBS="-lCbc"
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,clp_addlibs.txt}
cp -a README.md doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README.md
%{_bindir}/clp
%{_libdir}/libClp.so.1
%{_libdir}/libClp.so.1.*
%{_libdir}/libClpSolver.so.1
%{_libdir}/libClpSolver.so.1.*
%{_libdir}/libOsiClp.so.1
%{_libdir}/libOsiClp.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libClp.so
%{_libdir}/libClpSolver.so
%{_libdir}/libOsiClp.so
%{_libdir}/pkgconfig/clp.pc
%{_libdir}/pkgconfig/osi-clp.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/clp_doxy.tag

%changelog
%autochangelog
