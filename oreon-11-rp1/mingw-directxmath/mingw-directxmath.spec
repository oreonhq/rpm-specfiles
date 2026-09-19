%global source0_hash 8ac7f060d7fcc971d77c5a9f3ff98548ecf119c144a7c2dd9d21f4b66ba94cd4

%{?mingw_package_header}
# Header-only package
%global debug_package %{nil}

%global pkgname directxmath
%global tag apr2025

Name:          mingw-%{pkgname}
Version:       3.20
Release:       6%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       MIT
URL:           https://github.com/microsoft/DirectXMath
Source0:       https://github.com/microsoft/DirectXMath/archive/%{tag}/%{pkgname}-%{version}.tar.gz
# Fix cmake module install dir
# Adapt header install dir
Patch0:        directxmath_cmake.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
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

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n DirectXMath-%{tag}

%build
%mingw_cmake
%mingw_make_build

%install
%mingw_make_install

%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_includedir}/directxmath/
%{mingw32_libdir}/pkgconfig/DirectXMath.pc
%{mingw32_datadir}/cmake/directxmath/

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_includedir}/directxmath/
%{mingw64_libdir}/pkgconfig/DirectXMath.pc
%{mingw64_datadir}/cmake/directxmath/

%changelog
%autochangelog
