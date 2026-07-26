%global source0_hash 721d06a5fff66e550b3f686ecb0ddf6232fddd41192eb7385420b24795e5fa1e

Name:           bygfoot
Version:        3.0.0
Release:        1%{?dist}
Summary:        Football management game
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.bygfoot.com
Source0:        https://gitlab.com/bygfoot/bygfoot/-/archive/%{version}/bygfoot-%{version}.tar.bz2
Source1:        bygfoot.desktop

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel gettext
BuildRequires:  ninja-build cmake
BuildRequires:  json-c-devel
BuildRequires:  sqlite-devel
Requires: bygfoot-data

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

%autosetup -n %{name}-%{version} -p1

%build
#This package requires -fcommon to build.
%global _legacy_common_support 1

# This package does not ship any object files or static libraries, so we
# don't need -ffat-lto-objects.
%if %{defined _lto_cflags}
%global _lto_cflags %(echo %{_lto_cflags} | sed 's/-ffat-lto-objects//')
%endif

%cmake -G Ninja -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install
%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO UPDATE
%license COPYING
%{_bindir}/bygfoot*
%{_datadir}/applications/bygfoot.desktop

%files data
%{_datadir}/bygfoot

%changelog
%autochangelog
