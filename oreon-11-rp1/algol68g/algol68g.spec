%global source0_hash b900ed9a92ef9b2548a6ac708ec81f724c59f2c089ed90f8e39a4e1287b28c1f
%ifarch %{ix86} x86_64 ia64 ppc64le
%bcond_without libquadmath
%else
%bcond_with libquadmath
%endif
Name: algol68g
Summary:        Algol 68 Genie compiler-interpreter
Version: 3.13.3
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://jmvdveer.home.xs4all.nl/en.algol-68-genie.html
Source0:        https://jmvdveer.home.xs4all.nl/%{name}-%{version}.tar.gz
%if %{with libquadmath}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libRmath)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  plotutils-devel
# /oreon:deps
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
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
