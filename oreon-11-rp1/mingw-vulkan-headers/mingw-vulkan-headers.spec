%global source0_hash 37e00e30611375938a9437477de793e355e55d486c25ab3dfd7a1a11ab0f8f07
%{?mingw_package_header}
%global pkgname vulkan-headers
%global srcname Vulkan-Headers
Name:          mingw-%{pkgname}
Version:       1.4.364
Release:        1%{?dist}
Summary:        MinGW Windows vulkan-headers
License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:        https://github.com/KhronosGroup/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
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
%files -n mingw32-vulkan-headers -f %{oreon_filedir}/mingw32-vulkan-headers.list
%files -n mingw64-vulkan-headers -f %{oreon_filedir}/mingw64-vulkan-headers.list

%changelog

%autochangelog
