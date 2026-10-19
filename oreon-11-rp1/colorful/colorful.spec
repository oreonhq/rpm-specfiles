%global source0_hash dc93bf023ddff8c2449c74a17949956794592ec48797249a7f824a61d74f4c28
Name:          colorful
%global rtld pl.suve.colorful
Version:       2.2
Release:        1%{?dist}
Summary:        Side-view shooter game
License:       GPL-3.0-only AND (MPL-2.0 OR Zlib)
URL:           https://svgames.pl
Source0:        https://github.com/suve/LD25/releases/download/release-%{version}/colorful-%{version}-source.zip
Requires:      colorful-data = %{version}-%{release}
Requires:      hicolor-icon-theme
ExclusiveArch:  %{fpc_arches}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  glibc-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  optipng
BuildRequires:  vorbis-tools
# /oreon:deps
%description
Colorful is a simple side-view shooter game, where the protagonist 
travels a maze of caves and corridors in order to collect color artifacts.

%package data
Summary:       Game data for Colorful
License:       zlib-acknowledgement
BuildArch:     noarch
%description data
Data files (graphics, maps, sounds) required to play Colorful.

%prep
%global oreon_srcdir %{name}-%{version}-source
%oreon_prep
%build 

./configure.sh --assets=systemwide --flags="-g -gl -gw" --prefix=%{_prefix} --strip=false
%make_build
%install
%make_install
%oreon_autofiles colorful-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rtld}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n colorful-data -f %{oreon_filedir}/colorful-data.list

%changelog

%autochangelog
