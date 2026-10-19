%global source0_hash 71af7b9799856d8b03619df3949e9c1be9703f8de0795af71399ba283cb27aac
%{?mingw_package_header}
%global pkgname minizip
Name:          mingw-%{pkgname}
Version:       4.2.2
Release:        1%{?dist}
Summary:        MinGW Windows minizip library
BuildArch:     noarch
License:       Zlib
URL:           https://github.com/zlib-ng/minizip-ng
Source0:        https://github.com/zlib-ng/%{pkgname}-ng/archive/%{version}/%{pkgname}-%{version}.tar.gz
Patch0:        mingw-minizip_libver.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-xz
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-zstd
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-xz
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-zstd
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-minizip -f %{oreon_filedir}/mingw32-minizip.list
%files -n mingw64-minizip -f %{oreon_filedir}/mingw64-minizip.list

%changelog

%autochangelog
