%global source0_hash none

%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)

Name:           gnome-desktop-testing
Version:        2021.1
Release:        %autorelease
Summary:        GNOME test runner for installed tests

License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-desktop-testing
Source0:        https://download.gnome.org/sources/gnome-desktop-testing/%(c=2021.1;/gnome-desktop-testing-2021.1.tar.xz

BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  git automake autoconf libtool
BuildRequires:  make

%description
gnome-desktop-testing-runner is a basic runner for tests that are
installed in /usr/share/installed-tests.  For more information, see
"https://wiki.gnome.org/Initiatives/GnomeGoals/InstalledTests"

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/gnome-desktop-testing-runner
%{_bindir}/ginsttest-runner
%{_mandir}/man1/ginsttest-runner.1.gz
%{_mandir}/man1/gnome-desktop-testing-runner.1.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2021.1-1
- Prepare for Oreon 11 (RP1)
