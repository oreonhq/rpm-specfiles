%global source0_hash a84704487ea3afe1485c47fb2ab598b8f779f540ae0dcbf0a1c5f85e64a7e253
%global gtk3_version    %(pkg-config --modversion gtk+-3.0 2>/dev/null || echo bad)
%global gtk4_version    %(pkg-config --modversion gtk4 2>/dev/null || echo bad)
%global glib2_version   %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global nm_version      1:1.16.0
%global libnma_version  1.8.27
%global obsoletes_ver   1:0.9.7
%bcond_without libnma_gtk4
%bcond_with appindicator
Name: network-manager-applet
Summary:        A network control and status applet for NetworkManager
Version: 1.36.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.gnome.org/projects/NetworkManager/
Obsoletes: NetworkManager-gnome < %{obsoletes_ver}
Source0:        https://download.gnome.org/sources/network-manager-applet/1.36/%{name}-%{version}.tar.xz
Patch1: 0001-nm-applet-no-notifications.patch
%if ! 0%{?flatpak}
Requires: NetworkManager >= %{nm_version}
%endif
Requires: nm-connection-editor%{?_isa} = %{version}-%{release}
Requires: libnma%{?_isa} >= %{libnma_version}
%if %{with libnma_gtk4}
%endif
%if %{with appindicator}
%endif
# oreon:deps
BuildRequires:  /usr/bin/autopoint
BuildRequires:  ModemManager-glib-devel
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcr-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  jansson-devel
BuildRequires:  libnma-devel
BuildRequires:  libsecret-devel
BuildRequires:  libselinux-devel
BuildRequires:  meson
BuildRequires:  mobile-broadband-provider-info-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
This package contains a network control and status notification area applet
for use with NetworkManager.

%package -n nm-connection-editor
Summary: A network connection configuration editor for NetworkManager
Requires: libnma%{?_isa} >= %{libnma_version}
%description -n nm-connection-editor
This package contains a network configuration editor and Bluetooth modem
utility for use with NetworkManager.

%package -n nm-connection-editor-desktop
Summary: The desktop file for nm-connection-editor
Requires: nm-connection-editor%{?_isa} = %{version}-%{release}
%description -n nm-connection-editor-desktop
This package contains the desktop file and appdata for nm-connection-editor.
Without it, the nm-connection-editor cannot be started from the desktop
environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Dselinux=true \
%if %{with appindicator}
    -Dappindicator=auto
%else
    -Dappindicator=no
%endif
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-vpn-properties
%find_lang nm-applet
cat nm-applet.lang >> %{name}.lang
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/nm-applet.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/nm-connection-editor.desktop
%oreon_autofiles nm-connection-editor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nm-connection-editor-desktop usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n nm-connection-editor -f %{oreon_filedir}/nm-connection-editor.list
%files -n nm-connection-editor-desktop -f %{oreon_filedir}/nm-connection-editor-desktop.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.36.0-7
- Prepare for Oreon 11 (RP1)
