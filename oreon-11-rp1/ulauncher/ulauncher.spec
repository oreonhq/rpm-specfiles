%global source0_hash 5a229f51180c756fda68d2adb764e1653fef1f4b5f05afa01b3163725f6adaac
Name:           ulauncher
Version:        5.16.2
Release:        1%{?dist}
Summary:        Feature rich application Launcher for Linux
BuildArch:      noarch
License:        GPL-3.0-or-later
URL:            https://github.com/Ulauncher/Ulauncher
Source0:        https://github.com/Ulauncher/Ulauncher/releases/download/%{version}/%{name}_%{version}.tar.gz
Requires:       hicolor-icon-theme
Requires:       keybinder3
Requires:       webkit2gtk4.1
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-inotify
Requires:       python3-Levenshtein
Requires:       python3-pyxdg
Requires:       python3-websocket-client
Requires:       wmctrl
Recommends:     libappindicator-gtk3
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  keybinder3-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-inotify
BuildRequires:  python3-pyxdg
BuildRequires:  python3-setuptools
BuildRequires:  python3-websocket-client
BuildRequires:  python3dist(requests)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Ulauncher is a fast application launcher for Linux. It's written in Python using
GTK+, and features: App Search (fuzzy matching), Calculator, Extensions,
Shortcuts, File browser mode and Custom Color Themes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1
# Newer version patch: https://github.com/Ulauncher/Ulauncher/issues/1194
sed -i "s|version=''|version='%{version}'|g" setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%postun

%systemd_user_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
