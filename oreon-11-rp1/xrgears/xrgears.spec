%global source0_hash none
%global forgeurl  https://gitlab.freedesktop.org/monado/demos/xrgears
%global commit    6376389139a11eec16138148e17073bbe96f137d
%global date      20231207
%forgemeta
Name:           xrgears
Version:        1.0.1
Release:        1%{?dist}
Summary:        OpenXR VR demo using Vulkan for rendering
License:        MIT AND Apache-2.0 AND BSL-1.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
ExcludeArch:    %{ix86}
Provides: bundled(KTX-Software)
# oreon:deps
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
# /oreon:deps
%description
xrgears is an OpenXR VR demo using Vulkan for rendering.

%prep

%forgeautosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
