%global source0_hash 5ff264bc4eebc0459255a92036dc8dc84b6d48caef8509f88a783beaadea750b
Name:       xkill
Version:    1.0.7
Release:        1%{?dist}
Summary:        Utility to force-close an X client's connection
License:    MIT-open-group
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
xkill is a utility for forcing the X server to close connections to
clients. This program is very dangerous, but is useful for aborting
programs that have displayed undesired windows on a user's screen.

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
