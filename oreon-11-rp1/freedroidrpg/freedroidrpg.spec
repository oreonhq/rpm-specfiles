%global source0_hash none

%global short_version 1.0
Name:           freedroidrpg
Version:        %{short_version}
Release:        10%{?dist}
Summary:        Role playing game with Freedroid theme and Tux as the hero

License:        GPL-2.0-or-later
URL:            http://freedroid.sourceforge.net/
Source0:        http://ftp.osuosl.org/pub/freedroid/freedroidRPG-%{version}/freedroidRPG-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  ImageMagick
BuildRequires:  libvorbis-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libGLU-devel
BuildRequires:  gettext-devel
BuildRequires:  lua-devel
BuildRequires:  glew-devel
BuildRequires:  make
BuildRequires:  autoconf automake

Requires:       freedroidrpg-data = %{version}-%{release}

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
# Fix permissions, remove extra junk.
find $RPM_BUILD_ROOT%{_datadir}/%{name} -type f -exec chmod -x "{}" \;

%find_lang freedroidrpg
%find_lang freedroidrpg-data
%find_lang freedroidrpg-dialogs
cat freedroidrpg-data.lang >> freedroidrpg.lang
cat freedroidrpg-dialogs.lang >> freedroidrpg.lang
rm -f freedroidrpg-data.lang
rm -f freedroidrpg-dialogs.lang

%files -f freedroidrpg.lang
%license COPYING
%doc AUTHORS README* NEWS CONTRIBUTING.md
%{_bindir}/*
%{_datadir}/applications/org.freedroid.freedroidRPG.desktop
%{_metainfodir}/org.freedroid.freedroidRPG.appdata.xml
%{_datadir}/icons/*
%{_mandir}/man6/freedroidRPG.6.*

%files data
%{_datadir}/%{name}

%changelog
%autochangelog
