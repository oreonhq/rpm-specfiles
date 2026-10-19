%global source0_hash d54a712b7b1d7708bc7a819a8e6e47b2fde9536f487b89ccbca295072a7d9943
%global debug_package %{nil}
Name:           catch2
Version:        2.13.10
Release:        9%{?dist}
Summary:        Modern, C++-native, header-only, framework for unit-tests, TDD and BDD
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Conflicts:      catch-devel
%description    devel
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Catch2-%{version}
%oreon_prep
%build

%cmake \
    -DCATCH_BUILD_EXTRA_TESTS=ON \
    -DCATCH_ENABLE_WERROR=OFF \
    -DCATCH_INSTALL_DOCS=OFF \
    -DBUILD_SHARED_LIBS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles catch2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n catch2-devel -f %{oreon_filedir}/catch2-devel.list

%changelog

%autochangelog
