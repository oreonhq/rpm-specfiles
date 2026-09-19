%global source0_hash d4c30b0e6f18c82f387585a737ee3b72d468c927892b08a898c41bc12248e8ee

Name:           xbacklight
Version:        1.2.4
Release:        %autorelease
Summary:        Adjust backlight brightness using RandR

License:        MIT
URL:            https://xorg.freedesktop.org/releases/individual/app/
Source:         https://xorg.freedesktop.org/releases/individual/app/xbacklight-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-randr)

%description
Xbacklight is used to adjust the backlight brightness where
supported. It finds all outputs on the X server supporting backlight
brightness control and changes them all in the same way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xbacklight
%{_datadir}/man/man1/xbacklight.*

%changelog
%autochangelog
