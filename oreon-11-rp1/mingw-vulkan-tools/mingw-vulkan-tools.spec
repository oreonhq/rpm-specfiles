%global source1_hash 14ec2632918e0855f035a661bd6704abec801f8b8c1eab3903933b4cfd3bd2e0
%global source0_hash 4d5669d4e06e9901eff2fdefdf638d267c9ed7f50caf964f69a218754cf8abd7
%{?mingw_package_header}
%global pkgname vulkan-tools
%global srcname Vulkan-Tools
%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')
Name:          mingw-%{pkgname}
Version:       1.4.363
Release:        1%{?dist}
Summary:        MinGW Windows vulkan-tools
License:       Apache-2.0 AND MIT
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:        https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz
Source1:       https://github.com/zeux/volk/archive/vulkan-sdk-%{version}.tar.gz#/volk-vulkan-sdk-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw32-vulkan-loader
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-vulkan-loader
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

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version} -a1
cp -a volk-vulkan-sdk-%{version}/LICENSE.md LICENSE_volk.md

%build

pushd volk-vulkan-sdk-%{version}
%mingw_cmake -G Ninja -DVOLK_INSTALL:BOOL=ON
%mingw_ninja -v
DESTDIR=$PWD/dist ninja -C build_win32 install
DESTDIR=$PWD/dist ninja -C build_win64 install
popd
MINGW32_CMAKE_ARGS="-Dvolk_DIR=$PWD/volk-vulkan-sdk-%{version}/dist/%{mingw32_libdir}/cmake/volk" \
MINGW64_CMAKE_ARGS="-Dvolk_DIR=$PWD/volk-vulkan-sdk-%{version}/dist/%{mingw64_libdir}/cmake/volk" \
%mingw_cmake -G Ninja
%mingw_ninja -v
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-vulkan-tools -f %{oreon_filedir}/mingw32-vulkan-tools.list
%files -n mingw64-vulkan-tools -f %{oreon_filedir}/mingw64-vulkan-tools.list

%changelog

%autochangelog
