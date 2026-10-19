%global source0_hash 2731ffbf22e6fa4afa321fd677d3981c9a3851b9bca1e65d2439e6f3f6b735bf
Name:           materia-kde
Version:        20220823
Release:        1%{?dist}
Summary:        Port of the popular GTK theme Materia for the Plasma 5 desktop
License:        GPL-3.0-only
URL:            https://github.com/PapirusDevelopmentTeam/materia-kde
Source0:        https://github.com/PapirusDevelopmentTeam/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Recommends:     %{name}-kvantum
Recommends:     %{name}-decorations
Recommends:     %{name}-konsole
Recommends:     %{name}-wallpapers
Recommends:     %{name}-yakuake
Recommends:     papirus-icon-theme
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

In this package you'll find:

 - Aurorae Themes
 - Konsole Color Schemes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Settings
 - Wallpapers
 - Yakuake Skins

%package decorations
Summary:    Materia-KDE Aurorae theme
%description decorations
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Aurorae window decorations.

%package konsole
Summary:    Materia-KDE Konsole theme
%description konsole
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark Konsole theme.

%package kvantum
Summary:    Materia-KDE Kvantum theme
Requires:   kvantum
%description kvantum
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark and MateriaLight Kvantum theme.

%package sddm
Summary:    Materia-KDE SDDM theme
Requires:   sddm
%description sddm
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark and Materia SDDM theme.

%package wallpapers
Summary:    Materia-KDE wallpapers
%description wallpapers
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Materia wallpapers.

%package yakuake
Summary:    Materia-KDE Yakuake theme
%description yakuake
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Yakuake theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n materia-kde-decorations -f %{oreon_filedir}/materia-kde-decorations.list
%files -n materia-kde-konsole -f %{oreon_filedir}/materia-kde-konsole.list
%files -n materia-kde-kvantum -f %{oreon_filedir}/materia-kde-kvantum.list
%files -n materia-kde-sddm -f %{oreon_filedir}/materia-kde-sddm.list
%files -n materia-kde-wallpapers -f %{oreon_filedir}/materia-kde-wallpapers.list
%files -n materia-kde-yakuake -f %{oreon_filedir}/materia-kde-yakuake.list

%changelog

%autochangelog
