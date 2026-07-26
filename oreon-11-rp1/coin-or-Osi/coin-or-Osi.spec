%global source0_hash 1063b6a057e80222e2ede3ef0c73c0c54697e0fee1d913e2bef530310c13a670

%global		module		Osi

Name:		coin-or-%{module}
Summary:	COIN-OR Open Solver Interface Library
Version:	0.108.11
Release:	7%{?dist}

# The project as a whole is licensed EPL-2.0.  However, many source files still
# claim to be licensed EPL-1.0.  This is probably an upstream oversight.
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz
# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch
# Fix build with glpk > 4.48
Patch1:		%{name}-glpk.patch
# Fix non-C99 constructs in the configure script
Patch2:		%{name}-configure-c99.patch
# Fix build with SoPlex >= 1.7
Patch3:		%{name}-soplex.patch
# Upstream fix for objective offset being ignored when reading a .lp file
# https://github.com/coin-or/Osi/commit/4071468cf9629d39660e49e4a28e1a91fe41018b
Patch4:		%{name}-objective-offset.patch

BuildRequires:	coin-or-CoinUtils-doc
BuildRequires:	coin-or-Data-Netlib
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	glpk-devel
%ifnarch %{ix86}
BuildRequires:	libsoplex-devel
%endif
BuildRequires:	make
BuildRequires:	pkgconfig(coinutils)

%description
The COIN-OR Open Solver Interface Library is a collection of solver
interfaces (SIs) that provide a common interface --- the OSI API --- for all
the supported solvers.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-CoinUtils-devel%{?_isa}
Requires:	glpk-devel%{?_isa}
%ifnarch %{ix86}
Requires:	libsoplex-devel%{?_isa}
%endif
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-CoinUtils-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @OSILIB_PCLIBS@/\nLibs.private:&/' Osi/osi.pc.in

# Change dependencies on zlib to dependencies on zlib-ng
sed -i 's/-lz/-lz-ng/' Osi/src/OsiSpx/Makefile.{am,in}

%build
export CPPFLAGS='-DNDEBUG'
%configure \
%ifnarch %{ix86}
  --with-soplex-incdir=%{_includedir}/soplex --with-soplex-lib=-lsoplex \
%endif
  --with-glpk-incdir=%{_includedir} --with-glpk-lib=-lglpk

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
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,osi_addlibs.txt}
cp -a doxydoc/{html,*.tag} README.md Osi/CHANGELOG %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README.md
%{_libdir}/libOsi.so.1
%{_libdir}/libOsi.so.1.*
%{_libdir}/libOsiCommonTests.so.1
%{_libdir}/libOsiCommonTests.so.1.*
%{_libdir}/libOsiGlpk.so.1
%{_libdir}/libOsiGlpk.so.1.*
%ifnarch %{ix86}
%{_libdir}/libOsiSpx.so.1
%{_libdir}/libOsiSpx.so.1.*
%endif

%files		devel
%{_includedir}/coin/*
%{_libdir}/libOsi.so
%{_libdir}/libOsiCommonTests.so
%{_libdir}/libOsiGlpk.so
%{_libdir}/pkgconfig/osi.pc
%{_libdir}/pkgconfig/osi-glpk.pc
%{_libdir}/pkgconfig/osi-unittests.pc
%ifnarch %{ix86}
%{_libdir}/libOsiSpx.so
%{_libdir}/pkgconfig/osi-soplex.pc
%endif

%files		doc
%{_docdir}/%{name}/CHANGELOG
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/osi_doxy.tag

%changelog
%autochangelog
