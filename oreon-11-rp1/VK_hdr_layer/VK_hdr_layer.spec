%global source0_hash 83cec91f377702d97c2d7ef14000f62a0e38196e8c9107db2ff2a6234541d543

%global commitdate 20250416
%global commithash 3b276e68136eb10825aa7cabd06abb324897f0e8
%global shortcommit %(c=%{commithash}; echo ${c:0:7})

Name:           VK_hdr_layer
Version:        0~git%{commitdate}.%{shortcommit}
Release:        4%{?dist}
Summary:        Vulkan Wayland HDR WSI Layer

License:        MIT
URL:            https://github.com/zamundaaa/VK_hdr_layer
Source:         %{url}/archive/%{commithash}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(vkroots)
BuildRequires:  pkgconfig(wayland-client)

# KWin is the main reference supported compositor
Enhances:       kwin-wayland >= 6.3

%description
Vulkan layer utilizing a small color management/HDR
protocol for experimentation.
The proposed mainline protocol for color management is
wp_color_management.

This implements the following vulkan extensions,
if the protocol is supported by the compositor.

* VK_EXT_swapchain_colorspace
* VK_EXT_hdr_metadata

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commithash} -p1

%conf
%meson --libdir=%{_libdir}/%{name}

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}/libVkLayer_hdr_wsi.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_hdr_wsi.*.json

%changelog
%autochangelog
