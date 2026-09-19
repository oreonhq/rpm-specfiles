%global source0_hash 744a88cc6b98a4625ae5c5ee819640561f3df87518be0f9fca00ad787814b200

Name: neo
Summary: Digital rain in your terminal

# README.md says "GNU GPL v3", but license headers in source files
# and the --version option say "version 3 or later". 
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later

Version: 0.6.1
Release: 12%{?dist}

URL: https://github.com/st3w/neo
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# When the program is invoked with the --version option,
# the printed text contains the date of the build,
# which makes builds non-reproducible.
# This patch removes the build-date information.
Patch0: %{name}--reproducible-build.patch

BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(ncurses)

%description
%{name} recreates the digital rain effect known from the film "The Matrix".
Streams of random characters will endlessly scroll down your terminal screen.

%{name} handles Unicode, 16/256 and 32-bit color. It has automatic detection
for terminal color, and supports resizing gracefully.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc doc/NEWS
%license doc/COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
