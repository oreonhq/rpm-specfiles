%global source0_hash 2cafccb2aaf2491a4068676117a0d4f90ab307724b96fffc54cd1da953779400
Name:       xrandr
Version:    1.5.4
Release:        1%{?dist}
Summary:        Commandline utility to change output properties
License:    HPND-sell-variant
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
# /oreon:deps
%description
xrandr is a commandline utility to set the size, orientation and/or
reflection of the outputs for an X screen. It can also set the screen size
and turn outputs on and off..

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install
%configure --disable-silent-rules
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_bindir}/xkeystone
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
