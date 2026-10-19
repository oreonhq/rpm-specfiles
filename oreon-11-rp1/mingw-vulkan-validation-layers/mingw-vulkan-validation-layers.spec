%global source0_hash 0858cd346e0d96bb18daaf25e731d362e96143c6f940ad6508c21f8019825d69
%{?mingw_package_header}
%global pkgname vulkan-validation-layers
%global srcname Vulkan-ValidationLayers
%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')
Name:          mingw-%{pkgname}
Version:       1.4.363
Release:        1%{?dist}
Summary:        MinGW Windows vulkan-validation-layers library
License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:        https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glslang
BuildRequires:  mingw32-spirv-headers
BuildRequires:  mingw32-spirv-tools
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw32-vulkan-utility-libraries
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glslang
BuildRequires:  mingw64-spirv-headers
BuildRequires:  mingw64-spirv-tools
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-vulkan-utility-libraries
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

%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}

%build

%mingw_cmake -G Ninja
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-vulkan-validation-layers -f %{oreon_filedir}/mingw32-vulkan-validation-layers.list
%files -n mingw64-vulkan-validation-layers -f %{oreon_filedir}/mingw64-vulkan-validation-layers.list

%changelog

%autochangelog
