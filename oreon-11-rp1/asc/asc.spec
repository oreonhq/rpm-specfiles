%global source0_hash none

Name:           asc
Version:        2.8.0.2
Release:        29%{?dist}
Summary:        Advanced Strategic Command
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.asc-hq.org/
Source0:        http://terdon.asc-hq.org/asc/builds/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         asc-2.8.0.2-gcc-10.patch
Patch1:         asc-2.8.0.2-gcc-11.patch
BuildRequires:  SDL_image-devel SDL_mixer-devel SDL_sound-devel
BuildRequires:  bzip2-devel libjpeg-devel libsigc++20-devel physfs-devel
BuildRequires:  libvorbis-devel libpng-devel libtiff-devel boost-devel
BuildRequires:  freetype-devel expat-devel lua-devel wxGTK-devel libcurl-devel
BuildRequires:  make gcc gcc-c++ libtool desktop-file-utils zip
Requires:       hicolor-icon-theme

%description
ASC is a free, turn based strategy game.

%prep
#bug in upstream tarbal, contains 2.8.0.1 dir instead of 2.8.0.2
%autosetup -p1 -n asc-2.8.0.1
autoreconf -ivf
sed -i 's|$datadir/games/|$datadir/|g' configure
sed -i 's|$(datadir)/games/|$(datadir)/|g' `find -name Makefile.in`
chmod -x source/libs/paragui/include/paragui.h source/unitcostcalculator-pbp.cpp

%build
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++11 -D__EXPORT__="
%configure --enable-genparse --disable-paraguitest
make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 data/icons/program-icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

%files
%doc README AUTHORS
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}*.6.gz

%changelog
%autochangelog
