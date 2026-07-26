%global source0_hash 898e0d653860f996b0b4881d3715a4d236a25e3e82548426c6079ed5192fea08

# header-only library
%global debug_package %{nil}

Name:           reflection-cpp
Version:        0.4.0
Release:        %autorelease
Summary:        C++ static reflection support library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/reflection-cpp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
C++ static reflection support library.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
C++ static reflection support library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc README.md
%dir %{_includedir}/reflection-cpp
%{_includedir}/reflection-cpp/reflection.hpp
%{_libdir}/cmake/reflection-cpp

%changelog
%autochangelog
