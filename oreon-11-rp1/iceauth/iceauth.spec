%global source0_hash 9d633cf0d4d1d98e3ef02d18660372958b60a67016e8a72cd04093a8d8f8d4e9
Name:       iceauth
Version:    1.0.11
Release:        1%{?dist}
Summary:        Display the authorization information used in connecting with ICE
License:    MIT-open-group
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes:  xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE. It operates very much
like the xauth program for X11 connection authentication records.

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
