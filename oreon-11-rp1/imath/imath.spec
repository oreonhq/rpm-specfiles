%global source0_hash e10c12b3f21f45bf08e09d4215d9c7691368d747beebd840de0b6fefed2df9f8
%global srcname Imath
%global sover 30
%global pyver_under %(%{python3} -Esc "import sys; sys.stdout.write('{0.major}_{0.minor}'.format(sys.version_info))")
Name:           imath
Version:        3.2.3
Release:        1%{?dist}
Summary:        Library of 2D and 3D vector, matrix, and math operations for computer graphics
License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/Imath
Source0:        https://github.com/AcademySoftwareFoundation/%{srcname}/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         imath-disable-python-testPlane.patch
Patch1:         imath-fix-quat-test-precision.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-breathe
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1

%build

%cmake  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DPYTHON=ON \
		-DDOCS=ON \
		-DINSTALL_DOCS=OFF \
		--trace-source=docs/CMakeLists.txt
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch aarch64
%ctest -E PyImath.PyImathTest
%else
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-imath -f %{oreon_filedir}/python3-imath.list
%files -n imath-devel -f %{oreon_filedir}/imath-devel.list

%changelog

%autochangelog
