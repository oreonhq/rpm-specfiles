%global source0_hash 6dd5fd5956924c85af92ebefaef1e113e38fa814355fbb0f07c26049c3014437

Name:		fcitx-hangul
Version:	0.3.1
Release:	24%{?dist}
Summary:	Hangul Engine for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Hangul
Source0:	http://download.fcitx-im.org/fcitx-hangul/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libhangul-devel
Requires:	fcitx

%description
Fcitx-hangul is a Hangul engine wrapper for Fcitx. It
Provides Korean input method from libhangul.

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
%doc COPYING AUTHORS README
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/hangul.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/imicon/hangul.png
%dir %{_datadir}/fcitx/hangul/
%{_datadir}/fcitx/hangul/symbol.txt
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/*/status/fcitx-hanja-active.png
%{_datadir}/icons/hicolor/*/status/fcitx-hanja-inactive.png

%changelog
%autochangelog
