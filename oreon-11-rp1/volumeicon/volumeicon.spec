%global source0_hash 7bf6b6e2d1447940ab34027328539a46de1f03cc845def42e2e0ee93cca12ac9

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=722914

%global commit  b034dd1fefe38ef41a5e70f212f2aabf68010f93

Name:           volumeicon
Version:        0.5.1
Release:        20.20230208gitb034dd1%{?dist}
Summary:        Lightweight volume control for the system tray

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/Maato/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
# Source1 was borrowed from gnome-media package and adjusted for our needs
Source1:        %{name}.desktop

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel >= 0.5.0
BuildRequires:  intltool
BuildRequires:  gettext

Requires:       pavucontrol

# bundling of some functions partly copied from keybinder, currently retired
Provides:       bundled(keybinder) = 0.3.1

%description
Volume Icon aims to be a lightweight volume control that sits in your system
tray.

Features:
* Change volume by scrolling on the systray icon
* Ability to choose which channel to control
* Configurable stepsize
* Several icon themes
* Configurable external mixer
* Volume slider
* Hotkey support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{name}-%{commit}

%build
sh -v ./autogen.sh
# Use pavucontrol by default in Fedora
%configure --enable-notify --with-default-mixerapp=pavucontrol
%make_build

%install
%make_install INSTALL='install -p'
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_sysconfdir}/xdg/autostart %{SOURCE1}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README.md
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/man/man1/%{name}.1*
%{_datadir}/man/man5/%{name}.5*

%changelog
%autochangelog
