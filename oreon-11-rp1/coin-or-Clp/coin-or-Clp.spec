%global source0_hash 2c078e174dc1a7a308e091b6256fb34b4017897fc140ea707ba207b2913ea46d
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global		module		Clp
%bcond bootstrap 0
Name:		coin-or-%{module}
Summary:        Coin-or linear programming
Version:	1.17.11
Release:        1%{?dist}
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:        https://github.com/coin-or/%{module}/archive/releases/%{version}/%{module}-%{version}.tar.gz
%if %{without bootstrap}
%endif
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-bad-cast.patch
Patch2:		%{name}-param.patch
Patch3:		%{name}-catch.patch
Patch4:		%{name}-overflow.patch
Patch5:		%{name}-signed.patch
Patch6:		%{name}-no-avx.patch
Patch7: coin-or-Clp-configure-c99.patch
Patch8: coin-or-Clp-configure-amd_defaults-c99.patch
# oreon:deps
BuildRequires:  MUMPS-devel
BuildRequires:  asl-devel
BuildRequires:  coin-or-Data-Netlib
BuildRequires:  coin-or-Osi-doc
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(readline)
BuildRequires:  suitesparse-devel
# /oreon:deps
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
%oreon_autofiles coin-or-Clp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-Clp-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test
%files -f %{oreon_filedir}/main.list
%files -n coin-or-Clp-devel -f %{oreon_filedir}/coin-or-Clp-devel.list
%files -n coin-or-Clp-doc -f %{oreon_filedir}/coin-or-Clp-doc.list

%changelog

%autochangelog
