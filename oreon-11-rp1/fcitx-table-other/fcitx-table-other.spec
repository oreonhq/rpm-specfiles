%global source0_hash 18bae7020704b43d00b23a7b75a30753c88428042cfb1179d362166a320526b6
Name:		fcitx-table-other
Version:	0.2.4
Release:        1%{?dist}
Summary:        Other tables for Fcitx
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/fcitx-table-other/%{name}-%{version}.tar.xz
BuildArch:	noarch
Requires:	fcitx
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx
BuildRequires:  fcitx-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
