%global source0_hash none

Name:		megaglest-data
Version:	3.13.0
Release:	19%{?dist}
Summary:	Mega Glest data files
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:	LicenseRef-Callaway-CC-BY-SA
Url:		http://megaglest.org/
Source0:        https://github.com/MegaGlest/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
Obsoletes:	glest-data <= 3.2.2

%description
MegaGlest is an entertaining free (freeware and free software) and
open source cross-platform 3D real-time strategy (RTS) game, where
you control the armies of one of seven different factions: Tech,
Magic, Egypt, Indians, Norsemen, Persian or Romans. The game is
setup in one of 17 naturally looking settings, which -like the
unit models- are crafted with great appreciation for detail.
A lot of additional game data can be downloaded from within the
game at no cost.

%prep
%autosetup -n %{name}-%{version}

%build
# TODO: Please submit an issue to upstream (rhbz#2380904)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
mkdir -p %{_vpath_builddir}
%cmake \
  -DMEGAGLEST_ICON_INSTALL_PATH=%{_datadir}/icons
%cmake_build

%install
%cmake_install
rm -fr %{buildroot}/%{_datadir}/megaglest/docs
for image in `ls %{buildroot}/%{_datadir}/megaglest/icons`
do
  [ -e %{buildroot}%{_datadir}/$image ] \
  || ln -sf %{_datadir}/icons/$image %{buildroot}/%{_datadir}/megaglest
done
for file in megaglest megaglest_editor megaglest_g3dviewer
do
  desktop-file-validate %{buildroot}/%{_datadir}/applications/$file.desktop
done

# remove Debian style menu file
rm %{buildroot}/%{_datadir}/menu/megaglest

%files
%doc docs/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/megaglest*.desktop
%{_datadir}/icons/megaglest.*
%dir %{_datadir}/megaglest
%{_datadir}/megaglest/data/
%{_datadir}/megaglest/maps/
%{_datadir}/megaglest/scenarios/
%{_datadir}/megaglest/techs/
%{_datadir}/megaglest/tilesets/
%{_datadir}/megaglest/tutorials/

%changelog
%autochangelog
