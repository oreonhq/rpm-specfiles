# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8a1bc258f3149b5729c2f4f8ffd337c0e57f09096e4ba9784329f40c4a9035da
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname Imath
%global sover 29
%global pyver_under %(%{python3} -Esc "import sys; sys.stdout.write('{0.major}_{0.minor}'.format(sys.version_info))")

Name:           imath
Version:        3.1.12
Release:        1%{?dist}
Summary:        Library of 2D and 3D vector, matrix, and math operations for computer graphics

License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/Imath
Source0:        https://github.com/AcademySoftwareFoundation/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

Patch0:         imath-disable-python-testPlane.patch
Patch1:         imath-disable-python-testM44fArray.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  python3-devel
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  python3-breathe

%description
Imath is a basic, light-weight, and efficient C++ representation of 2D and 3D
vectors and matrices and other simple but useful mathematical objects,
functions, and data types common in computer graphics applications, including
the “half” 16-bit floating-point type.

%package -n python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Python module for Imath

%description -n python3-%{name}
%{summary}.

%package devel
Summary:        Development files for Imath
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       python3-devel

%description devel
%{summary}.

%prep
%oreon_sha256
%setup -n %{srcname}-%{version}
%patch -P0 -p1
%ifarch x86_64 && 0%{?rhel} >= 10
%patch -P1 -p1
%endif

%build
%cmake  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DPYTHON=ON \
		-DDOCS=ON \
		-DINSTALL_DOCS=OFF \
		--trace-source=docs/CMakeLists.txt

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%{_libdir}/libImath-3_1.so.%{sover}*

%files -n python3-%{name}
%{_libdir}/libPyImath_Python%{pyver_under}-3_1.so.%{sover}*
%{python3_sitearch}/imath.so
%{python3_sitearch}/imathnumpy.so

%files devel
%{_includedir}/Imath/
%{_libdir}/pkgconfig/Imath.pc
%{_libdir}/pkgconfig/PyImath.pc
%{_libdir}/cmake/Imath/
%{_libdir}/libImath.so
%{_libdir}/libImath-3_1.so
%{_libdir}/libPyImath_Python%{pyver_under}-3_1.so

%changelog
%autochangelog
