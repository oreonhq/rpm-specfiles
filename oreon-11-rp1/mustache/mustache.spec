%global source0_hash acd66359feb4318b421f9574cfc5a511133a77d916d0b13c7caa3783c0bfe167
%global appname Mustache
Name: mustache
Version: 4.1
Release:        1%{?dist}
License: BSL-1.0
Summary:        Mustache text templates for modern C++
URL: https://github.com/kainjow/%{appname}
Source0:        https://github.com/kainjow/%{appname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch100: %{name}-4.1-catch-fixes.patch
Patch101: %{name}-4.1-cmake4-fixes.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
Text templates implementation for modern C++ (requires C++11).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The %{name}-devel package contains C++ headers for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{appname}-%{version}
sed -e '/-Werror/d' -i CMakeLists.txt
ln -svf %{_includedir}/catch2/catch.hpp ./catch.hpp

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
%check

%ctest
%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p %{name}.hpp %{buildroot}%{_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mustache-devel -f %{oreon_filedir}/mustache-devel.list

%changelog

%autochangelog
