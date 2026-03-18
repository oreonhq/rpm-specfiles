Name:       setxkbmap
Version:    1.3.4
Release:    7%{?dist}
Summary:    X11 keymap client

License:    HPND
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/setxkbmap-%{version}.tar.xz

BuildRequires:  make gcc
BuildRequires:  pkgconfig(x11) pkgconfig(xrandr)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-xkb-utils < 7.8

%description
setxkbmap is an X11 client to change the keymaps in the X server for a
specified keyboard to use the layout determined by the options listed
on the command line.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.4-7
- Prepare for Oreon 11 (RP1)
