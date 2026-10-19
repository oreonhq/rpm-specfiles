%global source0_hash 0957cae5821b17ce07f0833aaa52b5137643a8382203221f363a8303c109af34
Name:           catch
Version:        3.16.0
Release:        1%{?dist}
Summary:        Modern C++ unit test and micro-benchmark framework
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/v%{version}/Catch2-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python3
# /oreon:deps
%description
Catch2 is a C++ unit testing and micro-benchmarking framework.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description devel
Libraries and headers for applications using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Catch2-%{version}
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCATCH_BUILD_EXTRA_TESTS=ON \
    -DCATCH_ENABLE_WERROR=OFF \
    -DCATCH_INSTALL_DOCS=OFF \
    -DBUILD_SHARED_LIBS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles catch-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n catch-devel -f %{oreon_filedir}/catch-devel.list

%changelog

%autochangelog
