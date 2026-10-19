%global source0_hash 443c2db1b9307ff80c7d3bca5b0ca9c69d669ac2bc8aa6f451d028e809bc433d
%global gettext_version                         0.19.6
%global gnome_desktop_version                   44.0
%global glib2_version                           2.68.0
%global gtk4_version                            3.24.27
%global mutter_version                          50~beta
%global gsettings_desktop_schemas_version       40~rc
%global ibus_version                            1.5.24
%global gnome_settings_daemon_version           40~rc
%bcond x11 0
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-kiosk
Version:        51.0
Release:        1%{?dist}
Summary:        Window management and application launching for GNOME
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-kiosk
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
%if %{with x11}
Provides:       firstboot(windowmanager) = %{name}
%endif
Requires:       gnome-settings-daemon%{?_isa} >= %{gnome_settings_daemon_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Recommends:     xorg-x11-server-Xwayland
# oreon:deps
BuildRequires:  dconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libmutter-18)
BuildRequires:  python3-devel
# /oreon:deps
%description
GNOME Kiosk provides a desktop enviroment suitable for fixed purpose, or
single application deployments like wall displays and point-of-sale systems.

%package search-appliance
Summary:        Example search application application that uses GNOME Kiosk
Requires:       %{name} = %{version}-%{release}
Requires:       firefox
Requires:       gnome-session
BuildArch:      noarch
%description search-appliance
This package provides a full screen firefox window pointed to google.

%package script-session
Summary:        Basic session used for running kiosk application from shell script
Requires:       %{name} = %{version}-%{release}
Recommends:     gedit
Requires:       gnome-session
BuildArch:      noarch
%description script-session
This package generates a shell script and the necessary scaffolding to start that shell script within a kiosk session.

%package a11y
Summary:        Accessibility panel for gnome-kiosk
Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject
Requires:       gtk4
BuildRequires:  python3-devel
BuildArch:      noarch
%description a11y
Accessibility panel for gnome-kiosk to control accessibility features.

%package notification-daemon
Summary:        A basic notification daemon for gnome-kiosk
Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject
Requires:       gtk4
BuildRequires:  python3-devel
BuildArch:      noarch
%description notification-daemon
A basic notification daemon for gnome-kiosk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -S git -n %{name}-%{tarball_version}

%build

%meson -Daccessibility-panel=true -Dnotification-daemon=true
%meson_build
%install
%meson_install
%if !%{with x11}
rm -rf %{buildroot}%{_datadir}/xsessions
rm -f %{buildroot}%{_userunitdir}/org.gnome.Kiosk@x11.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Kiosk.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Kiosk.SearchApp.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnome-kiosk-search-appliance -f %{oreon_filedir}/gnome-kiosk-search-appliance.list
%files -n gnome-kiosk-script-session -f %{oreon_filedir}/gnome-kiosk-script-session.list
%files -n gnome-kiosk-a11y -f %{oreon_filedir}/gnome-kiosk-a11y.list
%files -n gnome-kiosk-notification-daemon -f %{oreon_filedir}/gnome-kiosk-notification-daemon.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
