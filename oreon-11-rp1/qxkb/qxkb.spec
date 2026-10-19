%global source0_hash e1741abf7364b1aee35f20130a2c4559040f37b84d223692f681593aed862e4b
%undefine __cmake_in_source_build
%global commit ee9a1eee9dc810b33b931601203051d841bc3e7a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		qxkb
Version:	0.5.1
Release:        17%{?dist}
License:	GPL-2.0-only
Url:		https://github.com/disels/qxkb
Source0:        https://github.com/disels/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Summary:        Qt keyboard layout switcher
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  qt5-linguist
# /oreon:deps
%description
The keypad switch written on Qt5.
Uses setxkbmap.
The interface repeats kxkb.
Can use svg icon for indicate language layer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
