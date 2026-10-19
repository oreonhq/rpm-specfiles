%global source0_hash 92e73f252e5e9c8a1124623a7d421410ef43c798a4a992955e6eb4f666f5c8a0
Name:           pop-icon-theme
Version:        3.5.1
Release:        1%{?dist}
Summary:        Pop Icons
License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/icon-theme
Source0:        https://github.com/pop-os/icon-theme/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       gnome-icon-theme
# oreon:deps
BuildRequires:  meson
# /oreon:deps
%description
Pop_Icons is the icon theme for Pop!_OS.  It uses a semi-flat design with
raised 3D motifs to help give depth to icons.  Pop_Icons take inspiration from
the Adwaita GNOME Icons.

%prep
%global oreon_srcdir icon-theme-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
