%global source0_hash a848ea193304fad7afda2a5dbea8b1826dbe2559e478fc6298f333b97fb81c12

Name:		fcitx-libpinyin
Version:	0.5.4
Release:	14%{?dist}
Summary:	Libpinyin Wrapper for Fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Libpinyin
Source0:	http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz

BuildRequires:	gcc
BuildRequires:	libpinyin-devel >= 1.9.91
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libpinyin-devel
BuildRequires:	libpinyin-tools, glib2-devel, fcitx
BuildRequires:	qt5-qtwebengine-devel, dbus-devel
BuildRequires:	fcitx-qt5-devel >= 1.1
Requires:	fcitx
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
Fcitx-libpinyin is a libpinyin Wrapper for Fcitx.

Libpinyin is a Frontend of the Intelligent Pinyin IME Backend.

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
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/*.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/imicon/*
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/*-libpinyin.conf
%{_datadir}/fcitx/libpinyin/
%{_datadir}/icons/hicolor/48x48/status/fcitx-*.png

%changelog
%autochangelog
