%global source0_hash 8d6a4092d5de62d0c6290394cf81cf7a99e36875934b1b75d595e76d08fcadd1

%{?mingw_package_header}

%global pkgname vulkan-tools
%global srcname Vulkan-Tools

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')

Name:          mingw-%{pkgname}
Version:       1.4.328.1
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname}

# volk.h is MIT
License:       Apache-2.0 AND MIT
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz
Source1:       https://github.com/zeux/volk/archive/vulkan-sdk-%{version}.tar.gz#/volk-vulkan-sdk-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-vulkan-headers >= %{baseversion}
BuildRequires: mingw32-vulkan-loader >= %{baseversion}

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-vulkan-headers >= %{baseversion}
BuildRequires: mingw64-vulkan-loader >= %{baseversion}

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
# Build volk
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

%files -n mingw32-%{pkgname}
%license LICENSE.txt LICENSE_volk.md
%{mingw32_bindir}/vkcube.exe
%{mingw32_bindir}/vkcubepp.exe
%{mingw32_bindir}/vulkaninfo.exe

%files -n mingw64-%{pkgname}
%license LICENSE.txt LICENSE_volk.md
%{mingw64_bindir}/vkcube.exe
%{mingw64_bindir}/vkcubepp.exe
%{mingw64_bindir}/vulkaninfo.exe

%changelog
%autochangelog
