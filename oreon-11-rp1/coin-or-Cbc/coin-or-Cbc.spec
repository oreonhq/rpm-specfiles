%global source0_hash 9ed71e4b61668462fc3794c102e26b4bb01a047efbbbcbd69ae7bde1f04f46a8
%global module Cbc
%global blaslib openblas
Name:		coin-or-%{module}
Summary:        Coin-or branch and cut
Version:	2.933
Release:        1%{?dist}
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:        https://github.com/coin-or/%{module}/archive/releases/%{version}/%{module}-%{version}.tar.gz
%ifnarch %{ix86}
%endif
Requires(post):   %{_sbindir}/alternatives
Requires(preun):  %{_sbindir}/alternatives
Obsoletes:	      coin-or-Cbc < 0:2.933-5
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-svnversion.patch
Patch2:		%{name}-exception.patch
Patch3:		%{name}-configure-c99.patch
Patch4:		%{name}-register.patch
Patch5:		%{name}-test.patch
# oreon:deps
BuildRequires:  MUMPS-devel
BuildRequires:  asl-devel
BuildRequires:  coin-or-Cgl-doc
BuildRequires:  coin-or-Clp-doc
BuildRequires:  coin-or-DyLP-doc
BuildRequires:  coin-or-Vol-doc
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig(cgl)
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(coindatamiplib3)
BuildRequires:  pkgconfig(coindatanetlib)
BuildRequires:  pkgconfig(dylp)
BuildRequires:  pkgconfig(highs)
BuildRequires:  pkgconfig(libnauty)
BuildRequires:  pkgconfig(vol)
# /oreon:deps
%description
Cbc (Coin-or branch and cut) is an open-source mixed integer programming
solver written in C++. It can be used as a callable library or using a
stand-alone executable. It can be called through AMPL (natively), GAMS
(using the links provided by the "Optimization Services" and "GAMSlinks"
projects), MPL (through the "CoinMP" project), AIMMS (through the "AIMMSlinks"
project), or "PuLP".

Cbc links to a number of other COIN projects for additional functionality,
including:

   * Clp (the default solver for LP relaxations)
   * Cgl (for cut generation)
   * CoinUtils (for reading input files and various utilities)

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Cgl-devel%{?_isa}
Requires:	coin-or-Clp-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Cgl-doc
Requires:	coin-or-Clp-doc
Requires:	coin-or-DyLP-doc
Requires:	coin-or-Vol-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
This package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @CBCLIB_PCLIBS@/\nLibs.private:&/' Cbc/cbc.pc.in

%build

export CPPFLAGS='-DNDEBUG'
%configure \
  --enable-cbc-parallel \
  --with-asl-incdir=%{_includedir}/asl \
  --with-asl-lib=-lasl \
  --with-blas-incdir=%{_includedir}/%{blaslib} \
  --with-blas-lib=-l%{blaslib} \
  --with-glpk-incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
%ifnarch %{ix86}
  --with-highs-incdir=%{_includedir}/highs \
  --with-highs-lib=-lhighs \
%endif
  --with-lapack-incdir=%{_includedir}/%{blaslib} \
  --with-lapack-lib=-l%{blaslib} \
  --with-mumps-incdir=%{_includedir}/MUMPS \
  --with-mumps-lib=-ldmumps \
  --with-nauty-incdir=%{_includedir}/nauty \
  --with-nauty-lib=-lnauty
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build all doxydoc
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,cbc_addlibs.txt}
cp -a README.md doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}
touch -c %{buildroot}%{_bindir}/coin.cbc
mv %{buildroot}%{_bindir}/cbc %{buildroot}%{_bindir}/Cbc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{_sbindir}/update-alternatives --verbose --install %{_bindir}/coin.cbc CoinCbc %{_bindir}/Cbc 2
%preun

if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --verbose --remove-all CoinCbc
fi
%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test
%files -f %{oreon_filedir}/main.list
%files -n coin-or-Cbc-devel -f %{oreon_filedir}/coin-or-Cbc-devel.list
%files -n coin-or-Cbc-doc -f %{oreon_filedir}/coin-or-Cbc-doc.list

%changelog

%autochangelog
