%global source0_hash 1412a21b943c6e1db834ee2d74145aad20b3f62b12152d475613b8241d9cde10
Name:           libspiro
Version:        20240903
Release:        4%{?dist}
Summary:        Library to simplify the drawing of beautiful curves
License:        GPL-3.0-or-later
URL:            https://github.com/fontforge/libspiro/
Source0:        https://github.com/fontforge/libspiro/releases/download/%{version}/libspiro-dist-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libspiro-%{version}
%oreon_prep
%build

%configure --disable-static
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libspiro-devel -f %{oreon_filedir}/libspiro-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240903-4
- Import
