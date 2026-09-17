%global source0_hash eef1785d78639b228ae2de26b334129fe6a7d399c4ac6f8fc5bb9054ba00de64

%global		module		CoinUtils

%if 0%{?fedora}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:		coin-or-%{module}
Summary:	Coin-or Utilities
Version:	2.11.12
Release:	5%{?dist}

# The project as a whole is licensed EPL-2.0.  However, many source files still
# claim to be licensed EPL-1.0.  This is probably an upstream oversight.
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	glpk-devel
BuildRequires:	make
BuildRequires:	%{blaslib}-devel
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(coindatanetlib)
BuildRequires:	pkgconfig(coindatasample)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(zlib)

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch
# Fix invalid C constructs in the configure script
Patch1:		%{name}-configure-c99.patch

%description
CoinUtils (Coin-or Utilities) is an open-source collection of classes
and functions that are generally useful to more than one COIN-OR project.
These utilities include:

  * Vector classes
  * Matrix classes
  * MPS file reading
  * Comparing floating point numbers with a tolerance

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Sample
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @COINUTILSLIB_PCLIBS@/\nLibs.private:&/' CoinUtils/coinutils.pc.in

%build
%configure \
  --enable-coinutils-threads \
  --enable-gnu-packages \
  --with-blas-incdir=%{_includedir}/%{blaslib} \
  --with-blas-lib=-l%{blaslib} \
  --with-glpk-incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
  --with-lapack-incdir=%{_includedir}/%{blaslib} \
  --with-lapack-lib=-l%{blaslib}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,coinutils_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%{_pkgdocdir}/
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/coinutils_doxy.tag
%license LICENSE
%{_libdir}/libCoinUtils.so.3
%{_libdir}/libCoinUtils.so.3.*

%files devel
%{_includedir}/coin
%{_libdir}/libCoinUtils.so
%{_libdir}/pkgconfig/coinutils.pc

%files doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/coinutils_doxy.tag

%changelog
%autochangelog
