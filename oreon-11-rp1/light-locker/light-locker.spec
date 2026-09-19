%global source0_hash 9915ed34b6c38f519e17902541a180b8b2d775c26edd8ed5aba024722039157c

Name:           light-locker
Version:        1.9.0
Release:        17%{?dist}
Summary:        Simple session-locker for lightdm
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

URL:            https://github.com/the-cavalry/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  xorg-x11-proto-devel

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)

# functional runtime
Requires:       lightdm

%description
light-locker is a simple locker (forked from gnome-screensaver)
that aims to have simple, sane, secure defaults and be well
integrated with the desktop while not carrying any desktop-
specific dependencies.

It relies on lightdm for locking and unlocking your session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
    -Dmit-ext=true \
    -Ddpms-ext=true \
    -Dxf86gamma-ext=true \
    -Dsystemd=true \
    -Dupower=true \
    -Dlate-locking=true \
    -Dlock-on-suspend=true \
    -Dlock-on-lid=true \
    -Dgsettings=true

%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%{_bindir}/%{name}
%{_bindir}/%{name}-command

%{_datadir}/glib-2.0/schemas/apps.%{name}.gschema.xml
%{_mandir}/man1/%{name}*.1*

%changelog
%autochangelog
