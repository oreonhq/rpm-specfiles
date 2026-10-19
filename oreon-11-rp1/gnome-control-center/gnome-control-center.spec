%global source0_hash c8ca5b6a0ae44fd0d64aac5aa3b79a83c2445095b159a9d13d1c9cc172ac4fb9
%global blueprint_compiler_version 0.17
%global gcr_version 4.1.0
%global gnome_online_accounts_version 3.51.0
%global glib2_version 2.76.6
%global gnome_desktop_version 44.0-7
%global gsd_version 48~rc
%global gsettings_desktop_schemas_version 48~alpha-2
%global upower_version 1.90.6
%global gtk4_version 4.15.2
%global gnome_bluetooth_version 42~alpha
%global libadwaita_version 1.8~alpha
%global nm_version 1.52.0
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
%bcond malcontent %[!0%{?rhel}]
Name:           gnome-control-center
Version:        51.0
Release:        1%{?dist}
Summary:        Utilities to configure the GNOME desktop
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/GNOME/gnome-control-center/
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
%if %{with malcontent}
%endif
%ifnarch s390 s390x
%endif
Requires: libadwaita%{?_isa} >= %{libadwaita_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop4%{?_isa} >= %{gnome_desktop_version}
Requires: gnome-online-accounts%{?_isa} >= %{gnome_online_accounts_version}
Requires: gnome-settings-daemon%{?_isa} >= %{gsd_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk4%{?_isa} >= %{gtk4_version}
Requires: upower%{?_isa} >= %{upower_version}
%ifnarch s390 s390x
Recommends: gnome-bluetooth%{?_isa} >= 1:%{gnome_bluetooth_version}
%endif
Requires: %{name}-filesystem = %{version}-%{release}
Requires: accountsservice
Requires: alsa-lib
Recommends: bolt
Requires: colord
Requires: cups-pk-helper
Requires: dbus
Requires: iso-codes
%if %{with malcontent}
Requires: malcontent
Recommends: malcontent-control
%endif
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor
Recommends: gnome-color-manager
Recommends: gnome-remote-desktop
Recommends: switcheroo-control
Requires: /usr/bin/tecla
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
Recommends: ppd-service
Suggests: tuned-ppd
%endif
Provides: control-center = 1:%{version}-%{release}
Provides: control-center%{?_isa} = 1:%{version}-%{release}
Obsoletes: control-center < 1:%{version}-%{release}
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk4)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-3.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(tecla)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
# /oreon:deps
%description
This package contains configuration utilities for the GNOME desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

%package filesystem
Summary: GNOME Control Center directories
BuildArch: noarch
Provides: control-center-filesystem = 1:%{version}-%{release}
Obsoletes: control-center-filesystem < 1:%{version}-%{release}
%description filesystem
The GNOME control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
  -Ddocumentation=true \
  -Dlocation-services=enabled \
%if %{with malcontent}
  -Dmalcontent=true \
%else
  -Dmalcontent=false \
%endif
  %{nil}
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/cursor-fonts
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-control-center-filesystem -f %{oreon_filedir}/gnome-control-center-filesystem.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
