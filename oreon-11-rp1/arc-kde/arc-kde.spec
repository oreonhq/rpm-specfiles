%global source0_hash bb4f547df20fc43fc19315cd0c96a447068abdc4095e7ae8b654a813e3422e93
Name:           arc-kde
Version:        20220908
Release:        1%{?dist}
Summary:        Port of the popular GTK theme Arc for the Plasma 5 desktop
License:        GPL-3.0-only AND CC-BY-SA-4.0
URL:            https://github.com/PapirusDevelopmentTeam/arc-kde
Source0:        https://github.com/PapirusDevelopmentTeam/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         arc-kde-plasma-6-support.patch
BuildArch:      noarch
Recommends:     %{name}-kvantum
Recommends:     %{name}-decorations
Recommends:     %{name}-konsole
Recommends:     %{name}-konversation
Recommends:     %{name}-wallpapers
Recommends:     %{name}-yakuake
Recommends:     papirus-icon-theme
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

In this package you'll find:

 - Aurorae Themes
 - Konsole Color Schemes
 - Konversation Themes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Settings
 - Wallpapers
 - Yakuake Skins
 - Extra tools

%package kvantum
Summary:    Arc-KDE Kvantum theme
License:    GPL-3.0-only
BuildArch:  noarch
Requires:   kvantum
%description kvantum
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the ArcDark ard ArcDarker Kvantum theme.

%package decorations
Summary:    Arc-KDE Aurorae theme
License:    GPL-3.0-only
BuildArch:  noarch
%description decorations
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Aurorae window decorations.

%package konsole
Summary:    Arc-KDE Konsole theme
License:    GPL-3.0-only
BuildArch:  noarch
%description konsole
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the ArcDark Konsole theme.

%package konversation
Summary:    Arc-KDE Konversation theme
License:    GPL-3.0-only
BuildArch:  noarch
%description konversation
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Konversation theme.

%package wallpapers
Summary:    Arc-KDE wallpapers
License:    CC-BY-SA-4.0
BuildArch:  noarch
%description wallpapers
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Arc wallpapers.

%package yakuake
Summary:    Arc-KDE Yakuake theme
License:    GPL-3.0-only
BuildArch:  noarch
%description yakuake
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Yakuake theme.

%prep

%autosetup -p1

cp wallpapers/Arc-Dark/LICENSE LICENSE-wallpapers

%build

%install
%make_install
%oreon_autofiles arc-kde-kvantum usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles arc-kde-decorations usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles arc-kde-konsole usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles arc-kde-konversation usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles arc-kde-wallpapers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles arc-kde-yakuake usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n arc-kde-kvantum -f %{oreon_filedir}/arc-kde-kvantum.list
%files -n arc-kde-decorations -f %{oreon_filedir}/arc-kde-decorations.list
%files -n arc-kde-konsole -f %{oreon_filedir}/arc-kde-konsole.list
%files -n arc-kde-konversation -f %{oreon_filedir}/arc-kde-konversation.list
%files -n arc-kde-wallpapers -f %{oreon_filedir}/arc-kde-wallpapers.list
%files -n arc-kde-yakuake -f %{oreon_filedir}/arc-kde-yakuake.list

%changelog

%autochangelog
