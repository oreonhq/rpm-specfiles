%global source2_hash 5bb2f1a372c841621d2269ba4a3f5d9ddd3c2804523fdcf41ea65c4e9a65a63e
%global source0_hash da2f062de8d4796cd48daf193e4202f05be204ad95b4a4e3f4faafa5504ce05d
%global public_key RWRzJFnXiLZleAyCIv1talBjyRewelcy9gzYQq9pd3SKSFBPoy57sf5s
Name:           ibus-chewing
Version:        2.2.0
Release:        1%{?dist}
Summary:        The Chewing engine for IBus input platform
Summary(zh_TW): IBus新酷音輸入法
License:        GPL-2.0-or-later
URL:            https://github.com/chewing/ibus-chewing
Source0:        https://github.com/chewing/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://chewing.im/.well-known/openpgpkey/hu/y84sdmnksfqswe7fxf5mzjg53tbdz8f5?l=release#/libchewing.pgp
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-runtime
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(chewing)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
# /oreon:deps
%description
IBus-chewing is an IBus front-end of Chewing, an intelligent Chinese input
method for Zhuyin (BoPoMoFo) users.
It supports various Zhuyin keyboard layout, such as standard (DaChen),
IBM, Gin-Yeah, Eten, Eten 26, Hsu, Dvorak, Dvorak-Hsu, and DaChen26.

Chewing also support toned Hanyu pinyin input.

%description -l zh_TW
IBus-chewing 是新酷音輸入法的IBus前端。
新酷音輸入法是個智慧型注音輸入法，支援多種鍵盤布局，諸如：
標準注音鍵盤、IBM、精業、倚天、倚天26鍵、許氏、Dvorak、Dvorak許氏
及大千26鍵。

本輸入法也同時支援帶調漢語拼音輸入。

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}

%build

%meson
%meson_build
%install
%meson_install
rm -fr %{buildroot}%{_docdir}/*
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
