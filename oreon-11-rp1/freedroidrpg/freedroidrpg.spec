%global source0_hash 7995b70b594248ea14d1b4ef595397a60183031c99163b01c1a8a70ccef3bbcf
%global short_version 1.0
Name:           freedroidrpg
Version:        %{short_version}
Release:        1%{?dist}
Summary:        Role playing game with Freedroid theme and Tux as the hero
License:        GPL-2.0-or-later
URL:            http://freedroid.sourceforge.net/
Source0:        http://ftp.osuosl.org/pub/freedroid/freedroidRPG-%{version}/freedroidRPG-%{version}.tar.gz
Requires:       freedroidrpg-data = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glew-devel
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
%description
The Freedroid RPG is an extension/modification of the classical
freedroid engine into a role playing game.

%package data
Summary:        Data files for the freedroidrpg game
BuildArch:      noarch
Requires:       freedroidrpg = %{version}-%{release}
%description data
Data files for the freedroidrpg game.

%prep

%setup -q
rm -f lua/*.a
rm -f lua/*.o

# Update the timestamp to avoid unnecessarily running configure
touch -r configure.ac aclocal.m4

%build

autoreconf -fi
export CPPFLAGS="$CPPFLAGS -fcommon -fPIE"
%configure --disable-dependency-tracking
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 644 data/graphics/FreedroidRPG.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/freedroidrpg.png
find $RPM_BUILD_ROOT%{_datadir}/%{name} -type f -exec chmod -x "{}" \;
%find_lang freedroidrpg
%find_lang freedroidrpg-data
%find_lang freedroidrpg-dialogs
cat freedroidrpg-data.lang >> freedroidrpg.lang
cat freedroidrpg-dialogs.lang >> freedroidrpg.lang
rm -f freedroidrpg-data.lang
rm -f freedroidrpg-dialogs.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n freedroidrpg-data -f %{oreon_filedir}/freedroidrpg-data.list

%changelog

%autochangelog
