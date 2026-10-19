%global source0_hash a5e0b1b1ba8fc5d6ed8778695a0ef092d8cd6fcd82662fb122adf2aedcff0626
%global gcalmantag 4
Name:		gcal
Version:	4.2.0
Release:        1%{?dist}
Summary:        GNU Gregorian calendar program
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/gcal/
Source0:        https://ftp.gnu.org/gnu/gcal/%{name}-%{version}.tar.xz
Source1:	gcal-man-v%{gcalmantag}.tar.xz
Patch:		gcal-glibc-no-libio.patch
Patch:		gcal-configure-c99.patch
Patch:		gcal-4.1-oob-write.patch
Patch:		gcal-configure-tget.patch
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Gcal is a program for calculating and printing calendars.  Gcal
displays hybrid and proleptic Julian and Gregorian calendar sheets.
It also displays holiday lists for many countries around the globe.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
tar xf %{SOURCE1}

%build

autoreconf -ifv
export LIBS=-lunistring
%configure --enable-unicode
%make_build
%check

make check
%install
%make_install
install -dm 755 %{buildroot}%{_mandir}/man1
install -pm 644 doc/en/man/*.1 %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_datadir}/%{name}/Makefile.in
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
