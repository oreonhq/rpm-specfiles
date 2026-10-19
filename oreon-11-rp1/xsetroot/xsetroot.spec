%global source0_hash 1315a3f7e9abe06357363b93461e272601f67225ce0bc075c430cce35073362b
Name:       xsetroot
Version:    1.1.4
Release:        1%{?dist}
Summary:        Root window parameter setting utility for X
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
BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
The xsetroot program allows you to tailor the appearance of the background
window of an X server.

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
