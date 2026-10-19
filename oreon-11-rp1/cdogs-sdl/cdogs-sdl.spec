%global source0_hash 0fde6aaf07db2156e5d4c8e448f0ddb4608ed3b92b89aae1e2c87b20866e451c
Name:           cdogs-sdl
Version:        2.4.0
Release:        1%{?dist}
Summary:        C-Dogs is an arcade shoot-em-up
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0
URL:            http://cxong.github.io/cdogs-sdl/
Source0:        https://github.com/cxong/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cdogs-sdl-0.5.8-cmake.patch
Patch1:         cdogs-sdl-0.7.3-fcommon-fix.patch
Requires:       hicolor-icon-theme
Obsoletes:      cdogs-data < 0.5
Provides:       cdogs-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  enet-devel
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libappstream-glib
BuildRequires:  ncurses-devel
BuildRequires:  physfs-devel
# /oreon:deps
%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilizing the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the “dogfight” death-match mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.

%prep

%autosetup -p1 -n %{name}-%{version}%{?extra_version}
# We use the system enet
rm -r src/cdogs/enet
# Misc. cleanups
sed -i 's/\r//' doc/original_readme.txt
find graphics sounds -name "*.sh" -delete

%build

%cmake -DCDOGS_DATA_DIR=/usr/share/cdogs-sdl/ -DUSE_SHARED_ENET=1
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/io.github.cxong.%{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
