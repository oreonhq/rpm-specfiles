%global source0_hash none

%global         _tarname SuperTux-v%{version}-Source

Name:           supertux
Version:        0.6.3
Release:        18%{?dist}
Summary:        Jump'n run like game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.supertux.org
Source0:        https://github.com/SuperTux/%{name}/releases/download/v%{version}/%{_tarname}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2056887
Patch0:         supertux-0.6.3-build-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2082179
Patch1:         supertux-0.6.3-squirrel-CVE-2022-30292.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1833368
ExcludeArch:    s390x

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  sed
BuildRequires:  pkgconfig(raqm)
BuildRequires:  pkgconfig(sdl2) >= 2.0.1
BuildRequires:  pkgconfig(SDL2_image) >= 2.0.0
BuildRequires:  boost-devel
BuildRequires:  freetype-devel
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  libcurl-devel
BuildRequires:  libGLU-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  physfs-devel
BuildRequires:  zlib-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
Requires:       hicolor-icon-theme

# Bundled version of squirrel 3 (only version 2 in Fedora).
Provides:       bundled(squirrel) = 3.1
# Bundled (and forked) version of tinygettext.
Provides:       bundled(tinygettext) = 0.1.20160606git

%description
SuperTux is a jump'n run like game, Run and jump through multiple worlds,
fighting off enemies by jumping on them or bumping them from below.
Grabbing power-ups and other stuff on the way.

%prep
%autosetup -p1 -n %{_tarname}

%build
%cmake -DINSTALL_SUBDIR_SHARE=share/supertux2 -DINSTALL_SUBDIR_BIN=bin \
    -DENABLE_BOOST_STATIC_LIBS=OFF
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_docdir}/supertux2

# Icon stuff
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/pixmaps/supertux.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/supertux2.png
rm %{buildroot}%{_datadir}/pixmaps/supertux.xpm

install -Dpm 644 man/man6/supertux2.6 %{buildroot}%{_mandir}/man6/supertux2.6

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/supertux2.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/supertux2.desktop

%files
%doc README.md NEWS.md
%license LICENSE.txt
%{_bindir}/supertux2
%{_datadir}/supertux2
%{_datadir}/applications/supertux2.desktop
%{_datadir}/icons/hicolor/48x48/apps/supertux2.png
%{_datadir}/icons/hicolor/scalable/apps/supertux2.svg
%{_datadir}/metainfo/supertux2.appdata.xml
%{_mandir}/man6/supertux2.6*

%changelog
%autochangelog
