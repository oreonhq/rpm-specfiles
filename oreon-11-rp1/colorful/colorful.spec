%global source0_hash none

Name:          colorful
%global rtld pl.suve.colorful

Version:       2.2
Release:       5%{?dist}
Summary:       Side-view shooter game

# The game itself is GPLv3.
# The source archive also inluces Pascal units for SDL2.
# Said units are dual-licensed: MPLv2 or zlib.
License:       GPL-3.0-only AND (MPL-2.0 OR Zlib)

URL:           https://svgames.pl
Source0:       https://github.com/suve/LD25/releases/download/release-%{version}/colorful-%{version}-source.zip

Requires:      colorful-data = %{version}-%{release}
Requires:      hicolor-icon-theme

# Needed for compilation
BuildRequires: fpc >= 3.0.0
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: optipng
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: vorbis-tools

# Needed to properly build the RPM
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# FPC is not available on all architectures
ExclusiveArch:  %{fpc_arches}

%description
Colorful is a simple side-view shooter game, where the protagonist 
travels a maze of caves and corridors in order to collect color artifacts.

%package data
Summary:       Game data for Colorful
# The game uses separate licenses for code and assets
License:       zlib-acknowledgement
BuildArch:     noarch

%description data
Data files (graphics, maps, sounds) required to play Colorful.

%prep
%autosetup -p1 -n %{name}-%{version}-source

%build 
./configure.sh --assets=systemwide --flags="-g -gl -gw" --prefix=%{_prefix} --strip=false
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rtld}.metainfo.xml

%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_mandir}/*/man6/%{name}.6*
%{_datadir}/applications/%{rtld}.desktop
%{_datadir}/metainfo/%{rtld}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc README.md
%license LICENCE-CODE.txt

%files data
%{_datadir}/suve/
%license LICENCE-ASSETS.txt

%changelog
%autochangelog
