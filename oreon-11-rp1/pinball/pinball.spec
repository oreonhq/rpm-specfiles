%global source0_hash c5b7a3992fd681c0d9a907461c2c68a8d868e9e15178534529ce7b9366698542
%global __brp_remove_la_files %nil
Name:           pinball
Version:        0.3.4
Release:        21%{?dist}
Summary:        Emilia 3D Pinball Game
License: GPL-2.0-or-later AND FSFAP AND LGPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            http://pinball.sourceforge.net
Source0:        https://github.com/sergiomb2/pinball/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         6.patch
Requires:   hicolor-icon-theme
Requires:   opengl-games-utils
Requires:   timidity++-patches
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
# /oreon:deps
%description
The Emilia Pinball project is an open source pinball simulator for linux
and other unix systems. The current release features a number of tables:
tux, professor, professor2, gnu and hurd and is very addictive.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains files for development with %{name}.
May be used in pinball-pinedit.

%prep

%setup -q

%patch -P 0 -p1

sed -i 's/Exec=pinball/Exec=pinball-wrapper/' pinball.desktop
./bootstrap

%build

%configure --disable-static
%make_build
%install
%make_install
%find_lang %{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libModuleTest.*
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --set-key='Keywords' --set-value='Game;Arcade;Pinball;' \
  pinball.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pinball.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 pinball.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pinball-devel -f %{oreon_filedir}/pinball-devel.list

%changelog

%autochangelog
