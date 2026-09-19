%global source0_hash 17fe59f23da7721d43bfa5a06cb2bc09214f3b9aecef257ee385d802c7f3a732

Name:		fcitx-skk
Version:	0.1.4
Release:	14%{?dist}
Summary:	Japanese SKK (Simple Kana Kanji) Engine for Fcitx

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	fcitx-devel, fcitx-qt5-devel, qt5-qtbase-devel, libskk-devel
BuildRequires:	cmake, gettext, intltool
Requires:	fcitx
Requires:	skkdic

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

%files -f %{name}.lang
%doc COPYING
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/libfcitx-skk-config.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/skk.conf
%{_datadir}/fcitx/skk/
%{_datadir}/fcitx/imicon/skk.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
%autochangelog
