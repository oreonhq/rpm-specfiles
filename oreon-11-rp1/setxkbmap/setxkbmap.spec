%global source0_hash 360193cecc93f906d8383a8fb5c1f3a7eed35e6ced0e118a64ee56ae13c88cac
Name:       setxkbmap
Version:    1.3.5
Release:        1%{?dist}
Summary:        X11 keymap client
License:    HPND
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/setxkbmap-%{version}.tar.xz
Obsoletes:  xorg-x11-xkb-utils < 7.8
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
setxkbmap is an X11 client to change the keymaps in the X server for a
specified keyboard to use the layout determined by the options listed
on the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
