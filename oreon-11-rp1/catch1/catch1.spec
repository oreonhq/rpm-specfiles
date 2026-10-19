%global source0_hash 27bf01d20692e534a8963f96c6ca797df2b4ba6551db0379510c376558d75e3c
%global debug_package %{nil}
Name:           catch1
Version:        1.12.2
Release:        1%{?dist}
Summary:        A modern, C++-native, header-only, framework for unit-tests, TDD and BDD
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         catch1-sigstksz.patch
Patch1:         catch1-cmake4.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
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

%cmake
%cmake_build
%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include  %{buildroot}%{_includedir}/catch
%oreon_autofiles catch1-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n catch1-devel -f %{oreon_filedir}/catch1-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.2-1
- Prepare for Oreon 11 (RP1)
