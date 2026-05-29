%global source0_hash none

Summary: A utility for converting amounts from one unit to another
Name: units
Version: 2.26
Release: 1%{?dist}
Source:        https://ftp.gnu.org/gnu/units/units-2.26.tar.gz
URL: https://www.gnu.org/software/units/units.html
License: GPL-3.0-or-later

Requires: less

BuildRequires: bison
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: python3-devel
BuildRequires: readline-devel

# do not update currency.units from network during build
Patch100: 0100-units-2.22-no-network.patch

# make less a default pager to avoid error about missing /usr/bin/pager
Patch101: 0101-fix-make-less-default-pager.patch

%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another. The units program can handle multiplicative scale changes as 
well as conversions such as Fahrenheit to Celsius.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
# Use C17 standard to avoid compilation errors
# We will revert this change once the upstream adopts the latest C standard
%configure CFLAGS="$RPM_OPT_FLAGS -std=c17"
%make_build

%install
%make_install

# replace an absolute symlink by a relative symlink
ln -fsv ../../..%{_sharedstatedir}/units/currency.units %{buildroot}%{_datadir}/units

gzip %{buildroot}%{_infodir}/units.info

# provide a man page for units_cur as a symlink to units.1
ln -s units.1 %{buildroot}%{_mandir}/man1/units_cur.1

%check
make check

%files
%doc COPYING NEWS README
%{_bindir}/units
%{_bindir}/units_cur
%{_datadir}/units
%{_sharedstatedir}/units
%{_infodir}/*
%{_mandir}/man1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.26-1
- Prepare for Oreon 11 (RP1)
