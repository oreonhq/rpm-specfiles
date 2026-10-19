%global source0_hash ec228b305091b649c16c690e102aa1d66fc10e9834888d51e411913c82c1430d
%global xdg_desktop_portal_version 1.19.1
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           xdg-desktop-portal-gnome
Version:        51.0
Release:        1%{?dist}
Summary:        Backend implementation for xdg-desktop-portal using GNOME
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/%{name}
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:       dbus
Requires:       dbus-common
Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}
Supplements:    gnome-shell
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gnome-bg-4)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(xdg-desktop-portal)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A backend implementation for xdg-desktop-portal that is using various pieces of
GNOME infrastructure, such as the org.gnome.Shell.Screenshot or
org.gnome.SessionManager D-Bus interfaces.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dsystemduserunitdir=%{_userunitdir}
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
