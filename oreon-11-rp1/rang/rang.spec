%global source0_hash e835f79e71e1befb0b0c2906cfaa5cb07e12c6f88789931cd3c86c80c852453a
%global debug_package %{nil}
Name: rang
License: Unlicense
Summary:        Minimal, header-only, Modern C++ library for terminal goodies
Version: 3.3
Release:        1%{?dist}
URL: https://agauniyal.github.io/rang/
Source0:        https://github.com/agauniyal/rang/archive/v%{version}/rang-v%{version}.tar.gz
Patch0: 0000-rang-fix-tests.patch
%global with_tests 1
%if 0%{?with_tests}
%endif
%global desc %{expand:rang is a minimal, single-header library for colors in your terminal.
rang only depends on C++ standard library, "unistd.h" system header on Unix
and "windows.h" & "io.h" system headers on Windows-based systems.
In other words, you don't need any 3rd party dependencies.
}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(doctest)
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
%{desc}

%package devel
Summary: %{summary}
%description devel
This package contains development files for programs using the "rang" library.

%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%if 0%{?with_tests}
pushd test
%cmake
%cmake_build
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if 0%{?with_tests}
%check

pushd test/%{__cmake_builddir}
./all_rang_tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n rang-devel -f %{oreon_filedir}/rang-devel.list

%changelog

%autochangelog
