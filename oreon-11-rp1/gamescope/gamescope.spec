%global source3_hash 37b77586e91f7ebee70380dcddd73bf01ae4acef1053e6be41d0485ede022422
%global source2_hash 3aa6feda7773cc8ffa8fb012fe95e6207c776101e29198d0e0d34a0c5e339f6a
%global source0_hash 9fe99fb4c7a80323cb7617825887dd8ff43e80a1e8c60a42740320eaa91ea01e
%global libliftoff_minver 0.5.0
%global reshade_commit 696b14cd6006ae9ca174e6164450619ace043283
%global reshade_shortcommit %(c=%{reshade_commit}; echo ${c:0:7})
%global vkroots_commit 5106d8a0df95de66cc58dc1ea37e69c99afc9540
%global vkroots_shortcommit %(c=%{vkroots_commit}; echo ${c:0:7})
Name:           gamescope
Version:        3.16.29
Release:        1%{?dist}
Summary:        Micro-compositor for video games on Wayland
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ValveSoftware/gamescope
ExcludeArch:    ppc64le
Source0:        https://github.com/ValveSoftware/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        stb.pc
Source2:        https://github.com/misyltoad/reshade/archive/%{reshade_commit}/reshade-%{reshade_shortcommit}.tar.gz
Source3:        https://github.com/misyltoad/vkroots/archive/%{vkroots_commit}/vkroots-%{vkroots_shortcommit}.tar.gz
Patch:          0001-cstdint.patch
Patch:          Allow-to-use-system-wlroots.patch
Patch:          Use-system-stb-glm.patch
Provides:       bundled(vkroots) = 0^20240429git5106d8a
Requires:       libliftoff%{?_isa} >= %{libliftoff_minver}
Requires:       xorg-x11-server-Xwayland
Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers
# oreon:deps
BuildRequires:  (pkgconfig(libliftoff) >= 0.5.0 with pkgconfig(libliftoff) < 0.6)
BuildRequires:  /usr/bin/glslangValidator
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glm-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXmu-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openvr)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  spirv-headers-devel
BuildRequires:  stb_image-devel
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
# /oreon:deps
%description
%{name} is the micro-compositor optimized for running video games on Wayland.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -N
# Install stub pkgconfig file
mkdir -p pkgconfig
cp %{SOURCE1} pkgconfig/stb.pc

# Replace spirv-headers include with the system directory
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

# Push in reshade and vkroots from sources instead of submodule
tar -xzf %{SOURCE2} --strip-components=1 -C src/reshade
tar -xzf %{SOURCE3} --strip-components=1 -C subprojects/vkroots

%autopatch -p1

%build

export PKG_CONFIG_PATH=pkgconfig
%meson \
    -Davif_screenshots=enabled \
    -Dbenchmark=enabled \
    -Ddrm_backend=enabled \
    -Denable_gamescope=true \
    -Denable_gamescope_wsi_layer=true \
    -Denable_openvr_support=true \
    -Dforce_fallback_for=[] \
    -Dinput_emulation=enabled \
    -Dpipewire=enabled \
    -Drt_cap=enabled \
    -Dsdl2_backend=enabled
%meson_build
%install
%meson_install --skip-subprojects
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
