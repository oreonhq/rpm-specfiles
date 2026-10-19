%global source0_hash d64f41549733c4e31c0c35082b52087166039d8f4fbae00aa3dcb999f976ff7f
Name:		sar2
Version:	2.6.0
Release:        1%{?dist}
Summary:        An open source helicopter simulator
License:	GPL-2.0-or-later
URL:		https://github.com/SearchAndRescue2/sar2
Source0:        https://github.com/SearchAndRescue2/sar2/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libvorbis-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openal-soft-devel
BuildRequires:  scons
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
