%global source0_hash 0d4eecd54e440cc11f1bdaaa23180fcf890f003444343f533f639086b05b2cc5
Name:       xvidtune
Version:    1.0.4
Release:        1%{?dist}
Summary:        Video mode tuner for Xorg
License:    X11-distribute-modifications-variant
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-apps < 7.7-31
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xxf86vm)
# /oreon:deps
%description
xvidtune is a client interface to the X server video mode extension
(XFree86-VidModeExtension).

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
