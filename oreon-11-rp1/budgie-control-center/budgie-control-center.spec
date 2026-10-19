%global source0_hash ad173a72bc8e06b9e256589593a9c2853bc46746e74076d0052af0150d14600a
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
Version:       2.1.3
Release:        1%{?dist}
Summary:        A fork of GNOME Control Center for the Budgie 10 Series
License:       GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:           https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:        https://github.com/BuddiesOfBudgie/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:       introduction.list
ExcludeArch:   %{ix86}
%ifnarch s390 s390x
%endif
Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_stack}
Requires: gnome-settings-daemon%{?_isa} >= %{gnome_stack}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gnome_stack}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}
Requires: %{name}-common = %{version}-%{release}
Requires: accountsservice
Requires: alsa-lib
Recommends: bolt
Requires: colord
Requires: cups-pk-helper
Requires: dbus
Requires: glx-utils
Recommends: switcheroo-control
Requires: iso-codes
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor
Requires: malcontent
Requires: malcontent-control
Requires: fprintd
Recommends: gnome-color-manager
Recommends: ppd-service
Suggests: tuned-ppd
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
# /oreon:deps
%description
A fork of GNOME Control Center for the Budgie 10 Series.

%package common
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
Summary: Common assets for %{name}
BuildArch: noarch
Requires: hicolor-icon-theme
%description common
This package contains architecture-agnostic common assets for ${name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
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
%oreon_autofiles budgie-control-center-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnn_name}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n budgie-control-center-common -f %{oreon_filedir}/budgie-control-center-common.list

%changelog

%autochangelog
