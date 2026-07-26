%global source0_hash none

#global extra_version -2

Name:           cdogs-sdl
Version:        0.7.3
Release:        17%{?dist}
Summary:        C-Dogs is an arcade shoot-em-up
# The game-engine is GPLv2+
# The game art is CC
# Automatically converted from old format: GPLv2+ and CC-BY and CC-BY-SA and CC0 - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0
URL:            http://cxong.github.io/cdogs-sdl/
Source0:        https://github.com/cxong/cdogs-sdl/archive/%{version}%{?extra_version}.tar.gz#/%{name}-%{version}%{?extra_version}.tar.gz
Patch0:         cdogs-sdl-0.5.8-cmake.patch
Patch1:         cdogs-sdl-0.7.3-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  cmake SDL2_mixer-devel SDL2_image-devel libGL-devel
BuildRequires:  ncurses-devel physfs-devel enet-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme
Obsoletes:      cdogs-data < 0.5
Provides:       cdogs-data = %{version}-%{release}

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

%check
desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/io.github.cxong.%{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml

%files
%doc doc/AUTHORS doc/CREDITS doc/original_readme.txt doc/README_DATA.md
%license doc/COPYING.BSD doc/COPYING.GPL doc/COPYING.MJSON.txt doc/COPYING.xgetopt.txt doc/COPYING.yajl.txt doc/LICENSE.nanopb.txt doc/license.rlutil.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml
%{_datadir}/applications/io.github.cxong.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.cxong.%{name}.png

%changelog
%autochangelog
