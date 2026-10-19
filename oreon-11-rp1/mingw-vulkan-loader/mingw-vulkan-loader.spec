%global source0_hash 2d5e5a84e83c5360a828d02d828e900380ecf1ac8c7d3182650b7755d11cf536
%{?mingw_package_header}
%global pkgname vulkan-loader
%global srcname Vulkan-Loader
%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')
Name:          mingw-%{pkgname}
Version:       1.4.364
Release:        1%{?dist}
Summary:        MinGW Windows vulkan-loader library
License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:        https://github.com/KhronosGroup/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  ninja-build
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%mingw_cmake -G Ninja -DUSE_MASM=OFF -DENABLE_WERROR=OFF
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-vulkan-loader -f %{oreon_filedir}/mingw32-vulkan-loader.list
%files -n mingw64-vulkan-loader -f %{oreon_filedir}/mingw64-vulkan-loader.list

%changelog

%autochangelog
