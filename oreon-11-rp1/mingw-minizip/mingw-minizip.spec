%global source0_hash 85417229bb0cd56403e811c316150eea1a3643346d9cec7512ddb7ea291b06f2

%{?mingw_package_header}

%global pkgname minizip

Name:          mingw-%{pkgname}
Version:       4.1.0
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       Zlib
URL:           https://github.com/zlib-ng/minizip-ng
Source0:       https://github.com/zlib-ng/minizip-ng/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Add a library version
Patch0:        mingw-minizip_libver.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-bzip2
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-openssl
BuildRequires: mingw32-xz
BuildRequires: mingw32-zlib
BuildRequires: mingw32-zstd

BuildRequires: mingw64-bzip2
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-openssl
BuildRequires: mingw64-xz
BuildRequires: mingw64-zlib
BuildRequires: mingw64-zstd

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

%autosetup -p1 -n %{pkgname}-ng-%{version}

%build
MINGW32_CMAKE_ARGS="-DINSTALL_INC_DIR=%{mingw32_includedir}/%{pkgname}" \
MINGW64_CMAKE_ARGS="-DINSTALL_INC_DIR=%{mingw64_includedir}/%{pkgname}" \
%mingw_cmake -DZSTD_FORCE_FETCH=OFF
%mingw_make_build

%install
%mingw_make_install

%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/lib%{pkgname}-1.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/cmake/%{pkgname}/
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc
%{mingw32_includedir}/%{pkgname}/

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/lib%{pkgname}-1.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/cmake/%{pkgname}/
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc
%{mingw64_includedir}/%{pkgname}/

%changelog
%autochangelog
