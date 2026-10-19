%global source0_hash 4c7a32cc0cda25e6386adfc7d665a544318359ef8f8df701d678a2c1a1946fa5
%global forgeurl  https://gitlab.freedesktop.org/monado/utilities/vulkan-layers
%global commit    ae43cdcbd25c56e3481bbc8a0ce2bfcebba9f7c2
%global date      20240221
%forgemeta
Name:           monado-vulkan-layers
Version:        0.9.0
Release:        1%{?dist}
Summary:        Optional Vulkan Layers for Monado
License:        BSL-1.0 AND CC0-1.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{commit}/vulkan-layers-%{commit}.tar.bz2
Requires:       vulkan-loader
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vulkan)
# /oreon:deps
%description
Vulkan layers to support additional APIs via Monado.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}/%{name}/layer \
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
