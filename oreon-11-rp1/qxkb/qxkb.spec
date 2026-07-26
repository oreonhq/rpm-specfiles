%global source0_hash cf588c02a4aab35ad3eab72c050969f7afd08f97665e9b87e524d04279721c70

%undefine __cmake_in_source_build

%global commit ee9a1eee9dc810b33b931601203051d841bc3e7a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		qxkb
Version:	0.5.1
Release:	17%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
Url:		https://github.com/disels/qxkb
Source0:	https://github.com/disels/qxkb/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Summary:	Qt keyboard layout switcher
BuildRequires:	cmake, desktop-file-utils
# libxkbfile-devel
BuildRequires:	pkgconfig(xkbfile)
# qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Core)
# qt5-qtsvg-devel
BuildRequires:	pkgconfig(Qt5Svg)
# qt5-qtx11extras-devel
BuildRequires:	pkgconfig(Qt5X11Extras)
# qt5-linguist
BuildRequires:	qt5-linguist
#BuildRequires:	pkgconfig(Qt5LinguistTools)

%description
The keypad switch written on Qt5.
Uses setxkbmap.
The interface repeats kxkb.
Can use svg icon for indicate language layer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
