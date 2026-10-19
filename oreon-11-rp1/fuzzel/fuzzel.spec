%global source0_hash 11bee600e19ee1638db592e41980445673224716fbedbd0213b25153325f4182
Name:           fuzzel
Version:        1.15.0
Release:        1%{?dist}
Summary:        App launcher and fuzzy finder for Wayland, inspired by rofi
License:        MIT
URL:            https://codeberg.org/dnkl/fuzzel
Source0:        https://codeberg.org/dnkl/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-5BBD4992C116573F.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  nanosvg-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  tllist-static
# /oreon:deps
%description
Fuzzel is a Wayland-native application launcher and fuzzy finder, inspired by
rofi and dmenu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -Dsystem-nanosvg=enabled \
  %{nil}
%meson_build
%install
%meson_install
rm %{buildroot}%{_docdir}/%{name}/LICENSE
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
