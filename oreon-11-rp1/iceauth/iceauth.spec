%global source0_hash 3deefb7da26af9dc799b5628d929d91c9af68c78575639944db3b955f29aa029

Name:       iceauth
Version:    1.0.10
Release:    %autorelease
Summary:    Display the authorization information used in connecting with ICE

License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE. It operates very much
like the xauth program for X11 connection authentication records.

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
