%global source0_hash 64977c08979e03b3da7830f86a3959c703add5d351889634fc66954176db9436
%global debug_package %{nil}
Name:           polylabel
Version:        2.1.0
Release:        1%{?dist}
Summary:        A fast algorithm for finding the pole of inaccessibility of a polygon
License:        ISC
URL:            https://github.com/mapbox/polylabel/
Source0:        https://github.com/mapbox/polylabel/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          polylabel-mason.patch
Requires:       geometry-hpp-devel
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  geometry-hpp-devel
BuildRequires:  geometry-hpp-static
BuildRequires:  make
BuildRequires:  rapidjson-devel
BuildRequires:  rapidjson-static
# /oreon:deps
%description
A fast algorithm for finding polygon pole of inaccessibility, the most
distant internal point from the polygon outline.

Useful for optimal placement of a text label on a polygon.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
A fast algorithm for finding polygon pole of inaccessibility, the most
distant internal point from the polygon outline.

Useful for optimal placement of a text label on a polygon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n polylabel-devel -f %{oreon_filedir}/polylabel-devel.list

%changelog

%autochangelog
