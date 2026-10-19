%global source0_hash 9b3e14e95a5b6aa0ee909b1d1e5c1fac04042024f29b66377cfb9e1923b25f5c
%global _docdir_fmt %{name}
Name:		gappa
Version:	1.8.3
Release:        1%{?dist}
Summary:        Prove programs with floating-point or fixed-point arithmetic
License:	GPL-3.0-only OR CECILL-2.1
URL:		https://gappa.gitlabpages.inria.fr/
VCS:		git:https://gitlab.inria.fr/gappa/gappa.git
Source0:        https://%{name}.gitlabpages.inria.fr//releases/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  python3dist(sphinx)
BuildRequires:  remake
# /oreon:deps
%description
Gappa is a tool intended to help verifying and formally prove
properties on numerical programs and circuits handling floating-point
or fixed-point arithmetic.  This tool manipulates logical formulas
stating the enclosures of expressions in some intervals.  Through the
use of rounding operators as part of the expressions, Gappa is specially
designed to deal with formulas that could appear when certifying numerical
codes. In particular, Gappa makes it simple to bound computational errors
due to floating-point arithmetic.  The tool and its documentation were
written by Guillaume Melquiond.

%package doc
Summary:	Documentation for gappa
BuildArch:	noarch
License:	(GPL-3.0-only OR CECILL-2.1) AND MIT AND BSD-2-Clause AND BSD-3-Clause
%description doc
Documentation for gappa.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
# Increase the test timeout for ARM
sed -i 's/timeout 5/&0/' Remakefile.in

%build

%configure
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags}
remake -d doc/html/index.html
rm doc/html/.buildinfo
%install
DESTDIR=%{buildroot} remake install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

remake check
%files -f %{oreon_filedir}/main.list
%files -n gappa-doc -f %{oreon_filedir}/gappa-doc.list

%changelog

%autochangelog
