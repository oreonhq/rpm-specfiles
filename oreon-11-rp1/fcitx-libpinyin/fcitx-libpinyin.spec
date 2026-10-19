%global source0_hash a848ea193304fad7afda2a5dbea8b1826dbe2559e478fc6298f333b97fb81c12
Name:		fcitx-libpinyin
Version:	0.5.4
Release:        1%{?dist}
Summary:        Libpinyin Wrapper for Fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Libpinyin
Source0:        http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz
Requires:	fcitx
ExclusiveArch: %{qt5_qtwebengine_arches}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  fcitx
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libpinyin-devel
BuildRequires:  libpinyin-tools
BuildRequires:  qt5-qtwebengine-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
