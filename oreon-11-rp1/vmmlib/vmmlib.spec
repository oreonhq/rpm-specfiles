%global source0_hash 32d45d81633d4e8e6eb7b52fbdd44db53b68df06557e786e5900cc1ceddddde7

%global git_commit 364732e348679893686ae46e8747cb17b0656d86
%global git_date 20220222

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:          vmmlib
Version:       1.8.0
Release:       0.10.%{git_suffix}%{?dist}
Summary:       A vector and matrix math library implemented using C++ templates
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
#URL:           http://vmmlib.sourceforge.net/
URL:           http://github.com/VMML/vmmlib/
#Source0:       http://github.com/VMML/vmmlib/archive/release-%%{version}.tar.gz#/%%{name}-release-%%{version}.tar.gz
Source0:       %{url}/archive/%{git_commit}/%{name}-%{version}-%{git_suffix}.tar.gz
BuildArch:     noarch
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: cmake
BuildRequires: boost-devel
# https://github.com/VMML/vmmlib/pull/101
Patch:         vmmlib-1.8.0-gcc-13-fix.patch
# https://github.com/VMML/vmmlib/issues/103
# https://github.com/Eyescale/CMake/pull/606
Patch:         vmmlib-1.8.0-cmake-4-fix.patch

%description
vmmlib is a vector and matrix math library implemented using C++ templates.
Its basic functionality includes a vector and a matrix class, with additional
functionality for the often-used 3d and 4d vectors and 3x3 and 4x4 matrices.
More advanced functionality include solvers, frustum computations and frustum
culling classes, and spatial data structures.

%package devel
Summary:       A vector and matrix math library implemented using C++ templates
Requires:      pkgconfig, cmake

%description devel
vmmlib is a vector and matrix math library implemented using C++ templates.
Its basic functionality includes a vector and a matrix class, with additional
functionality for the often-used 3d and 4d vectors and 3x3 and 4x4 matrices.
More advanced functionality include solvers, frustum computations and frustum
culling classes, and spatial data structures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build
%cmake
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/vmmlib/tests/*
rmdir %{buildroot}%{_datadir}/vmmlib/tests
mkdir -p %{buildroot}%{_includedir}
cp -a vmmlib %{buildroot}%{_includedir}

%check
%ctest

%files devel
%license LICENSE.txt
%doc doc/RELNOTES.md CHANGES README.md AUTHORS ACKNOWLEDGEMENTS
%{_includedir}/vmmlib
%{_datadir}/vmmlib/CMake/*.cmake

%changelog
%autochangelog
