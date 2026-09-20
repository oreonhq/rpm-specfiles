%global source0_hash 2cafccb2aaf2491a4068676117a0d4f90ab307724b96fffc54cd1da953779400

Name:       xrandr
Version:    1.5.4
Release:    %autorelease
Summary:    Commandline utility to change output properties

License:    HPND-sell-variant
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xrandr is a commandline utility to set the size, orientation and/or
reflection of the outputs for an X screen. It can also set the screen size
and turn outputs on and off..

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

# "needs more nickle bindings" since 2009...
rm -f $RPM_BUILD_ROOT%{_bindir}/xkeystone

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
