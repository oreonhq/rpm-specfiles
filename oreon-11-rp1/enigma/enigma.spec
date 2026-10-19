%global source0_hash none
%global forgeurl https://github.com/Enigma-Game/Enigma
%global version0 1.30
%global commit ab9967a7c7440ce5d3908c8b6eb63cb5a22cfef1
%forgemeta
Name:           enigma
Version:        %forgeversion
Release:        1%{?dist}
Summary:        Game where you control a marble with the mouse
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/enigma/
Source0:        %{forgeurl}/archive/%{commit}/Enigma-%{commit}.tar.gz
Patch1:         0001-etc-enigma.desktop-use-standard-specified-Categories.patch
Requires:       %{name}-data = %{version}-%{release}
%global fonts font(dejavusans)
Requires:       %{fonts}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  font(dejavusans)
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libenet)
BuildRequires:  texi2html
BuildRequires:  xerces-c-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%package data
Summary:        Data for Enigma game
License:        GPL-2.0-or-later
BuildArch:      noarch
%description data
Data files (levels, graphics, sound, music) and documentation for Enigma.

%prep

%forgeautosetup -p1
rm -r attic/ dlls/ lib-src/enet/*

%build

aclocal -I m4 && autoheader && automake --add-missing --foreign --copy && autoconf
%configure --enable-optimize --with-system-enet
%make_build
%install
%make_install
ln -f -s $(fc-match -f "%{file}" "dejavusans:condensed") \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/DejaVuSansCondensed.ttf
ln -f -s $(fc-match -f "%{file}" "dejavusans") \
desktop-file-install \
  --remove-key Version \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications            \
  $RPM_BUILD_ROOT%{_datadir}/applications/enigma.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/enigma.appdata.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n enigma-data -f %{oreon_filedir}/enigma-data.list

%changelog

%autochangelog
