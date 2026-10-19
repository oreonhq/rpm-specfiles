%global source0_hash 8f6b28ab3640b5d76d5b6664dda7257a4405ce59179220431b8fd196c79b2ecb
%global debug_package %{nil}
Name: mpark-variant
Summary:        C++17 std::variant for C++11/14/17
Version: 1.4.0
Release:        1%{?dist}
License: BSL-1.0
URL: https://github.com/mpark/variant
Source0:        https://github.com/mpark/variant/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mpark-variant-devel -f %{oreon_filedir}/mpark-variant-devel.list

%changelog

%autochangelog
