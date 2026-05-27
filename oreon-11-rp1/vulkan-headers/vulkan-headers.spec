%global source0_hash d73bc5036b6556b741f6985ff600ca720308c5f2850e4a43ceb498bd3de069e7

%global __python %{__python3}
Name:           vulkan-headers
Version:        1.4.341.0
Release:        %autorelease
Summary:        Vulkan Header files and API registry

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        https://github.com/KhronosGroup/Vulkan-Headers/archive/vulkan-sdk-1.4.341.0.tar.gz#/Vulkan-Headers-sdk-1.4.341.0.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildArch:      noarch       

%description
Vulkan Header files and API registry

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n Vulkan-Headers-vulkan-sdk-%{version}


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -GNinja
%cmake_build


%install
%cmake_install


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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.341.0-1
- Import
