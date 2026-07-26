%global source0_hash 8b42d9c33a6529a6c283a4f4c73c26326561ccc67fbb3e6a3225edd688b39973

# We do build some executables, but we don't package them, so no debuginfo
%global debug_package %{nil}

Name: rang
License: Unlicense
Summary: Minimal, header-only, Modern C++ library for terminal goodies

Version: 3.2
Release: 10%{?dist}

URL: https://agauniyal.github.io/rang/
Source0: https://github.com/agauniyal/rang/archive/v%{version}/rang-v%{version}.tar.gz

# Fix tests failing to build
Patch0: 0000-rang-fix-tests.patch

%global with_tests 1

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%if 0%{?with_tests}
BuildRequires: cmake(doctest)
%endif

%global desc %{expand:rang is a minimal, single-header library for colors in your terminal.
rang only depends on C++ standard library, "unistd.h" system header on Unix
and "windows.h" & "io.h" system headers on Windows-based systems.
In other words, you don't need any 3rd party dependencies.
}

%description
%{desc}

%package devel
Summary: %{summary}

%description devel
This package contains development files for programs using the "rang" library.

%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381405)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake

%if 0%{?with_tests}
pushd test
%cmake
%cmake_build
%endif

%install
%cmake_install

%if 0%{?with_tests}
%check
pushd test/%{__cmake_builddir}
./all_rang_tests
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
