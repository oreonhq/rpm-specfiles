%global source0_hash 64977c08979e03b3da7830f86a3959c703add5d351889634fc66954176db9436

%global debug_package %{nil}

Name:           polylabel
Version:        2.1.0
Release:        1%{?dist}
Summary:        A fast algorithm for finding the pole of inaccessibility of a polygon

License:        ISC
URL:            https://github.com/mapbox/polylabel/
Source0:        https://github.com/mapbox/polylabel/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable mason dependency handling
Patch:          polylabel-mason.patch

BuildRequires:  make gcc-c++
BuildRequires:  geometry-hpp-devel geometry-hpp-static
BuildRequires:  rapidjson-devel rapidjson-static

Requires:       geometry-hpp-devel

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

%autosetup

%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}

%check
%make_build test

%files devel
%license LICENSE
%doc README.md
%{_includedir}/mapbox

%changelog
%autochangelog
