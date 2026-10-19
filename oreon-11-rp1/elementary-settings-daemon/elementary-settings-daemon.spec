%global source0_hash 6cff7ab2842f264e0f0b42093789de895fb28c0043a90f0fcaa2af84076ade03
%global srcname settings-daemon
%global appname io.elementary.settings-daemon
%global iface   io.elementary.SettingsDaemon.AccountsService
Name:           elementary-settings-daemon
Version:        8.5.0
Release:        1%{?dist}
Summary:        Settings Daemon and Portal for Pantheon
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/elementary/settings-daemon
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires:       accountsservice
Requires:       dbus-common
Requires:       xdg-desktop-portal
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appname}
%oreon_autofiles main

%check

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%post

%systemd_post %{appname}.check-for-firmware-updates.timer
%systemd_user_post %{appname}.xdg-desktop-portal.service
%preun

%systemd_preun %{appname}.check-for-firmware-updates.timer
%systemd_user_preun %{appname}.xdg-desktop-portal.service
%postun

%systemd_postun_with_restart %{appname}.check-for-firmware-updates.timer
%systemd_user_postun_with_restart %{appname}.xdg-desktop-portal.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
