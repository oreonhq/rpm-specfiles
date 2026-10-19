%global source0_hash 17fe59f23da7721d43bfa5a06cb2bc09214f3b9aecef257ee385d802c7f3a732
Name:		fcitx-skk
Version:	0.1.4
Release:        1%{?dist}
Summary:        Japanese SKK (Simple Kana Kanji) Engine for Fcitx
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
Requires:	fcitx
Requires:	skkdic
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libskk-devel
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
Fcitx-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

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
