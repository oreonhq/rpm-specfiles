%global source0_hash b313c7134eb173668f42535b0eb6e985eb94fdf5d2fe705940a6cbfdcbadbaf0

Name:		fcitx-chewing
Version:	0.2.3
Release:	24%{?dist}
Summary:	Chewing Wrapper for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Chewing
Source0:	http://download.fcitx-im.org/fcitx-chewing/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libchewing-devel
Requires:	fcitx, fcitx-data

%description
Fcitx-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/chewing.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/skin/classic/chewing.png
%{_datadir}/fcitx/skin/dark/chewing.png
%{_datadir}/fcitx/skin/default/chewing.png
%{_datadir}/icons/hicolor/48x48/apps/fcitx-chewing.png

%changelog
%autochangelog
