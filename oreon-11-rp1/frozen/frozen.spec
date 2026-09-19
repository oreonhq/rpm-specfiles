%global source0_hash ed8339c017d7c5fe019ac2c642477f435278f0dc643c1d69d3f3b1e95915e823

# Header-only package
%global debug_package %{nil}

Name:           frozen
Version:        1.2.0
Release:        4%{?dist}
Summary:        A header-only, constexpr alternative to gperf for C++14 users

License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/frozen
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake

%description
Header-only library that provides 0 cost initialization
for immutable containers, fixed-size containers, and
various algorithms.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Requires:       pkgconfig
Provides:       %{name}-static = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%license LICENSE
%doc examples/ AUTHORS README.rst
%{_includedir}/frozen/
%{_datadir}/cmake/%{name}/

%changelog
%autochangelog
