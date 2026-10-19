%global source0_hash 898e0d653860f996b0b4881d3715a4d236a25e3e82548426c6079ed5192fea08
%global debug_package %{nil}
Name:           reflection-cpp
Version:        0.4.0
Release:        1%{?dist}
Summary:        C++ static reflection support library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/reflection-cpp
Source0:        https://github.com/contour-terminal/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
C++ static reflection support library.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
C++ static reflection support library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n reflection-cpp-devel -f %{oreon_filedir}/reflection-cpp-devel.list

%changelog

%autochangelog
