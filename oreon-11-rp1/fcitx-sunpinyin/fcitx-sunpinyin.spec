%global source0_hash 0bf2d72d77732f06e7f04c119507c08b9618b21c4027e3997186bd7e4d0788c4

Name:			fcitx-sunpinyin
Version:		0.4.2
Release:		24%{?dist}
Summary:		Sunpinyin Wrapper for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:		GPL-2.0-or-later
URL:			http://fcitx-im.org/wiki/Fcitx
Source0:		http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	fcitx-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	sunpinyin-devel
BuildRequires:	dbus-devel
BuildRequires:	libtool
BuildRequires:	sunpinyin
BuildRequires:	fcitx
Requires:		fcitx
Requires:		fcitx-data
Requires:		sunpinyin-data

%description
Fcitx-sunpinyin is a Sunpinyin Wrapper for Fcitx.

SunPinyin is an SLM (Statistical Language Model) based input method
engine. To model the Chinese language, it use a backoff bigram and
trigram language model.

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
%doc AUTHORS README
%license COPYING
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/sunpinyin.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/fcitx/skin/classic/sunpinyin.png
%{_datadir}/fcitx/skin/dark/sunpinyin.png
%{_datadir}/fcitx/skin/default/sunpinyin.png
%{_datadir}/fcitx/imicon/sunpinyin.png

%changelog
%autochangelog
