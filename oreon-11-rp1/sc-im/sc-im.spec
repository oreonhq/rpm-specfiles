%global source0_hash 49adb76fc55bc3e6ea8ee414f41428db4aef947e247718d9210be8d14a6524bd
Name:           sc-im
Version:        0.8.5
Release:        1%{?dist}
Summary:        Spreadsheet Calculator Improvised, ncurses based vim-like spreadsheet calculator
License:        BSD-4-Clause
URL:            https://github.com/andmarti1424/sc-im
Source0:        https://github.com/andmarti1424/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Recommends:     gnuplot
Recommends:     xclip
# oreon:deps
BuildRequires:  /usr/bin/pkg-config
BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libxls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(ncursesw)
# /oreon:deps
%description
Spreadsheet Calculator Improvised, aka sc-im, is an ncurses based, vim-like
spreadsheet calculator. sc-im is based on sc, whose original authors are James
Gosling and Mark Weiser, and mods were later added by Chuck Martin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sc-im-%{version}
%oreon_prep
%build

%make_build -C src/ prefix=%{_prefix}
%install
%make_install -C src/ prefix=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
