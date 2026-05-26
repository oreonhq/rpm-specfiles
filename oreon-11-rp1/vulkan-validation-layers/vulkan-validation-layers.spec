Name:           vulkan-validation-layers
Version:        1.4.341.0
Release:        %autorelease
Summary:        Vulkan validation layers

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source0:        https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/vulkan-sdk-1.4.341.0.tar.gz#/Vulkan-ValidationLayers-sdk-1.4.341.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 7f521490495e43561f70fe8b6317fd5cc13d4083413f1abf891f50cbabe12238
%global source0_file vulkan-sdk-1.4.341.0.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  glslang-devel
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel
BuildRequires:  vulkan-utility-libraries-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)

%description
Vulkan validation layers

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/vulkan-sdk-1.4.341.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7f521490495e43561f70fe8b6317fd5cc13d4083413f1abf891f50cbabe12238" || { echo "oreon: Source0 SHA256 mismatch for vulkan-sdk-1.4.341.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n Vulkan-ValidationLayers-vulkan-sdk-%{version}


%build
# Decrease debuginfo verbosity to reduce memory consumption even more
%ifarch %{ix86}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%global optflags %(echo %{optflags} | sed 's/-O2 /-O1 /')
%endif

%cmake -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_WERROR=OFF \
       -DGLSLANG_INSTALL_DIR=%{_prefix} \
       -DBUILD_LAYER_SUPPORT_FILES:BOOL=ON \
       -DUSE_ROBIN_HOOD_HASHING:BOOL=OFF \
       -DSPIRV_HEADERS_INSTALL_DIR=%{_prefix} \
       -DVULKAN_HEADERS_INSTALL_DIR=%{_prefix} \
       -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_datadir}/vulkan/explicit_layer.d/*.json
%{_libdir}/libVkLayer_*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.341.0-1
- Prepare for Oreon 11 (RP1)
