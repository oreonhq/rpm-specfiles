%global source0_hash e750774b73b08e51148b963736d8207e50c3973e5456b6569cb7ad86831e0e59
Name:		fcitx-unikey
Version:	0.2.7
Release:        1%{?dist}
Summary:        Vietnamese Engine for Fcitx
License:	GPL-3.0-or-later
URL:		https://fcitx-im.org/wiki/Unikey
Source0:        http://download.fcitx-im.org/fcitx-unikey/%{name}-%{version}.tar.xz
Requires:	fcitx
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
