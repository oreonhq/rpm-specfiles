%global source0_hash 99775601eae78e2c626bca76a6e9359491e13685541e36bee0d3207f81152e5e
Name:		megaglest-data
Version:	3.13.0
Release:        1%{?dist}
Summary:        Mega Glest data files
License:	LicenseRef-Callaway-CC-BY-SA
Url:		http://megaglest.org/
Source0:        https://github.com/MegaGlest/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
Obsoletes:	glest-data <= 3.2.2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

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
rm %{buildroot}/%{_datadir}/menu/megaglest
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
