%global source0_hash 41b7ac9402db883d9c487eb7101e59eb513cefd726e6e7a669dc94664d9385e6
%global		module		Cgl
Name:		coin-or-%{module}
Summary:        Cut Generation Library
Version:	0.60.10
Release:        1%{?dist}
License:	EPL-2.0 AND EPL-1.0
URL:		https://github.com/coin-or/%{module}
VCS:		git:%{url}.git
Source0:        https://github.com/coin-or/%{module}/archive/releases/%{version}/%{module}-%{version}.tar.gz
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-uninit.patch
Patch2:		%{name}-configure-c99.patch
Patch3:		%{name}-undef-EPS.patch
# oreon:deps
BuildRequires:  coin-or-CoinUtils-doc
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(dylp)
BuildRequires:  pkgconfig(vol)
# /oreon:deps
%description
The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators
that can be used with other COIN-OR packages that make use of cuts, such as,
among others, the linear solver Clp or the mixed integer linear programming
solvers Cbc or BCP.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Osi-devel%{?_isa}
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

%build

export CPPFLAGS='-DNDEBUG'
%configure
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build all doxydoc
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,cgl_addlibs.txt}
cp -a README.md doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}
%oreon_autofiles coin-or-Cgl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-Cgl-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test
%files -f %{oreon_filedir}/main.list
%files -n coin-or-Cgl-devel -f %{oreon_filedir}/coin-or-Cgl-devel.list
%files -n coin-or-Cgl-doc -f %{oreon_filedir}/coin-or-Cgl-doc.list

%changelog

%autochangelog
