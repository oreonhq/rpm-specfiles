%global source0_hash 7059f4420d504c4bc96f8a462a0f6d029c5be914ba55cc030a0a773366dd7bc8

%global debug_package %{nil}

Name:           mapbox-variant
Version:        1.2.0
Release:        13%{?dist}
Summary:        A header-only alternative to boost::variant for C++11 and C++14

License:        BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/mapbox/variant
Source0:        https://github.com/mapbox/variant/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make gcc-c++
BuildRequires:  catch1-devel

%description
Mapbox variant has the same speedy performance of boost::variant but is
faster to compile, results in smaller binaries, and has no dependencies.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Mapbox variant has the same speedy performance of boost::variant but is
faster to compile, results in smaller binaries, and has no dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n variant-%{version}
sed -i -e 's/-Werror //' Makefile
sed -i -e 's/-march=native //' Makefile
rm -f test/include/catch.hpp

%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}

%check
%make_build test CXXFLAGS="-I/usr/include/catch %{optflags}"

%files devel
%doc README.md doc
%license LICENSE LICENSE_1_0.txt
%{_includedir}/mapbox

%changelog
%autochangelog
