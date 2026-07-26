%global source0_hash none

%global __cmake_in_source_build 1
%global _legacy_common_support 1
%global _cmake_generator "Unix Makefiles"
%global warsow_libdir %{_prefix}/lib/warsow

%global nodotver 21

Name:           warsow
Version:        2.1.2
Release:        19%{?dist}
Summary:        Fast paced 3D first person shooter

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.warsow.net/
Source0:        http://update.warsow.gg/mirror/warsow_%{nodotver}_sdk.tar.gz
Source1:        warsow.desktop
Source2:        warsow.appdata.xml
# Downstream patch to look for data files and libs installed in our prefix
Patch0:         warsow-paths.patch
# Downstream patch to use our optimization flags
Patch1:         warsow-build.patch

# Warsow is only ported to these architectures
ExclusiveArch:  %{ix86} x86_64 %{arm}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openssl-devel
BuildRequires:  SDL2-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  ImageMagick
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/dos2unix
Requires:       hicolor-icon-theme
Requires:       warsow-data = %{version}

# Filter private libraries from provides
%global __provides_exclude_from ^%{warsow_libdir}/.*\\.so$

%description
Warsow is a fast paced first person shooter consisting of cel-shaded
cartoon-like graphics with dark, flashy and dirty textures. Warsow is based on
the E-novel "Chasseur de bots" ("Bots hunter" in English) by Fabrice Demurger.
Warsow's codebase is built upon Qfusion, an advanced modification of the Quake
II engine.

This package installs the client to play Warsow.

%package server
Summary:        Dedicated server for Warsow
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description server
Warsow is a fast paced first person shooter consisting of cel-shaded
cartoon-like graphics with dark, flashy and dirty textures. Warsow is based on
the E-novel "Chasseur de bots" ("Bots hunter" in English) by Fabrice Demurger.
Warsow's codebase is built upon Qfusion, an advanced modification of the Quake
II engine.

This package installs the standalone server and TV server for Warsow.

%prep
%setup -q -n warsow_%{nodotver}_sdk
%patch -P0 -p1 -b .paths
%patch -P1 -p1 -b .build

# Replace the placeholder that patch0 added with the actual prefix
sed -i -e 's|__PREFIX__|%{_prefix}|g' source/source/qcommon/files.c

# Remove bundled libs
pushd source/libsrcs
rm -rf libcurl libfreetype libjpeg libogg libpng libtheora libvorbis OpenAL-MOB openssl SDL2 zlib
popd

# Convert to utf-8 and Unix line breaks
dos2unix docs/license.txt

%build
mkdir -p source/source/cmake_build
pushd source/source/cmake_build

%cmake \
  -DQFUSION_GAME=Warsow \
  -DUSE_SDL2=YES \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  ..
%cmake_build

popd

%install
pushd source/source/build

# Install executables to bindir
install -Dm 755 warsow.* $RPM_BUILD_ROOT%{_bindir}/warsow
install -Dm 755 wsw_server.* $RPM_BUILD_ROOT%{_bindir}/warsow-server
install -Dm 755 wswtv_server.* $RPM_BUILD_ROOT%{_bindir}/warsow-tv-server

# Install private libraries to a private directory
install -d $RPM_BUILD_ROOT%{warsow_libdir}/libs
install -m 755 libs/*.so $RPM_BUILD_ROOT%{warsow_libdir}/libs/

popd

# Install icons and the desktop file
convert -strip source/icons/warsow256x256.xpm warsow256x256.png
install -D -m 0644 warsow256x256.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps/warsow.png
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/warsow.desktop
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata/warsow.appdata.xml

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/warsow.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/warsow.appdata.xml

%files
%license docs/license.txt
%{_bindir}/warsow
%{_datadir}/icons/hicolor/*/apps/warsow.png
%{_datadir}/appdata/warsow.appdata.xml
%{_datadir}/applications/warsow.desktop
%{warsow_libdir}/

%files server
%{_bindir}/warsow-server
%{_bindir}/warsow-tv-server

%changelog
%autochangelog
