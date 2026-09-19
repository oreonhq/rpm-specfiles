%global source0_hash c91bb19c1a7b53c5339bf2f75ae83839020d337990f237a8b9bc0f4416c120ef

Name:		fcitx-table-extra
Version:	0.3.8
Release:	23%{?dist}
Summary:	Extra tables for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	cmake, fcitx-devel, gettext, intltool, libtool, fcitx
BuildArch:	noarch
Requires:	fcitx

%description
Fcitx-table-extra provides extra table for Fcitx, including Boshiamy, Zhengma,
and Cangjie 3/5.

Boshiamy table and its icon are released under their own license.

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
%doc AUTHORS COPYING
%{_datadir}/fcitx/table/*.mb
%{_datadir}/fcitx/table/*.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png

%changelog
%autochangelog
