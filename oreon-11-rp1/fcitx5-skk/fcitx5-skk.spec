%global source0_hash 990b9b3d31e98464e5429a43a88d0650f24a11aa49e9c15199760a7f6f7b9be5

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:       fcitx5-skk
Version:    5.1.9
Release:    %autorelease
Summary:    Japanese SKK (Simple Kana Kanji) Engine for Fcitx5
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://github.com/fcitx/fcitx5-skk
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-qt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(libskk)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  /usr/bin/appstream-util
Requires:       skkdic
Requires:       hicolor-icon-theme
Requires:       fcitx5-data

%description
Fcitx5-skk is an SKK (Simple Kana Kanji) engine for Fcitx.  It provides
Japanese input method using libskk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -DCMAKE_CXX_STANDARD=17 -GNinja
%cmake_build

%install
%cmake_install
# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md
%{_libdir}/fcitx5/qt6/libfcitx5-skk-config.so
%{_libdir}/fcitx5/skk.so
%{_datadir}/fcitx5/addon/skk.conf
%{_datadir}/fcitx5/inputmethod/skk.conf
%dir %{_datadir}/fcitx5/skk
%{_datadir}/fcitx5/skk/dictionary_list
%{_datadir}/icons/hicolor/*/apps/fcitx_skk.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_skk.png
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
%autochangelog
