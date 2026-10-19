%global source0_hash 16a7ad9b31ba5880dac55d62b5d6f243c3ebc8d46a3514149e56b5e7ea81f85f
%global debug_package %{nil}
%bcond mingw %[%{undefined rhel} || %{defined epel}]
Name:           cereal
Version:        1.3.2
Release:        13%{?dist}
Summary:        A header-only C++11 serialization library
License:        BSD-3-Clause AND BSL-1.0 AND Zlib AND MIT AND (MIT OR BSL-1.0)
Url:            http://uscilab.github.io/cereal/
Source0:        https://github.com/USCiLab/cereal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %{with mingw}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

%package devel
Summary:        Development headers and libraries for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains development headers and libraries for the cereal library

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%{cmake} -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
%cmake_build
%if %{with mingw}
%mingw_cmake -DSKIP_PORTABILITY_TEST=ON -DBUILD_SANDBOX=OFF -DWITH_WERROR=OFF
%mingw_make_build
%endif
%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%oreon_autofiles cereal-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-cereal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-cereal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%ifarch ppc64le
%global testargs --exclude-regex '\(test_complex\|test_pod\)'
%endif
%ctest  --output-on-failure %{?testargs}
%files -f %{oreon_filedir}/main.list
%files -n cereal-devel -f %{oreon_filedir}/cereal-devel.list
%files -n mingw32-cereal -f %{oreon_filedir}/mingw32-cereal.list
%files -n mingw64-cereal -f %{oreon_filedir}/mingw64-cereal.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-13
- Prepare for Oreon 11 (RP1)
