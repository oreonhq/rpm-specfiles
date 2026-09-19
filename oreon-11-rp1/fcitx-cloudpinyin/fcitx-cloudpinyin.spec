%global source0_hash a097f75a7eeadb33705f9d8871ca9c026efeaf6c30490017fbb2e1b1f921232a

Name:		fcitx-cloudpinyin
Version:	0.3.7
Release:	18%{?dist}
Summary:	Cloudpinyin module for fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Cloudpinyin
Source0:	http://download.fcitx-im.org/fcitx-cloudpinyin/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libcurl-devel, pkgconfig
Requires:	fcitx, fcitx-pinyin

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

%files -f %{name}.lang
%doc README COPYING 
%{_datadir}/fcitx/configdesc/*.desc
%{_datadir}/fcitx/addon/*.conf
%{_libdir}/fcitx/*.so

%changelog
%autochangelog
