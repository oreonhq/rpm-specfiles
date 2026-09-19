%global source0_hash ac87f7c6135025bfec579b40d7a167bdfb10ce5f7b367dc5baeaaf78864d3dc2

%global uuid org.gnome.BreakTimer

Name: gnome-break-timer
Version: 2.0.3
Release: 14%{?dist}
Summary: Break timer application for GNOME

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://wiki.gnome.org/Apps/BreakTimer
Source0: https://gitlab.gnome.org/GNOME/gnome-break-timer/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gsound)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libnotify)

Requires: dbus-common
Requires: hicolor-icon-theme

%description
This helps you to schedule regular breaks. It will remind you to take them
based on how much you are using the computer. It tries to be simple but
helpful, and it uses notifications to indicate when a break has arrived.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md ABOUT-NLS AUTHORS NEWS
%{_bindir}/%{name}-*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml
%{_sysconfdir}/xdg/autostart/*.desktop

%changelog
%autochangelog
