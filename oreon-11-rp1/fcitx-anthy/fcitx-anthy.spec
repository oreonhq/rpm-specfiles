%global source0_hash 1f186cd915ee15ffdb85ccdc437f998fe808dfe6780447c8ccc21f50e50d5fb3
Name:			fcitx-anthy
Version:		0.2.4
Release:        1%{?dist}
Summary:        Anthy Engine for Fcitx
License:		GPL-2.0-or-later
URL:			https://fcitx-im.org/wiki/Anthy
Source0:        https://download.fcitx-im.org/fcitx-anthy/%{name}-%{version}.tar.xz
Requires:		fcitx
Requires:		dbus-x11
# oreon:deps
BuildRequires:  anthy-devel
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
