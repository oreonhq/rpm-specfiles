%global source0_hash f19b447e2faac2b1ca71864688a6fc73deee68d824d399a28aea230b2ec25c17
Name:		fcitx-kkc
Version:	0.1.4
Release:        1%{?dist}
Summary:        Japanese Kana Kanji Engine for Fcitx
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/fcitx-kkc/%{name}-%{version}.tar.xz
Requires:	fcitx
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libkkc-devel
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
Fcitx-kkc is a Kana Kanji engine for Fcitx.  It provides Japanese
input method using libkkc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
rm -f $RPM_BUILD_ROOT%{_includedir}/fcitx/module/kkc/fcitx-kkc.h
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
