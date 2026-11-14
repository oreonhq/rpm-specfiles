# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 70270d10bf2c1e074a06ee37a50b75d332993d1b80a1d9526eeed2da6d82ed22

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: vulkan-headers
Version: 1.4.350.0
Release: 1%{?dist}
Summary: Vulkan Header files and API registry
License: Apache-2.0
URL: https://github.com/KhronosGroup/Vulkan-Headers
Source0: %{url}/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-Headers-sdk-%{version}.tar.gz

BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: gcc-c++

%description
Vulkan Header files and API registry

%prep
%oreon_sha256

%autosetup -n Vulkan-Headers-vulkan-sdk-%{version} -p1

%build
%cmake \
    -G Ninja \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    %{nil}
%cmake_build

%install
%cmake_install

%check
test -f %{buildroot}%{_includedir}/vulkan/vulkan.h
test -f %{buildroot}%{_datadir}/vulkan/registry/vk.xml

%files
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%dir %{_datadir}/cmake/VulkanHeaders/
%{_datadir}/vulkan/registry/
%{_datadir}/cmake/VulkanHeaders/*.cmake

%changelog
%autochangelog
