%global source0_hash 953ef4c2547b1611f90102f531f362bcfd6c76751eba2ae8c0f23b38947ef48d

%{?mingw_package_header}

%global pkgname vulkan-utility-libraries
%global srcname Vulkan-Utility-Libraries

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')

Name:          mingw-%{pkgname}
Version:       1.4.328.1
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-vulkan-headers >= %{baseversion}

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-vulkan-headers >= %{baseversion}

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

%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}

%build
%mingw_cmake -G Ninja
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-%{pkgname}
%license LICENSES/Apache-2.0.txt
%{mingw32_includedir}/vulkan/
%{mingw32_libdir}/libVulkanLayerSettings.a
%{mingw32_libdir}/libVulkanSafeStruct.a
%{mingw32_libdir}/cmake/VulkanUtilityLibraries/

%files -n mingw64-%{pkgname}
%license LICENSES/Apache-2.0.txt
%{mingw64_includedir}/vulkan/
%{mingw64_libdir}/libVulkanLayerSettings.a
%{mingw64_libdir}/libVulkanSafeStruct.a
%{mingw64_libdir}/cmake/VulkanUtilityLibraries/

%changelog
%autochangelog
