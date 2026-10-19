%global source0_hash 062a15722769799524eee542fc82ae778f5ac180b618295d913f34962b134ffe
Name:           xstdcmap
Version:        1.0.6
Release:        1%{?dist}
Summary:        Utility to define standard colormap properties
License:        MIT
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:        %{url}/pub/individual/app/%{name}-%{version}.tar.xz.sig
Obsoletes:      xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
# /oreon:deps
%description
The xstdcmap utility can be used to selectively define standard colormap
properties.  It is intended to be run from a user's X startup script to
create standard colormap definitions in order to facilitate sharing of
scarce colormap resources among clients using PseudoColor visuals.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
