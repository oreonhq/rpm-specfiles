%global source0_hash c91bb19c1a7b53c5339bf2f75ae83839020d337990f237a8b9bc0f4416c120ef
Name:		fcitx-table-extra
Version:	0.3.8
Release:        1%{?dist}
Summary:        Extra tables for Fcitx
License:	GPL-2.0-or-later
URL:		http://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
