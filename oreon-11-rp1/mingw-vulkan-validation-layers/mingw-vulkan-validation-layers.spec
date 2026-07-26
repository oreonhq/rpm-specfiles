%global source0_hash 91d9be1347a270288bcc50206bda8ccf6aad33bab8318c0643dd36bef97478f9

%{?mingw_package_header}

%global pkgname vulkan-validation-layers
%global srcname Vulkan-ValidationLayers

%define baseversion %(echo %{version} | awk -F'.' '{print $1"."$2"."$3}')

Name:          mingw-%{pkgname}
Version:       1.4.328.1
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-glslang
BuildRequires: mingw32-spirv-headers
BuildRequires: mingw32-spirv-tools
BuildRequires: mingw32-vulkan-headers >= %{baseversion}
BuildRequires: mingw32-vulkan-utility-libraries >= %{baseversion}

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-glslang
BuildRequires: mingw64-spirv-headers
BuildRequires: mingw64-spirv-tools
BuildRequires: mingw64-vulkan-headers >= %{baseversion}
BuildRequires: mingw64-vulkan-utility-libraries >= %{baseversion}

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

%files -n mingw32-%{pkgname}
%doc README.md
%license LICENSE.txt
%{mingw32_bindir}/VkLayer_khronos_validation.dll
%{mingw32_bindir}/VkLayer_khronos_validation.json

%files -n mingw64-%{pkgname}
%doc README.md
%license LICENSE.txt
%{mingw64_bindir}/VkLayer_khronos_validation.dll
%{mingw64_bindir}/VkLayer_khronos_validation.json

%changelog
%autochangelog
