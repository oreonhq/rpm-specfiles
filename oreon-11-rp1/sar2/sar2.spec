%global source0_hash none

Name:		sar2
Version:	2.5.0
Release:	14%{?dist}
Summary:	An open source helicopter simulator
# Code is GPLv2+
# Content is either GPLv2+ or Public Domain
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/SearchAndRescue2/sar2
Source0:	https://github.com/SearchAndRescue2/sar2/archive/v%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:	scons, desktop-file-utils
BuildRequires:	libX11-devel, libSM-devel, libXi-devel, libXmu-devel
BuildRequires:	SDL2-devel, SDL2_image-devel, openal-soft-devel, freealut-devel
BuildRequires:	mesa-libGLU-devel, mesa-libGL-devel, libICE-devel
BuildRequires:	libXpm-devel, libvorbis-devel, libXext-devel
BuildRequires:	libXxf86vm-devel

%description
Search and Rescue II is a rescue helicopter simulator for Linux. It features 
several missions in which the player pilots a helicopter in order to rescue 
people in distress. There are several scenarios and helicopter models.

Search and Rescue II has a strong focus on realistic physics and low graphics 
requirements. It is a fork of the game "Search and Rescue" 
(http://searchandrescue.sf.net), originally developed by Wolfpack 
Entertainment.

%prep
%setup -q

%build
scons --optflags="%{optflags}"

%install
# install.sh is pretty dumb.
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/
mkdir -p %{buildroot}%{_datadir}/pixmaps/

cp -ar data/* %{buildroot}%{_datadir}/%{name}/
cp -a man/* %{buildroot}%{_mandir}/man6
cp -a bin/%{name} %{buildroot}%{_bindir}
cp -a extra/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/
cp -a src/icons/SearchAndRescue.xpm %{buildroot}%{_datadir}/pixmaps/
pushd %{buildroot}%{_datadir}/pixmaps/
ln -s ../icons/hicolor/48x48/sar2.xpm sar2.xpm
popd
desktop-file-install --dir=%{buildroot}%{_datadir}/applications extra/%{name}.desktop

%files
%doc AUTHORS CHANGELOG.md HACKING LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/

%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/%{name}.xpm
%{_datadir}/pixmaps/*.xpm
%{_mandir}/man6/*

%changelog
%autochangelog
