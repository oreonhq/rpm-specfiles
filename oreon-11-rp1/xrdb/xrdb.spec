%global source0_hash c88f560243278c896ce4fc92ae5a45a2b505a316ffa427fe55b02e5d5914c4e4
Name:       xrdb
Version:    1.2.3
Release:        1%{?dist}
Summary:        X server resource database utility
License:    HPND-DEC AND MIT-open-group
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Recommends: cpp
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
xrdb is used to get or set the contents of the RESOURCE_MANAGER property on
the root window of screen 0, or the SCREEN_RESOURCES property on the
root window of any or all screens, or everything combined.

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
