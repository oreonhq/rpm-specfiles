%global source0_hash 3fc9c17e993e1dc1c5de95a253c632807d4c2b1cf4862b61aa9a55680ed15ac1
%global debug_package %{nil}
Name: semver
Version: 1.0.1
Release:        1%{?dist}
License: MIT
Summary:        Semantic Versioning for modern C++
URL: https://github.com/Neargye/%{name}
Source0:        https://github.com/Neargye/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%else
%endif
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
C++ library compare and manipulate versions are available as extensions to the
<major>.<minor>.<patch>-<prerelease_type>.<prerelease_number> format complying
with Semantic Versioning 2.0.0.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Unbundling catch...
rm -rf test/3rdparty/Catch2
ln -svf %{_includedir}/catch2 test/3rdparty/Catch2

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSEMVER_OPT_BUILD_EXAMPLES:BOOL=ON \
    -DSEMVER_OPT_BUILD_TESTS:BOOL=ON \
    -DSEMVER_OPT_INSTALL:BOOL=ON
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n semver-devel -f %{oreon_filedir}/semver-devel.list

%changelog

%autochangelog
