%global source0_hash a84704487ea3afe1485c47fb2ab598b8f779f540ae0dcbf0a1c5f85e64a7e253

%global gtk3_version    %(pkg-config --modversion gtk+-3.0 2>/dev/null || echo bad)
%global gtk4_version    %(pkg-config --modversion gtk4 2>/dev/null || echo bad)
%global glib2_version   %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global nm_version      1:1.16.0
%global libnma_version  1.8.27
%global obsoletes_ver   1:0.9.7

%if 0%{?fedora} > 31 || 0%{?rhel} > 8
%bcond_with libnma_gtk4
%else
%bcond_without libnma_gtk4
%endif

%if 0%{?fedora} || 0%{?rhel} < 9
%bcond_without appindicator
%else
%bcond_with appindicator
%endif

Name: network-manager-applet
Summary: A network control and status applet for NetworkManager
Version: 1.36.0
Release: 7%{?dist}
License: GPL-2.0-or-later
URL: http://www.gnome.org/projects/NetworkManager/
Obsoletes: NetworkManager-gnome < %{obsoletes_ver}

Source:        https://download.gnome.org/sources/network-manager-applet/1.36/network-manager-applet-1.36.0.tar.xz
Patch1: 0001-nm-applet-no-notifications.patch

%if ! 0%{?flatpak}
Requires: NetworkManager >= %{nm_version}
%endif
Requires: nm-connection-editor%{?_isa} = %{version}-%{release}
Requires: libnma%{?_isa} >= %{libnma_version}

BuildRequires: NetworkManager-libnm-devel >= %{nm_version}
BuildRequires: libnma-devel >= %{libnma_version}
BuildRequires: ModemManager-glib-devel >= 1.0
BuildRequires: glib2-devel >= 2.32
BuildRequires: gtk3-devel >= 3.10
%if %{with libnma_gtk4}
BuildRequires: gtk4-devel >= 3.96
%endif
BuildRequires: gobject-introspection-devel >= 0.10.3
BuildRequires: gettext-devel
BuildRequires: /usr/bin/autopoint
BuildRequires: pkgconfig
BuildRequires: meson
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: desktop-file-utils
BuildRequires: iso-codes-devel
BuildRequires: libsecret-devel >= 0.12
BuildRequires: jansson-devel
BuildRequires: gcr-devel
BuildRequires: libselinux-devel
BuildRequires: mobile-broadband-provider-info-devel
%if %{with appindicator}
BuildRequires: libappindicator-gtk3-devel
%endif
%if 0%{?fedora} || 0%{?rhel} < 9
BuildRequires: libdbusmenu-gtk3-devel
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

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

# validate .desktop and autostart files
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/nm-applet.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/nm-connection-editor.desktop

%check
%meson_test


%files
%{_bindir}/nm-applet
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/icons/hicolor/22x22/apps/nm-adhoc.png
%{_datadir}/icons/hicolor/22x22/apps/nm-insecure-warn.png
%{_datadir}/icons/hicolor/22x22/apps/nm-mb-roam.png
%{_datadir}/icons/hicolor/22x22/apps/nm-secure-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-signal-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-stage*-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-tech-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-active-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-wwan-tower.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%{_datadir}/GConf/gsettings/nm-applet.convert
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%{_mandir}/man1/nm-applet*
%doc NEWS CONTRIBUTING
%license COPYING

# Yes, lang files for the applet go in nm-connection-editor RPM since it
# is the RPM that everything else depends on
%files -n nm-connection-editor -f %{name}.lang
%{_bindir}/nm-connection-editor
%{_datadir}/icons/hicolor/*/apps/nm-device-*.*
%{_datadir}/icons/hicolor/*/apps/nm-no-connection.*
%{_datadir}/icons/hicolor/16x16/apps/nm-vpn-standalone-lock.png
%{_mandir}/man1/nm-connection-editor*
%dir %{_datadir}/gnome-vpn-properties


%files -n nm-connection-editor-desktop
%{_datadir}/applications/nm-connection-editor.desktop
%{_datadir}/metainfo/nm-connection-editor.appdata.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.36.0-7
- Prepare for Oreon 11 (RP1)
