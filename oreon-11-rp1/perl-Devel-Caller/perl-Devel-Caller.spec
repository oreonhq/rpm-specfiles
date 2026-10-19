%global source0_hash b679a2b18034b0b720de82c3708724c364b10a6ca164cbc67cdc3af283f3503f
Name:           perl-Devel-Caller
Version:        2.07
Release:        1%{?dist}
Summary:        Meatier versions of caller
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Caller
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Caller-%{version}.tar.gz
Requires:       perl(PadWalker) >= 0.08
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(DB\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PadWalker\\)$
Provides:       perl(Devel::Caller)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Devel::Caller - Meatier versions of caller.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-Caller-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.07-11
- Prepare for Oreon 11 (RP1)
