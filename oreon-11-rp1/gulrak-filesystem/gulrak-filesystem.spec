%global source0_hash f4a098ed48e3b25b87b2be84cde58c884177af6b4ce27666ed2dbfe907b24418
%bcond system_catch2 1
Name:           gulrak-filesystem
Version:        1.5.16
Release:        1%{?dist}
Summary:        Implementation of C++17 std::filesystem for C++11/14/17/20
License:        MIT
URL:            https://github.com/gulrak/filesystem
Source0:        https://github.com/gulrak/filesystem/archive/v%{version}/filesystem-%{version}.tar.gz
%if %{with system_catch2}
%endif
%global debug_package %{nil}
%global common_description %{expand:
This is a header-only single-file std::filesystem compatible helper library,
based on the C++17 and C++20 specs, but implemented for C++11, C++14, C++17 or
C++20 (tightly following the C++17 standard with very few documented
exceptions). It is currently tested on macOS 10.12/10.14/10.15, Windows 10,
Ubuntu 18.04, Ubuntu 20.04, CentOS 7, CentOS 8, FreeBSD 12 and Alpine ARM/ARM64
Linux but should work on other systems too, as long as you have at least a
C++11 compatible compiler. It should work with Android NDK, Emscripten and I
even had reports of it being used on iOS (within sandboxing constraints) and
with v1.5.6 there is experimental support for QNX. The support of Android NDK,
Emscripten and QNX is not backed up by automated testing but PRs and bug
reports are welcome for those too. It is of course in its own namespace
ghc::filesystem to not interfere with a regular std::filesystem should you use
it in a mixed C++17 environment (which is possible).}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(catch2)
# /oreon:deps
%description %{common_description}

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n filesystem-%{version}

%if %{with system_catch2}
# Remove bundled Catch library and use the system version
rm -vf test/catch.hpp
sed -r -i 's|(include[[:blank:]]+")(catch.hpp")|\1catch2/\2|' test/*.cpp
sed -r -i 's|[[:blank:]]+catch\.hpp||' test/CMakeLists.txt
%endif

%conf
%cmake

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n gulrak-filesystem-devel -f %{oreon_filedir}/gulrak-filesystem-devel.list

%changelog

%autochangelog
