%global source0_hash 0c163f39a33746aec14a12ebe30f13e0f210e3b383979e7597512eabddca64b6

Name:           xdg-desktop-portal-xapp
Version:        1.1.3
Release:        2%{?dist}
Summary:        Backend implementation for xdg-desktop-portal using Xapp

License:        LGPL-2.1-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= 1.7.1
BuildRequires:  systemd-rpm-macros

Requires:       dbus-x11
Requires:       dbus-common
Requires:       xapps >= 2.5.0
Requires:       xdg-desktop-portal >= 1.7.1
Requires:       xdg-desktop-portal-gtk
Supplements:    cinnamon

%description
Xapp's Cinnamon, MATE and XFCE backends for xdg-desktop-portal.
This allows sandboxed applications to request services and information from
outside the sandbox in the MATE, XFCE and Cinnamon environments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dsystemduserunitdir=%{_userunitdir}
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license COPYING
%doc README.md
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.xapp.service
%{_datadir}/xdg-desktop-portal/portals/xapp.portal
%{_datadir}/xdg-desktop-portal/portals/xapp-gnome-keyring.portal
%{_userunitdir}/xdg-desktop-portal-xapp.service

%changelog
%autochangelog
