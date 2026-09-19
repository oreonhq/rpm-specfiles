%global source0_hash 8f6b28ab3640b5d76d5b6664dda7257a4405ce59179220431b8fd196c79b2ecb

# This is a header-only library, but it install also cmake
# scripts to %%{_libdir}, so it cannot be noarch.
%global debug_package %{nil}

Name: mpark-variant
Summary: C++17 std::variant for C++11/14/17
Version: 1.4.0
Release: 16%{?dist}

License: BSL-1.0
URL: https://github.com/mpark/variant
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n variant-%{version} -p1
sed -i 's@lib/@%{_libdir}/@g' CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.md
%{_includedir}/mpark
%{_libdir}/cmake/mpark_variant

%changelog
%autochangelog
