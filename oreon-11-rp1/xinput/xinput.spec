%global source0_hash ad04d00d656884d133110eeddc34e9c69e626ebebbbab04dc95791c2907057c8
Name:       xinput
Version:    1.6.4
Release:        1%{?dist}
Summary:        Utility to query X Input devices
License:    MIT AND HPND-sell-variant
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
xinput is a commandline utility to query and configure X11 X Input Extension
devices. It is commonly used to change driver properties at runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install
%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
