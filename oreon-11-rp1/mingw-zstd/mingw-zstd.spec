%global source0_hash 37d7284556b20954e56e1ca85b80226768902e2edabd3b649e9e72c0c9012ee3

%{?mingw_package_header}

%global pkgname zstd

Name:          mingw-%{pkgname}
Version:       1.5.7
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       BSD-3-Clause AND GPL-2.0-only
URL:           https://github.com/facebook/%{pkgname}
Source0:       https://github.com/facebook/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz


BuildRequires: make
BuildRequires: cmake

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
%autosetup -p1 -n %{pkgname}-%{version}


%build
MINGW32_CMAKE_ARGS="-DCMAKE_INSTALL_INCLUDEDIR=%{mingw32_includedir}/%{pkgname}" \
MINGW64_CMAKE_ARGS="-DCMAKE_INSTALL_INCLUDEDIR=%{mingw64_includedir}/%{pkgname}" \
%mingw_cmake -DZSTD_BUILD_PROGRAMS=OFF -DZSTD_BUILD_STATIC=OFF ../build/cmake/
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/lib%{pkgname}.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/cmake/%{pkgname}/
%{mingw32_libdir}/pkgconfig/lib%{pkgname}.pc
%{mingw32_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/lib%{pkgname}.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/cmake/%{pkgname}/
%{mingw64_libdir}/pkgconfig/lib%{pkgname}.pc
%{mingw64_includedir}/%{pkgname}/

%changelog
%autochangelog
