%global source0_hash a097f75a7eeadb33705f9d8871ca9c026efeaf6c30490017fbb2e1b1f921232a
Name:		fcitx-cloudpinyin
Version:	0.3.7
Release:        1%{?dist}
Summary:        Cloudpinyin module for fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Cloudpinyin
Source0:        http://download.fcitx-im.org/fcitx-cloudpinyin/%{name}-%{version}.tar.xz
Requires:	fcitx, fcitx-pinyin
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
Cloudpinyin is Fcitx addon that will add one candidate word to your pinyin
list. It current support four provider, Sogou, QQ, Baidu, Google.

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
