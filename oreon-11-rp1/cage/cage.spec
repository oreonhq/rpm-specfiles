%global source0_hash fc1238e3aa5b82787a95d49cb3e1bac0671e4d3a40090087848f43f3e1f63a98

%global forgeurl	https://github.com/cage-kiosk/cage

Name:			cage
Version:		0.2.1
Release:		3%{?dist}
Summary:		A Wayland kiosk

License:		MIT
URL:			https://www.hjdskes.nl/projects/cage
Source0:		%{forgeurl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:		%{forgeurl}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# https://keys.openpgp.org/search?q=34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48
Source2:		gpgkey-E88F5E48.gpg

BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	meson
BuildRequires:	pkgconfig(scdoc)
BuildRequires:	pkgconfig(wlroots-0.19)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.14
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)

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

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
