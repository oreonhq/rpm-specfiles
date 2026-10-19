%global source0_hash e6d0bf94979af5ab8aa478fd99fcd38bff51616ecdee4b36e5c9ddcb4af8f604
%define po_package budgie-session-1
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}
Name:           budgie-session
Version:        1.0.1
Release:        1%{?dist}
Summary:        Budgie Desktop session manager
License:        GPL-2.0-or-later
URL:            https://github.com/BuddiesOfBudgie/budgie-session
Source0:        https://github.com/BuddiesOfBudgie/%{name}/releases/download/v{version_no_tilde}/%{name}-v%{version}.tar.xz
Requires: dconf
Requires: system-logos
Requires: gsettings-desktop-schemas >= 0.1.7
Requires: dbus
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  usermode
BuildRequires:  xmlto
# /oreon:deps
%description
Budgie Session is a softish fork of gnome-session, designed to
provide a stable session manager for Budgie 10.x

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson -Dsystemd=true -Dsystemd_journal=true -Dsystemd_session="default"
%meson_build
%install
%meson_install
%find_lang %{po_package}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
