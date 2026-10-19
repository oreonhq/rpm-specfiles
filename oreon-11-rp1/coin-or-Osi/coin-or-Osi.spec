%global source0_hash 1d80d0b4275f2e1ceefc6dda66b8616e3a8c8b07a926ef4456db4a0d55249333
%global		module		Osi
Name:		coin-or-%{module}
Summary:        COIN-OR Open Solver Interface Library
Version:	0.108.12
Release:        1%{?dist}
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:        https://github.com/coin-or/%{module}/archive/releases/%{version}/%{module}-%{version}.tar.gz
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-glpk.patch
Patch2:		%{name}-configure-c99.patch
Patch3:		%{name}-soplex.patch
Patch4:		%{name}-objective-offset.patch
%ifnarch %{ix86}
%endif
# oreon:deps
BuildRequires:  coin-or-CoinUtils-doc
BuildRequires:  coin-or-Data-Netlib
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  pkgconfig(coinutils)
# /oreon:deps
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
%oreon_autofiles coin-or-Osi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-Osi-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test
%files -f %{oreon_filedir}/main.list
%files -n coin-or-Osi-devel -f %{oreon_filedir}/coin-or-Osi-devel.list
%files -n coin-or-Osi-doc -f %{oreon_filedir}/coin-or-Osi-doc.list

%changelog

%autochangelog
