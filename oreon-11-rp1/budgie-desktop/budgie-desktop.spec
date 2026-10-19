%global source2_hash 457b6bd60d99522ca3d202f55381f3d20e90a170f893591eecaf48e4b80dc501
%global source1_hash 3bbc09437f0dc4e1a588aa36fbbcbae59722dd7586b7525aa9c3fbdc538583db
%global source0_hash 5dae4e311bc95ad982b6256265537c2c6e2bcd19dd35efd19bdbb33633516b74
%global glib2_version 2.64
%global gnome_desktop_version 44.4
%global gnome_settings_daemon_version 49
%global gsettings_desktop_schemas_version 49
%global gtk3_version 3.24
%global polkit_version 0.105
%global vala_version 0.56.18
Name:           budgie-desktop
Version:        10.10.3
Release:        1%{?dist}
Summary:        A feature-rich, modern desktop designed to keep out the way of the user
License:        GPL-2.0-or-later AND GPL-2.0-only AND LGPL-2.1-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop
Source0:        https://github.com/BuddiesOfBudgie/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://forge.moderndesktop.dev/BuddiesOfBudgie/keyrings/raw/branch/main/JoshuaStrobl.gpg
ExcludeArch:    %{ix86}
Requires:       budgie-desktop-services
Requires:       budgie-session
Requires:       egl-utils
Requires:       gammastep
Requires:       grim
Requires:       gnome-settings-daemon
Requires:       gsettings-desktop-schemas
Requires:       gnome-keyring-pam
Requires:       hicolor-icon-theme
Requires:       labwc
Requires:       mutter-common
Requires:       network-manager-applet
Requires:       python3-psutil
Requires:       slurp
Requires:       swaybg
Requires:       swayidle
Requires:       switcheroo-control
Requires:       xdg-desktop-portal-gtk
Requires:       xdg-desktop-portal-wlr
Requires:       wlopm
Suggests:       budgie-control-center
Suggests:       budgie-display-configurator
Suggests:       papirus-icon-theme
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Conflicts:      %{name} < 10.6.4-2
Conflicts:      %{name}-devel < 10.6.4-2
Obsoletes:      budgie-screensaver < 5.1.0-9
# oreon:deps
BuildRequires:  budgie-desktop-view
BuildRequires:  desktop-file-utils
BuildRequires:  egl-utils
BuildRequires:  gammastep
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  grim
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  gtk-doc
BuildRequires:  gtklock
BuildRequires:  intltool
BuildRequires:  magpie-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxfce4windowing-0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  sassc
BuildRequires:  slurp
BuildRequires:  swaybg
BuildRequires:  swayidle
BuildRequires:  wlopm
# /oreon:deps
%description
A feature-rich, modern desktop designed to keep out the way of the user.

%package devel
Summary:        Development package for budgie-desktop
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      %{name} < 10.6.4-2
Conflicts:      %{name}-devel < 10.6.4-2
%description devel
Header files, libraries, and other files for developing Budgie Desktop.

%package docs
Summary:        Documentation for budgie-desktop
BuildArch:      noarch
Requires:       gtk-doc
Requires:       %{name} = %{version}-%{release}
%description docs
Documentation for budgie-desktop

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson -Dwith-hibernate=false
%meson_build
%install
%meson_install
chmod +x %{buildroot}/%{_libexecdir}/%{name}/labwc_bridge.py
%find_lang %{name}
%oreon_autofiles budgie-desktop-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles budgie-desktop-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n budgie-desktop-devel -f %{oreon_filedir}/budgie-desktop-devel.list
%files -n budgie-desktop-docs -f %{oreon_filedir}/budgie-desktop-docs.list

%changelog

%autochangelog
