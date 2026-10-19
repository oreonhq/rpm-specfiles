%global source0_hash ddfea48e10209215748bc9f90a8c04abbb912b662c1aefaf280018d0a181ef79
%global		module		CoinUtils
%global blaslib openblas
Name:		coin-or-%{module}
Summary:        Coin-or Utilities
Version:	2.11.13
Release:        1%{?dist}
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:        https://github.com/coin-or/%{module}/archive/releases/%{version}/%{module}-%{version}.tar.gz
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-configure-c99.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  glpk-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(coindatanetlib)
BuildRequires:  pkgconfig(coindatasample)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
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
%oreon_autofiles coin-or-CoinUtils-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-CoinUtils-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test
%files -f %{oreon_filedir}/main.list
%files -n coin-or-CoinUtils-devel -f %{oreon_filedir}/coin-or-CoinUtils-devel.list
%files -n coin-or-CoinUtils-doc -f %{oreon_filedir}/coin-or-CoinUtils-doc.list

%changelog

%autochangelog
