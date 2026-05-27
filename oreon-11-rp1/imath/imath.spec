%global source0_hash 8a1bc258f3149b5729c2f4f8ffd337c0e57f09096e4ba9784329f40c4a9035da

%global srcname Imath
%global sover 29
%global pyver_under %(%{python3} -Esc "import sys; sys.stdout.write('{0.major}_{0.minor}'.format(sys.version_info))")

Name:           imath
Version:        3.1.12
Release:        6%{?dist}
Summary:        Library of 2D and 3D vector, matrix, and math operations for computer graphics

License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/Imath
Source0:        https://github.com/AcademySoftwareFoundation/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

Patch0:         imath-disable-python-testPlane.patch

BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  python3-devel
# For documentation generation
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -n %{srcname}-%{version}
%patch -P0 -p1


%build
%cmake  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DPYTHON=ON \
		-DDOCS=ON \
		-DINSTALL_DOCS=OFF \
		--trace-source=docs/CMakeLists.txt

%cmake_build


%install
%cmake_install

# Fixup documentation so it can get installed correctly in imath-devel
#rm -rf %{__cmake_builddir}/docs/sphinx/.{doctrees,buildinfo}
#mv %{__cmake_builddir}/docs/sphinx ./html


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
#doc html/
%{_includedir}/Imath/
%{_libdir}/pkgconfig/Imath.pc
%{_libdir}/pkgconfig/PyImath.pc
%{_libdir}/cmake/Imath/
%{_libdir}/libImath.so
%{_libdir}/libImath-3_1.so
%{_libdir}/libPyImath_Python%{pyver_under}-3_1.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.12-6
- Prepare for Oreon 11 (RP1)
