%global source0_hash 972d7e5b2cc9b7b8f9b43fe637b4260a2035bef5bb59bbb7fbf02434610c2b3f
%{?mingw_package_header}
%global pkgname vulkan-utility-libraries
%global srcname Vulkan-Utility-Libraries
%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')
Name:          mingw-%{pkgname}
Version:       1.4.364
Release:        1%{?dist}
Summary:        MinGW Windows vulkan-utility-libraries
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
MinGW Windows %{pkgname}

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%mingw_cmake -G Ninja
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-vulkan-utility-libraries -f %{oreon_filedir}/mingw32-vulkan-utility-libraries.list
%files -n mingw64-vulkan-utility-libraries -f %{oreon_filedir}/mingw64-vulkan-utility-libraries.list

%changelog

%autochangelog
