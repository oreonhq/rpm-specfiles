%global source0_hash 7b1dde2f34f1427eea96058b93478f07d63f7a42981847d4f884b40b9340758c

Name:           vulkan-validation-layers
Version:        1.4.363
Release:        %autorelease
Summary:        Vulkan validation layers

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source0: https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/vulkan-sdk-1.4.363.tar.gz#/Vulkan-ValidationLayers-sdk-1.4.363.tar.gz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
