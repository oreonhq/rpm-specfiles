%global source0_hash c6d10a78e00c6d2d1f79771563fe1be6080d0d36e459451e1ab47dd935e7b4db

Summary: Financial, statistics, scientific and programmers calculator for GTK+
Name: gdcalc
Version: 3.4
Release: 8%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://gitlab.com/wef/%{name}
Source: %{url}/-/archive/%version/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: bison
BuildRequires: ncurses-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: autoconf, automake, libtool
BuildRequires: desktop-file-utils

Requires: units
Requires: hicolor-icon-theme

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

%files
%license COPYING
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%config(noreplace) %{_sysconfdir}/%{name}/

%doc README.md doc/manual_en.html
%{_mandir}/man1/*.1*

%changelog
%autochangelog
