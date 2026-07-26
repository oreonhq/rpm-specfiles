%global source0_hash 4e85b52f4f65a93449753bfb00ceb5d77f3317e24d07dc23147f2f116c785350

Name:       sessreg
Version:    1.1.4
Release:    %autorelease
Summary:    Utility to manage utmp/wtmp entries for X sessions
License:    MIT AND MIT-open-group 
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
Sessreg is a simple program for managing utmp/wtmp entries for X sessions.
It was originally written for use with xdm, but may also be used with
other display managers such as gdm or kdm.

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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
