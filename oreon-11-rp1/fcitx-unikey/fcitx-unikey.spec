%global source0_hash e750774b73b08e51148b963736d8207e50c3973e5456b6569cb7ad86831e0e59

Name:		fcitx-unikey
Version:	0.2.7
Release:	23%{?dist}
Summary:	Vietnamese Engine for Fcitx
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Unikey
Source0:	http://download.fcitx-im.org/fcitx-unikey/%{name}-%{version}.tar.xz

BuildRequires:	cmake, fcitx-devel, gettext, intltool
BuildRequires:	fcitx-qt5-devel qt5-qtbase-devel
Requires:	fcitx

%description
A Vietnamese engine for Fcitx that uses Unikey.

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
%doc ChangeLog COPYING README
%{_libdir}/fcitx/qt/*.so
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/unikey.conf
%{_datadir}/fcitx/configdesc/fcitx-unikey.desc
%{_datadir}/fcitx/imicon/unikey.png
%{_datadir}/icons/hicolor/256x256/apps/fcitx-unikey.png

%changelog
%autochangelog
