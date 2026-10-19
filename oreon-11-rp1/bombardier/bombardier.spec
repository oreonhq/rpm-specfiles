%global source0_hash 5235d302168ae10197e9ff693bc3a15dc63eab9519104c4edbbab9d3adde36d6
Name: bombardier
Version: 0.8.8
Release:        1%{?dist}
Summary:        The GNU Bombing utility
License: GPL-2.0-or-later        
URL: http://packages.debian.org/stable/source/bombardier
Source0:        http://http.debian.net/debian/pool/main/b/bombardier/bombardier_%{version}.tar.xz
Source1: bombardier.desktop
Source2: bombardier-logo.png
Patch0: bombardier-height.patch
Patch1: bombardier-0.8.2-string-format.patch
Patch2: format.patch
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Fly an ncurses plane over an ncurses city, and try to level the buildings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn bombardier

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build

make CFLAGS="$RPM_OPT_FLAGS"
%install
install -pD -m 755 bombardier %{buildroot}%{_bindir}/bombardier
install -pD -m 644 bombardier.6 %{buildroot}%{_mandir}/man6/bombardier.6
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install            \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
