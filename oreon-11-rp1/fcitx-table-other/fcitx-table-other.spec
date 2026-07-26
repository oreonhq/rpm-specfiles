%global source0_hash 18bae7020704b43d00b23a7b75a30753c88428042cfb1179d362166a320526b6

Name:		fcitx-table-other
Version:	0.2.4
Release:	23%{?dist}
Summary:	Other tables for Fcitx
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/fcitx-table-other/%{name}-%{version}.tar.xz

BuildRequires:	cmake, fcitx-devel, gettext, intltool, libtool, fcitx
BuildArch:	noarch
Requires:	fcitx

%description
Fcitx-table-other is a fork of ibus-table-others for Fcitx,
provides additional tables.

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
%doc AUTHORS COPYING README
%{_datadir}/fcitx/table/*.mb
%{_datadir}/fcitx/table/*.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png

%changelog
%autochangelog
