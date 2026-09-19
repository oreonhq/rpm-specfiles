%global source0_hash edad5faaa0bea1df124b5e8cb00bf0adbd2faeccecd3b5c146796cbcb8b5b71b

%global appname cmakerc
%global _description %{expand:
CMakeRC is a resource compiler provided in a single CMake script that can
easily be included in another project.

For the purpose of this project, a resource compiler is a tool that will
compile arbitrary data into a program. The program can then read this data
from without needing to store that data on disk external to the program.}

Name: cmrc
Version: 2.0.1
Release: %autorelease

License: MIT
Summary: Standalone CMake-Based C++ Resource Compiler
URL: https://github.com/vector-of-bool/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# https://github.com/vector-of-bool/cmrc/pull/40
Patch100: %{name}-installation.patch
# https://github.com/vector-of-bool/cmrc/pull/48
Patch101: %{name}-cmake-compatibility.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %{_description}

%package devel
Summary: Standalone CMake-Based C++ Resource Compiler
Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.txt
%{_datadir}/cmake/%{appname}/

%changelog
%autochangelog
