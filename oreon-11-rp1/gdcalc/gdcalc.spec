%global source0_hash c6d10a78e00c6d2d1f79771563fe1be6080d0d36e459451e1ab47dd935e7b4db
Summary:        Financial, statistics, scientific and programmers calculator for GTK+
Name: gdcalc
Version: 3.4
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://gitlab.com/wef/%{name}
Source0:        https://gitlab.com/wef/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires: units
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
gdcalc is a financial, statistics, scientific and programmers
calculator for gtk+-based under Unix and Linux.

It has both Algebraic notation (ie. conventional, TI or Casio-like)
and Reverse Polish Notation (HP-style).

To customise for fonts & colours:

mkdir ~/.config/%{name}
cp /etc/%{name}/%{name}.css ~/.config/%{name}/

This package includes the original dcalc for curses (Unix console)

If you want to know more about RPN calculators (and why they are more
intuitive than algebraic calculators with their = sign) take a look at
http://www.hpcalc.org

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
./autogen.sh

%build

%configure
%make_build
%install
%make_install
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
