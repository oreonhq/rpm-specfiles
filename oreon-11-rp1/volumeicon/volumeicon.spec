%global source0_hash 7bf6b6e2d1447940ab34027328539a46de1f03cc845def42e2e0ee93cca12ac9
%global commit  b034dd1fefe38ef41a5e70f212f2aabf68010f93
Name:           volumeicon
Version:        0.5.1
Release:        1%{?dist}
Summary:        Lightweight volume control for the system tray
License:        GPL-3.0-only
URL:            https://github.com/Maato/%{name}
Source0:        https://github.com/Maato/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:        %{name}.desktop
Requires:       pavucontrol
Provides:       bundled(keybinder) = 0.3.1
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libnotify-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
%build

sh -v ./autogen.sh
%configure --enable-notify --with-default-mixerapp=pavucontrol
%make_build
%install
%make_install INSTALL='install -p'
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_sysconfdir}/xdg/autostart %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
