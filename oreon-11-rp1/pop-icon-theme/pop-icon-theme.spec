%global source0_hash none

Name:           pop-icon-theme
Version:        3.5.0
Release:        %autorelease
Summary:        Pop Icons
License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/icon-theme
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  meson

Requires:       gnome-icon-theme

%description
Pop_Icons is the icon theme for Pop!_OS.  It uses a semi-flat design with
raised 3D motifs to help give depth to icons.  Pop_Icons take inspiration from
the Adwaita GNOME Icons.

%prep
%autosetup -n icon-theme-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING LICENSE
%{_datadir}/icons/Pop

%changelog
%autochangelog
