%global source0_hash 2ec25100cd76c620deec2d61876db44091d80910a79bb783ebe336aeaa0eed74

%ifarch %{ix86} x86_64 ia64 ppc64le
%bcond_without libquadmath
%else
%bcond_with libquadmath
%endif

Name: algol68g
Summary: Algol 68 Genie compiler-interpreter
Version: 3.11.0
Release: 1%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://jmvdveer.home.xs4all.nl/en.algol-68-genie.html
Source: https://jmvdveer.home.xs4all.nl/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(libRmath)
BuildRequires: pkgconfig(mpfr)
BuildRequires: pkgconfig(libpq)
%if %{with libquadmath}
BuildRequires: libquadmath-devel
%endif
BuildRequires: plotutils-devel

%description
Algol 68 Genie (Algol68G) is an Algol 68 compiler-interpreter.
It can be used for executing Algol 68 programs or scripts.
Algol 68 is a rather lean orthogonal general-purpose language
that is a beautiful means for denoting algorithms.
Algol 68 was designed as a general-purpose programming language
by IFIP Working Group 2.1 (Algorithmic Languages and Calculi)
that has continuing responsibility for Algol 60 and Algol 68.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%{_bindir}/a68g
%{_mandir}/man1/a68g.1*
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%exclude %{_includedir}
%exclude %{_pkgdocdir}/COPYING

%changelog
%autochangelog
