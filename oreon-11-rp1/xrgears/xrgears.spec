%global source0_hash none

%global forgeurl  https://gitlab.freedesktop.org/monado/demos/xrgears
# Upstream tag request: https://gitlab.freedesktop.org/monado/demos/xrgears/-/issues/16
%global commit    6376389139a11eec16138148e17073bbe96f137d
%global date      20231207
%forgemeta

Name:           xrgears
Version:        1.0.1
Release:        %autorelease
Summary:        OpenXR VR demo using Vulkan for rendering

License:        MIT AND Apache-2.0 AND BSL-1.0
URL:            %{forgeurl}
Source0:        %{forgesource}

ExcludeArch:    %{ix86}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  xxd

# src/ktx_stream.{c,h} Apache-2.0
# src/ktx_texture.{c,h} Apache-2.0
Provides: bundled(KTX-Software)

%description
xrgears is an OpenXR VR demo using Vulkan for rendering.

%prep
%forgeautosetup -p1

%build
# W: no-manual-page-for-binary xrgears
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/xrgears

%changelog
%autochangelog
