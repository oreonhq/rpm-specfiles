%global source0_hash fc1238e3aa5b82787a95d49cb3e1bac0671e4d3a40090087848f43f3e1f63a98
%global forgeurl	https://github.com/cage-kiosk/cage
Name:			cage
Version:		0.3.1
Release:        1%{?dist}
Summary:        A Wayland kiosk
License:		MIT
URL:			https://www.hjdskes.nl/projects/cage
Source0:        %{forgeurl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:		%{forgeurl}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:		gpgkey-E88F5E48.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
This is Cage, a Wayland kiosk. A kiosk runs a single, maximized application.

This README is only relevant for development resources and instructions. For a
description of Cage and installation instructions for end-users, please see its
project page and the Wiki.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
