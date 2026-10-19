%global source0_hash 71a83b8c23aa0b6d7ad749c9184537f6182e7a66a57ddb44dd74c605dbefba92
%undefine _strict_symbol_defs_build
%global codate 20250123
%global commit0 2bf2ca7f1623db7ad7840a4dd626444d11830815
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
ExcludeArch:    s390x
Name:           vkmark
Version:        2025.01
Release:        1%{?dist}
Summary:        Vulkan benchmarking suite
License:        LGPL-2.1-or-later
URL:            https://github.com/vkmark/vkmark
Source0:        https://github.com/%{name}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz
# oreon:deps
BuildRequires:  assimp-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libxcb-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  meson
BuildRequires:  vulkan-loader-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xcb-util-wm-devel
# /oreon:deps
%description
vkmark is an extensible Vulkan benchmarking suite with targeted,
configurable scenes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

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
