%global source0_hash 94efc160a2761de75df534707fd2ec53949c5389296d20ddbac1b285fe26d1ad
Name:		L-function
Version:	2.0.5
Release:        1%{?dist}
Summary:        C++ L-function class library and command line interface
License:	GPL-2.0-or-later
URL:		https://gitlab.com/sagemath/lcalc
VCS:		git:%{url}.git
Source0:        https://gitlab.com/sagemath/lcalc/-/archive/%{version}/lcalc-%{version}.tar.bz2
Patch0:		%{name}-mismatched-delete.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pari-devel
# /oreon:deps
%description
C++ L-function class library and command line interface.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
Headers and libraries for development with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lcalc-%{version}

autoreconf -fi .

%build

%configure --with-pari
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/libLfunction.la
rm -fr %{buildroot}%{_docdir}/lcalc
%oreon_autofiles L-function-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n L-function-devel -f %{oreon_filedir}/L-function-devel.list

%changelog

%autochangelog
