%global source0_hash c465aa56757e7746ac707f582b6e2d51546569a4a2488c1172fb543aa5fdfc2c

%{?mingw_package_header}

%global pkgname vulkan-headers
%global srcname Vulkan-Headers

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

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++

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
%license LICENSE.md
%{mingw32_includedir}/vulkan/
%{mingw32_includedir}/vk_video/
%{mingw32_datadir}/cmake/VulkanHeaders/
%{mingw32_datadir}/vulkan/

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_includedir}/vulkan/
%{mingw64_includedir}/vk_video/
%{mingw64_datadir}/cmake/VulkanHeaders/
%{mingw64_datadir}/vulkan/

%changelog
%autochangelog
