%global source0_hash ed9b4956356ca68e5f7bdd46492873ebebc921a6cf713d7fc62e5680393f5d06

Name:			fcitx-anthy
Version:		0.2.3
Release:		14%{?dist}
Summary:		Anthy Engine for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:		GPL-2.0-or-later
URL:			https://fcitx-im.org/wiki/Anthy
Source0:		https://download.fcitx-im.org/fcitx-anthy/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	fcitx-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	anthy-devel
BuildRequires:	gcc-c++
Requires:		fcitx
Requires:		dbus-x11

%description
Fcitx-anthy is an Anthy engine wrapper for Fcitx. It provides a Japanese input
method. You can input hiragana and katakana by romaji or using a Japanese
keyboard. And fcitx-anthy also supports converting hiragana or katakana to
kanji.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%build
%cmake
%cmake_build 

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS README
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/anthy/
%{_datadir}/fcitx/inputmethod/anthy.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/imicon/anthy.png
%{_datadir}/icons/hicolor/48x48/status/%{name}.png
%{_datadir}/icons/hicolor/22x22/status/%{name}-symbol.png
%{_datadir}/icons/hicolor/scalable/status/%{name}-*.svg

%changelog
%autochangelog
