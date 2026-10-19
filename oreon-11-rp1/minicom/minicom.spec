%global source0_hash b296b0e5795ca143fb1ffa78f46fd294daddfccd720faf9909a842d2f70c564e
Summary:        A text-based modem control and terminal emulation program
Name: minicom
Version: 2.11.1
Release:        1%{?dist}
URL: https://salsa.debian.org/minicom-team/minicom
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Source0:        https://salsa.debian.org/minicom-team/minicom/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires: lockdev lrzsz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  lockdev-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Minicom is a simple text-based modem control and terminal emulation
program somewhat similar to MSDOS Telix. Minicom includes a dialing
directory, full ANSI and VT100 emulation, an (external) scripting
language, and other features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am

cp -pr doc doc_
rm -f doc_/Makefile*

%build

autoreconf --verbose --force --install
rm -f lib/snprintf.c
%configure
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
