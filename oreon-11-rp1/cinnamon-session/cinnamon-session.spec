%global source0_hash ac7426dc383bbec3bd1576cb569d0837d95a87ec166a897263e0941be95feed6

%global cinnamon_desktop_version 6.6.0

Summary: Cinnamon session manager
Name:    cinnamon-session
Version: 6.6.3
Release: 1%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch: %{ix86}

Requires: system-logos
# Needed for cinnamon-settings-daemon
Requires: cinnamon-control-center-filesystem

# pull in dbus-x11, see bug 209924
Requires: dbus-x11

# an artificial requires to make sure we get dconf, for now
Requires: dconf

Requires: cinnamon-desktop >= %{cinnamon_desktop_version}

BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.37.3
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xapp) >= 1.4.6
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: meson
BuildRequires: gcc
BuildRequires: intltool
BuildRequires: python3-packaging
BuildRequires: xmlto

%description
Cinnamon-session manages a Cinnamon desktop or GDM login session. It starts up
the other core components and handles logout and saving the session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%doc AUTHORS README
%doc %{_mandir}/man*/*
%license COPYING
%{_bindir}/*
%{_libexecdir}/cinnamon-session-binary
%{_libexecdir}/cinnamon-session-check-accelerated
%{_libexecdir}/cinnamon-session-check-accelerated-helper
%{_datadir}/cinnamon-session/
%{_datadir}/icons/hicolor/*/apps/cinnamon-session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/cinnamon-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml

%changelog
%autochangelog
