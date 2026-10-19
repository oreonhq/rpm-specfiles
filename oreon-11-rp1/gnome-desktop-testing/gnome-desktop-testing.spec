%global source0_hash 4818d22bdeccb6b58cf22770f2e388e14225c224987563c67c9ac0773b37c165
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)
Name:           gnome-desktop-testing
Version:        2021.1
Release:        1%{?dist}
Summary:        GNOME test runner for installed tests
License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-desktop-testing
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsystemd)
# /oreon:deps
%description
gnome-desktop-testing-runner is a basic runner for tests that are
installed in /usr/share/installed-tests.  For more information, see
"https://wiki.gnome.org/Initiatives/GnomeGoals/InstalledTests"

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2021.1-1
- Prepare for Oreon 11 (RP1)
