%global source0_hash 721d06a5fff66e550b3f686ecb0ddf6232fddd41192eb7385420b24795e5fa1e
Name:           bygfoot
Version:        3.0.0
Release:        1%{?dist}
Summary:        Football management game
License:        GPL-2.0-only
URL:            http://www.bygfoot.com
Source0:        https://gitlab.com/bygfoot/bygfoot/-/archive/%{version}/bygfoot-%{version}.tar.bz2
Source1:        bygfoot.desktop
Requires: bygfoot-data
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  json-c-devel
BuildRequires:  ninja-build
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Bygfoot is a small and simple graphical football (a.k.a. soccer) manager game 
featuring many international leagues and cups. You manage a team from one such 
league: you form the team, buy and sell players, get promoted or relegated and
of course try to be successful.

%package data
Summary: bygfoot country definitions and other game files.
BuildArch:	noarch
%description data
bygfoot country definitions and other game files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%global _legacy_common_support 1
%if %{defined _lto_cflags}
%global _lto_cflags %(echo %{_lto_cflags} | sed 's/-ffat-lto-objects//')
%endif
%cmake -G Ninja -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles bygfoot-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bygfoot-data -f %{oreon_filedir}/bygfoot-data.list

%changelog

%autochangelog
