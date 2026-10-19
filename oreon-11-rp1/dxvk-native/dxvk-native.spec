%global source1_hash 862ee0d5fed8c7c8dff87e7b0dbc0985e6ab5f71901785a2dec656457d8c665b
%global source0_hash ef4944134f6c39d0937f265391db2d08bca33cd3a2f0ee9133e1eb55f1cc657c
%global dxbc_spirv_commit 31b74bfb99c39ddaaaf6490cfce30046c38913e4
Name:           dxvk-native
Version:        3.1.1
Release:        1%{?dist}
Summary:        Vulkan-based D3D8~D3D11 implementation for Linux
SourceLicense:  Zlib and MIT
License:        Zlib
URL:            https://github.com/doitsujin/dxvk
Source0:        https://github.com/doitsujin/dxvk/archive/v%{version}/dxvk-%{version}.tar.gz
Source1:        https://github.com/doitsujin/dxbc-spirv/archive/%{dxbc_spirv_commit}/dxbc-spirv-%{dxbc_spirv_commit}.tar.gz
Patch0101:      https://github.com/doitsujin/dxvk/pull/5491.patch
Patch0102:      https://github.com/doitsujin/dxvk/pull/5494.patch
Patch1001:      dxvk-libdisplay-info-0.3.0.patch
Requires:       vulkan-loader%{?_isa}
Requires:       SDL3%{?_isa}
Requires:       SDL2%{?_isa}
Requires:       glfw%{?_isa}
ExclusiveArch:  %{ix86} %{x86_64}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  meson
BuildRequires:  mingw64-headers
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  spirv-headers-devel
BuildRequires:  vulkan-loader-devel
# /oreon:deps
%description
DXVK Native is a port of DXVK to Linux which allows it
to be used natively without Wine.

This is primarily useful for game and application ports
to either avoid having to write another rendering backend,
or to help with port bringup during development.

%package devel
Summary:        Development files used to build applications using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       SDL3-devel%{?_isa}
Requires:       SDL2-devel%{?_isa}
Requires:       glfw-devel%{?_isa}
Requires:       vulkan-loader-devel%{?_isa}
%description devel
This package provides the development libraries and other
files for building applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dxvk-%{version} -p1

mkdir -p subprojects/dxbc-spirv
# Prepare subprojects/dxbc-spirv
tar -xf %{SOURCE1} -C subprojects/dxbc-spirv --strip-components=1

# Copy the MinGW DirectX headers to include/native/directx/
cp %{mingw64_includedir}/d3d10_1.h include/native/directx
cp %{mingw64_includedir}/d3d10_1shader.h include/native/directx
cp %{mingw64_includedir}/d3d10effect.h include/native/directx
cp %{mingw64_includedir}/d3d10.h include/native/directx
cp %{mingw64_includedir}/d3d10misc.h include/native/directx
cp %{mingw64_includedir}/d3d10sdklayers.h include/native/directx
cp %{mingw64_includedir}/d3d10shader.h include/native/directx
cp %{mingw64_includedir}/d3d11_1.h include/native/directx
cp %{mingw64_includedir}/d3d11_2.h include/native/directx
cp %{mingw64_includedir}/d3d11_3.h include/native/directx
cp %{mingw64_includedir}/d3d11_4.h include/native/directx
cp %{mingw64_includedir}/d3d11.h include/native/directx
cp %{mingw64_includedir}/d3d11on12.h include/native/directx
cp %{mingw64_includedir}/d3d11sdklayers.h include/native/directx
cp %{mingw64_includedir}/d3d11shader.h include/native/directx
cp %{mingw64_includedir}/d3d12.h include/native/directx
cp %{mingw64_includedir}/d3d12sdklayers.h include/native/directx
cp %{mingw64_includedir}/d3d12shader.h include/native/directx
cp %{mingw64_includedir}/d3d8caps.h include/native/directx
cp %{mingw64_includedir}/d3d8.h include/native/directx
cp %{mingw64_includedir}/d3d8types.h include/native/directx
cp %{mingw64_includedir}/d3d9caps.h include/native/directx
cp %{mingw64_includedir}/d3d9.h include/native/directx
cp %{mingw64_includedir}/d3d9types.h include/native/directx
cp %{mingw64_includedir}/d3dcaps.h include/native/directx
cp %{mingw64_includedir}/d3dcommon.h include/native/directx
cp %{mingw64_includedir}/d3dcompiler.h include/native/directx
cp %{mingw64_includedir}/d3d.h include/native/directx
cp %{mingw64_includedir}/d3dhal.h include/native/directx
cp %{mingw64_includedir}/d3drmdef.h include/native/directx
cp %{mingw64_includedir}/d3drm.h include/native/directx
cp %{mingw64_includedir}/d3drmobj.h include/native/directx
cp %{mingw64_includedir}/d3dtypes.h include/native/directx
cp %{mingw64_includedir}/d3dvec.inl include/native/directx
cp %{mingw64_includedir}/d3dx9anim.h include/native/directx
cp %{mingw64_includedir}/d3dx9core.h include/native/directx
cp %{mingw64_includedir}/d3dx9effect.h include/native/directx
cp %{mingw64_includedir}/d3dx9.h include/native/directx
cp %{mingw64_includedir}/d3dx9math.h include/native/directx
cp %{mingw64_includedir}/d3dx9math.inl include/native/directx
cp %{mingw64_includedir}/d3dx9mesh.h include/native/directx
cp %{mingw64_includedir}/d3dx9shader.h include/native/directx
cp %{mingw64_includedir}/d3dx9shape.h include/native/directx
cp %{mingw64_includedir}/d3dx9tex.h include/native/directx
cp %{mingw64_includedir}/d3dx9xof.h include/native/directx
cp %{mingw64_includedir}/dxdiag.h include/native/directx
cp %{mingw64_includedir}/dxerr8.h include/native/directx
cp %{mingw64_includedir}/dxerr9.h include/native/directx
cp %{mingw64_includedir}/dxfile.h include/native/directx
cp %{mingw64_includedir}/dxgi1_2.h include/native/directx
cp %{mingw64_includedir}/dxgi1_3.h include/native/directx
cp %{mingw64_includedir}/dxgi1_4.h include/native/directx
cp %{mingw64_includedir}/dxgi1_5.h include/native/directx
cp %{mingw64_includedir}/dxgi1_6.h include/native/directx
cp %{mingw64_includedir}/dxgicommon.h include/native/directx
cp %{mingw64_includedir}/dxgidebug.h include/native/directx
cp %{mingw64_includedir}/dxgiformat.h include/native/directx
cp %{mingw64_includedir}/dxgi.h include/native/directx
cp %{mingw64_includedir}/dxgitype.h include/native/directx
cp %{mingw64_includedir}/dxtmpl.h include/native/directx
cp %{mingw64_includedir}/dxva2api.h include/native/directx
cp %{mingw64_includedir}/dxva.h include/native/directx
cp %{mingw64_includedir}/dxvahd.h include/native/directx
cp %{mingw64_includedir}/_mingw_unicode.h include/native/directx

%build

%meson -Dbuild_id=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dxvk-native-devel -f %{oreon_filedir}/dxvk-native-devel.list

%changelog

%autochangelog
