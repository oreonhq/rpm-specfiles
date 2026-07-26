%global source0_hash none

%global __cmake_in_source_build 1
#global rctag rc1

%global __global_ldflags %(echo "%{__global_ldflags} -lX11")

Name:           supertuxkart
Version:        1.5
Release:        2%{?dist}
Summary:        Kids 3D go-kart racing game featuring Tux
# Font licensing
# [unbundled] GNU FreeFont - GPLv3
# wqyMicroHei - GPLv3 with exception and ASL 2.0
# Noto Naskh Arabic UI - ASL 2.0
# [unbundled] Cantarell - SIL 1.1 (OFL)
# SigmarOne - SIL 1.1 (OFL)
License:        GPL-2.0-or-later AND GPL-3.0-only AND CC-BY-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND OFL-1.1 AND Apache-2.0 AND Zlib
URL:            https://supertuxkart.net/Main_Page
Source0:        https://github.com/%{name}/stk-code/releases/download/%{version}/SuperTuxKart-%{version}%{?rctag:-%{rctag}}-src.tar.gz
Source1:        %{name}.6
Source2:        supertuxkart-0.7.3-license-clarification.txt
Patch0:         defaultgpu.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires:  git-core
BuildRequires:  cmake
# For fonts rpm macro
BuildRequires:  fontpackages-devel
BuildRequires:  freetype-devel
BuildRequires:  libvorbis-devel freeglut-devel desktop-file-utils
BuildRequires:  openal-soft-devel freealut-devel >= 1.1.0-10 libtool
BuildRequires:  libcurl-devel fribidi-devel
BuildRequires:  pkgconfig(libenet)
BuildRequires:  wiiuse-devel bluez-libs-devel
BuildRequires:  libpng-devel libjpeg-turbo-devel
BuildRequires:  libXrandr-devel
BuildRequires:  angelscript-devel
BuildRequires:  pkgconfig(glew)
BuildRequires:  openssl-devel
BuildRequires:  libsquish-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  wayland-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  SDL2-devel
BuildRequires:  libgamerzilla-devel
BuildRequires:  libshaderc-devel
Requires:       hicolor-icon-theme opengl-games-utils
Requires:       %{name}-data = %{version}

# Bundled bullet with their patch
Provides:       bundled(bullet) = 2.87
Provides:       bundled(libtinygettext) = 0.1.0

%description
3D go-kart racing game for kids with several famous OpenSource mascots
participating. Race as Tux against 3 computer players in many different fun
race courses (Standard race track, Dessert, Mathclass, etc). Full information
on how to add your own race courses is included. During the race you can pick
up powerups such as: (homing) missiles, magnets and portable zippers.

%package data
Summary:        %{summary}
Requires:       gnu-free-sans-fonts
Requires:       abattis-cantarell-fonts
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
This package contains the data files for SuperTuxKart.

%prep
%autosetup -n SuperTuxKart-%{version}%{?rctag:-%{rctag}}-src -p1
cp -p %{SOURCE2} .
# Delete bundled libs
#rm -rf lib/enet lib/wiiuse lib/angelscript lib/glew
#sed -i -e '/setAnimationStrength/s/^/\/\//' src/karts/kart_model.cpp
mkdir build

%build
pushd build
  %cmake ../ -DUSE_SYSTEM_ANGELSCRIPT=ON -DBUILD_RECORDER=FALSE -DCMAKE_POLICY_VERSION_MINIMUM=3.5
  %cmake_build
popd

%install
pushd build
  %cmake_install
popd

# Remove a too large icon that goes outside of hicolor-icon-theme spec and breaks flatpak builds
rm %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/supertuxkart.png

ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper
ln -sf %{_fontbasedir}/abattis-cantarell-fonts/Cantarell-Regular.otf %{buildroot}%{_datadir}/%{name}/Cantarell-Regular.otf
ln -sf %{_fontbasedir}/abattis-cantarell-fonts/Cantarell-Bold.otf %{buildroot}%{_datadir}/%{name}/Cantarell-Bold.otf
ln -sf %{_fontbasedir}/gnu-free/FreeSans.ttf %{buildroot}%{_datadir}/%{name}/FreeSans.ttf
ln -sf %{_fontbasedir}/gnu-free/FreeSansBold.ttf %{buildroot}%{_datadir}/%{name}/FreeSansBold.ttf

# add the manpage (courtesy of Debian)
mkdir -p %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop

%files
%license COPYING supertuxkart-0.7.3-license-clarification.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{name}*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/net.supertuxkart.SuperTuxKart.metainfo.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%exclude %{_includedir}/wiiuse.h
%exclude %{_libdir}/libwiiuse.a

%files data
%{_datadir}/%{name}/

%changelog
%autochangelog
