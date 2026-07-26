%global source0_hash b4275d83fb95521510e389b8d13af10298ed5bed1c8e13efd961d91b1105e462

%{?mingw_package_header}

%global pkgname imath

Name:          mingw-%{pkgname}
Version:       3.2.2
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD-3-Clause
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:       https://github.com/AcademySoftwareFoundation/Imath/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++

%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Imath-%{version}

%build
%mingw_cmake -DIMATH_INSTALL_PKG_CONFIG=ON -DBUILD_TESTING=OFF
%mingw_make_build

%install
%mingw_make_install

%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/libImath-3_2.dll
%{mingw32_includedir}/Imath/
%{mingw32_libdir}/libImath-3_2.dll.a
%{mingw32_libdir}/cmake/Imath/
%{mingw32_libdir}/pkgconfig/Imath.pc

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/libImath-3_2.dll
%{mingw64_includedir}/Imath/
%{mingw64_libdir}/libImath-3_2.dll.a
%{mingw64_libdir}/cmake/Imath/
%{mingw64_libdir}/pkgconfig/Imath.pc

%changelog
%autochangelog
