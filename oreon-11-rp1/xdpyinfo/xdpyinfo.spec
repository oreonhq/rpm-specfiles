%global source0_hash dc1de6e6e091ed46c4837b0ae9811e8182f7be0d2af638cab3e530ff081a48b6
Summary:        X11 display information utility
Name:       xdpyinfo
Version:    1.4.0
Release:        1%{?dist}
License:    MIT
URL:        http://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes: xorg-x11-utils < 7.5-39
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dmx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  pkgconfig(xxf86vm)
# /oreon:deps
%description
xdpyinfo prints basic diagnostic information about a given X server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
