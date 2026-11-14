# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 91f88fc43abb36821a568c7fbb3f815e9baf946d5fe187928df279708d45e509

Name: vulkan-loader
Version: 1.4.350.0
Release: 1%{?dist}
Summary: Vulkan ICD loader
License: Apache-2.0
URL: https://github.com/KhronosGroup/Vulkan-Loader
Source0: %{url}/archive/refs/tags/vulkan-sdk-%{version}.tar.gz#/Vulkan-Loader-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: ninja-build
BuildRequires: pkgconfig
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xrandr)
BuildRequires: vulkan-headers = %{version}

Provides: vulkan = %{version}-%{release}

%description
The Vulkan loader discovers and loads Vulkan drivers on the system.

%package devel
Summary: Development files for the Vulkan loader
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: vulkan-headers = %{version}
Provides: pkgconfig(vulkan) = %{version}

%description devel
Linker and pkg-config files for applications using Vulkan.

%prep
%oreon_sha256
%autosetup -n Vulkan-Loader-vulkan-sdk-%{version}

%build
%cmake \
  -G Ninja \
  -DBUILD_TESTS=OFF \
  -DBUILD_WERROR=OFF
%cmake_build

%install
%cmake_install

%check
PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig pkg-config --validate vulkan
cat > loader-smoke.c <<'EOF'
#include <vulkan/vulkan.h>
int main(void) {
    uint32_t version = 0;
    return vkEnumerateInstanceVersion(&version) != VK_SUCCESS;
}
EOF
gcc loader-smoke.c -L%{buildroot}%{_libdir} \
  -Wl,-rpath,%{buildroot}%{_libdir} -lvulkan \
  -o loader-smoke
./loader-smoke

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libvulkan.so.1*

%files devel
%{_libdir}/libvulkan.so
%{_libdir}/pkgconfig/vulkan.pc
%{_libdir}/cmake/VulkanLoader/

%changelog
%autochangelog
