%global source0_hash 0d4eecd54e440cc11f1bdaaa23180fcf890f003444343f533f639086b05b2cc5

Name:       xvidtune
Version:    1.0.4
Release:    %autorelease
Summary:    Video mode tuner for Xorg
License:    X11-distribute-modifications-variant
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xvidtune is a client interface to the X server video mode extension
(XFree86-VidModeExtension).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xvidtune
%{_mandir}/man1/xvidtune.1*
%{_datadir}/X11/app-defaults/Xvidtune

%changelog
%autochangelog
