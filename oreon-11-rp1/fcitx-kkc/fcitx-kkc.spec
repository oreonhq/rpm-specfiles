%global source0_hash f19b447e2faac2b1ca71864688a6fc73deee68d824d399a28aea230b2ec25c17

Name:		fcitx-kkc
Version:	0.1.4
Release:	14%{?dist}
Summary:	Japanese Kana Kanji Engine for Fcitx

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/fcitx-kkc/%{name}-%{version}.tar.xz

BuildRequires:	fcitx-devel, fcitx-qt5-devel, qt5-qtbase-devel, libkkc-devel
BuildRequires:	cmake, gettext, intltool
Requires:	fcitx

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

%files -f %{name}.lang
%doc
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/libfcitx-kkc-config.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/kkc.conf
%{_datadir}/fcitx/kkc/
%{_datadir}/fcitx/imicon/kkc.png
%{_datadir}/icons/hicolor/64x64/apps/fcitx-kkc.png

%changelog
%autochangelog
