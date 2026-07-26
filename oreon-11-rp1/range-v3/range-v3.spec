%global source0_hash 015adb2300a98edfceaf0725beec3337f542af4915cec4d0b89fa0886f4ba9cb

%global debug_package %{nil}

Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.12.0
Release: 10%{?dist}

License: BSL-1.0
URL: https://github.com/ericniebler/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DRANGES_ENABLE_WERROR:BOOL=OFF \
    -DRANGES_MODULES:BOOL=OFF \
    -DRANGES_NATIVE:BOOL=OFF \
    -DRANGE_V3_DOCS:BOOL=OFF \
    -DRANGE_V3_EXAMPLES:BOOL=OFF \
    -DRANGE_V3_PERF:BOOL=OFF \
    -DRANGE_V3_TESTS:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md CREDITS.md TODO.md
%license LICENSE.txt
%exclude %{_includedir}/module.modulemap
%{_includedir}/{meta,range,concepts,std}
%{_libdir}/cmake/%{name}

%changelog
%autochangelog
