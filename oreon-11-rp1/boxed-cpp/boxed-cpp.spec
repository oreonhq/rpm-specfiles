%global source0_hash 75afd9c1627846ed350253b0885a71207a0c2d52f350ded86daa5d18712bad93

# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/contour-terminal/boxed-cpp
Version:        1.4.3
%forgemeta

Name:           boxed-cpp
Release:        %autorelease
Summary:        Boxing primitive types in C++
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  catch-devel

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake -DBOXED_CPP_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.txt
%doc README.md
%dir %{_includedir}/boxed-cpp
%{_includedir}/boxed-cpp/boxed.hpp
%{_libdir}/cmake/boxed-cpp/

%changelog
%autochangelog
