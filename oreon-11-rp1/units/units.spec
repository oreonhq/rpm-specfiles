%global source0_hash e1bbdb09672e7c08eee986749e7a1629eb84a6bdf41f5a2a79d6804444abbe10
Summary:        A utility for converting amounts from one unit to another
Name: units
Version: 2.27
Release:        1%{?dist}
Source0:        https://mirrors.kernel.org/gnu/units/%{name}-%{version}.tar.gz
URL: https://www.gnu.org/software/units/units.html
License: GPL-3.0-or-later
Requires: less
Patch100: 0100-units-2.22-no-network.patch
Patch101: 0101-fix-make-less-default-pager.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another. The units program can handle multiplicative scale changes as 
well as conversions such as Fahrenheit to Celsius.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure CFLAGS="$RPM_OPT_FLAGS -std=c17"
%make_build
%install
%make_install
ln -fsv ../../..%{_sharedstatedir}/units/currency.units %{buildroot}%{_datadir}/units
gzip %{buildroot}%{_infodir}/units.info
ln -s units.1 %{buildroot}%{_mandir}/man1/units_cur.1
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.26-1
- Prepare for Oreon 11 (RP1)
