%global source0_hash ff31a4ded6589387d029d7d10ec1d787420adf1ccdb2ec96ab2da92b4d5993a7

Name:           lest
Version:        1.37.0
Release:        %autorelease
Summary:        Tiny C++11 test framework

License:        BSL-1.0
URL:            https://github.com/martinmoene/lest
Source:         %{url}/archive/v%{version}/lest-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
A modern, C++11-native, single-file header-only, tiny framework for unit-tests,
TDD and BDD (includes C++98 variant).}

%description %{common_description}

%package devel
Summary:        Development files for %{name}

BuildArch:      noarch

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

The %{name}-devel package contains header files for developing applications
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lest-%{version} -p1

%conf
# https://github.com/martinmoene/lest/issues/56#issuecomment-344417309:
# > The numbered 'tests' are actually examples of which several fail for
# > educational reasons.
# >
# > CMake variable LEST_BUILD_EXAMPLE lets you control inclusion of the
# > examples in the build process; by default it's on.
%cmake -DLEST_BUILD_EXAMPLE:BOOL=OFF

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.txt
%doc CHANGES.txt
%doc README.md
%doc example/

%{_includedir}/lest/

%changelog
%autochangelog
