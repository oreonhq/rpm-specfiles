%global source0_hash 33cf8841e4ff4082d80b9248014295bbbea61d14683e86dff100e3ab8f7b27cb
%global __cmake_in_source_build 1
%global __global_ldflags %(echo "%{__global_ldflags} -lX11")
Name:           supertuxkart
Version:        1.5
Release:        2%{?dist}
Summary:        Kids 3D go-kart racing game featuring Tux
License:        GPL-2.0-or-later AND GPL-3.0-only AND CC-BY-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND OFL-1.1 AND Apache-2.0 AND Zlib
URL:            https://supertuxkart.net/Main_Page
Source0:        https://github.com/%{name}/stk-code/releases/download/%{version}/SuperTuxKart-%{version}-src.tar.gz
Source1:        %{name}.6
Source2:        supertuxkart-0.7.3-license-clarification.txt
Patch0:         defaultgpu.patch
Requires:       hicolor-icon-theme opengl-games-utils
Requires:       %{name}-data = %{version}
Provides:       bundled(bullet) = 2.87
Provides:       bundled(libtinygettext) = 0.1.0
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  angelscript-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  harfbuzz-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgamerzilla-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libshaderc-devel
BuildRequires:  libsquish-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  wayland-devel
BuildRequires:  wiiuse-devel
# /oreon:deps
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
rm %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/supertuxkart.png
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper
ln -sf %{_fontbasedir}/abattis-cantarell-fonts/Cantarell-Regular.otf %{buildroot}%{_datadir}/%{name}/Cantarell-Regular.otf
ln -sf %{_fontbasedir}/abattis-cantarell-fonts/Cantarell-Bold.otf %{buildroot}%{_datadir}/%{name}/Cantarell-Bold.otf
ln -sf %{_fontbasedir}/gnu-free/FreeSans.ttf %{buildroot}%{_datadir}/%{name}/FreeSans.ttf
ln -sf %{_fontbasedir}/gnu-free/FreeSansBold.ttf %{buildroot}%{_datadir}/%{name}/FreeSansBold.ttf
mkdir -p %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n supertuxkart-data -f %{oreon_filedir}/supertuxkart-data.list

%changelog

%autochangelog
