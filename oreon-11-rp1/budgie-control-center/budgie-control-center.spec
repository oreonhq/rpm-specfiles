%global source0_hash b61ecd9946dfc5e75714d3311def8ba90efeaad58b4342ea001c236da50ea56c

%global cheese_version 3.28.0
%global glib2_version 2.64
%global gnome_online_accounts_version 3.44.0
%global gnome_stack 42.0
%global gtk3_version 3.24
%global polkit_version 0.105
%global upower_version 0.99.8
%global vala_version 0.52.5
%global rdnn_name org.buddiesofbudgie.controlcenter

%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

Name:          budgie-control-center
Version:       2.1.0
Release:       1%{?dist}
Summary:       A fork of GNOME Control Center for the Budgie 10 Series

# GPL-2.0-or-later: the entire project
# GPL-3.0-or-later:
# - panels/applications/*
# - panels/background/bg-recent-source.{c,h}
# - panels/background/cc-background-{chooser,preview}.{c,h}
# - panels/common/cc-list-row.{c,h}
# - panels/common/cc-permission-infobar.{c,h}
# - panels/multitasking/cc-multitasking-row.{c,h}
# - panels/network/cc-qr-code.{c,h}
# - panels/network/cc-wifi-hotspot-dialog.{c,h}
# - panels/power/cc-power-profile-{info-,}row.{c,h}
# - panels/printers/pp-job-row.{c,h}
# - panels/wwan/*
# LGPL-2.0-or-later:
# - panels/notifications/cc-app-notifications-dialog.{c,h}
# - panels/notifications/cc-notifications-panel.{c,h}
# - panels/online-accounts/cc-online-accounts-panel.{c,h}
# LGPL-2.1-or-later:
# - panels/thunderbolt/*
# LGPL-3.0-or-later:
# - panels/sharing/cc-tls-certificate.{c,h}
# LicenseRef-Fedora-Public-Domain:
# - panels/datetime/backward
# Files with inconsistent license statements (GPL or LGPL?):
# - panels/universal-access/*
License:       GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:           https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:       %{url}/releases/download/v%{version}/budgie-control-center-%{version}.tar.xz
Source1:       introduction.list

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= %{cheese_version}
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_stack}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gnome_stack}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gnome_stack}
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm) >= 1.24
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.13
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libwacom)
%endif

Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_stack}
Requires: gnome-settings-daemon%{?_isa} >= %{gnome_stack}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gnome_stack}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}

# Need common
Requires: %{name}-common = %{version}-%{release}

# For user accounts
Requires: accountsservice
Requires: alsa-lib

# For the thunderbolt panel
Recommends: bolt

# For the color panel
Requires: colord

# For the printers panel
Requires: cups-pk-helper
Requires: dbus

# For the info/details panel
Requires: glx-utils
Recommends: switcheroo-control

# For the user languages
Requires: iso-codes

# For the network panel
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor

# For parental controls support
Requires: malcontent
Requires: malcontent-control

# Fingerprint support
Requires: fprintd

# For Show Details in the color panel
Recommends: gnome-color-manager

# For the power panel
Recommends: ppd-service
%if 0%{?fedora} && 0%{?fedora} < 41
Suggests: power-profiles-daemon
%else
Suggests: tuned-ppd
%endif

%description
A fork of GNOME Control Center for the Budgie 10 Series.

%package common
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
Summary: Common assets for %{name}
BuildArch: noarch

Requires: hicolor-icon-theme

%description common
This package contains architecture-agnostic common assets for ${name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%meson \
    -Dbluetooth=false \
    -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/system-logo-white.png \
    -Ddocumentation=true \
    -Dmalcontent=true
%meson_build

%install
%meson_install
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/introduction/introduction.list
mkdir -p %{buildroot}%{_datadir}/budgie/wm-properties
rm -rf %{buildroot}%{_datadir}/budgie/autostart
rm -rf %{buildroot}%{_datadir}/budgie/cursor-fonts
chrpath --delete %{buildroot}%{_bindir}/%{name}
%find_lang %{name} --all-name --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnn_name}.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/budgie-cc-remote-login-helper
%{_libexecdir}/%{name}-print-renderer
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings-*.svg
%{_datadir}/man/man1/%{name}.1*
%{_datadir}/metainfo/%{rdnn_name}.metainfo.xml

%files common -f %{name}.lang
%dir %{_datadir}/budgie
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/keybindings
%dir %{_datadir}/%{name}/pixmaps
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_datadir}/pixmaps
%dir %{_datadir}/pixmaps/budgie-faces
%dir %{_datadir}/pixmaps/budgie-faces/legacy
%dir %{_datadir}/sounds/budgie
%dir %{_datadir}/sounds/budgie/default
%dir %{_datadir}/sounds/budgie/default/alerts
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie/wm-properties
%{_datadir}/pixmaps/budgie-faces/*.jpg
%{_datadir}/pixmaps/budgie-faces/*.png
%{_datadir}/pixmaps/budgie-faces/legacy/*.jpg
%{_datadir}/pixmaps/budgie-faces/legacy/*.png
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/%{name}/introduction/introduction.template
%{_datadir}/%{name}/introduction/introduction.list
%{_datadir}/%{name}/keybindings/*.xml
%{_datadir}/%{name}/keyfile/labwc_keyfile.ini
%{_datadir}/%{name}/pixmaps/noise-texture-light.png
%{_datadir}/icons/hicolor/scalable/*/budgie-*.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.buddiesofbudgie.Settings-symbolic.svg
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/%{name}.rules
%{_datadir}/sounds/budgie/default/alerts/*.ogg

%changelog
%autochangelog
