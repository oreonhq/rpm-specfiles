%global source0_hash a30a5ebead35cc78e5f337571df8c5de2bdd9141426034c74b17e4d3db15f024
Name:           i3lock
Version:        2.16
Release:        1%{?dist}
Summary:        Simple X display locker like slock
License:        MIT
URL:            https://i3wm.org/%{name}
Source0:        https://i3wm.org/%{name}/%{name}-%{version}.tar.xz
Source1:        %{URL}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
# /oreon:deps
%description
i3lock is a simple screen locker like slock. After starting it, you will see a
white screen (you can configure the color/an image). You can return to your
screen by entering your password.

Many little improvements have been made to i3lock over time:

- i3lock forks, so you can combine it with an alias to suspend to RAM (run
  "i3lock && echo mem > /sys/power/state" to get a locked screen after waking up
  your computer from suspend to RAM)

- You can specify either a background color or a PNG image which will be
  displayed while your screen is locked.

- You can specify whether i3lock should bell upon a wrong password.

- i3lock uses PAM and therefore is compatible with LDAP etc. On OpenBSD i3lock
  uses the bsd_auth(3) framework.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
