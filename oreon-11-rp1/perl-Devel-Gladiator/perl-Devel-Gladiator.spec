%global source0_hash feeed75cabd7522e2d61831b65a0cce521b8f6f2661c7138c637f03718b566b6

Name:           perl-Devel-Gladiator
Version:        0.08
Release:        21%{?dist}
Summary:        Walk Perl's arena
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Gladiator
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Devel-Gladiator-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)

%description
Devel::Gladiator iterates Perl's internal memory structures and can be used to
enumerate all the currently live SVs. This can be used to hunt leaks and to
profile memory usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Gladiator-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
%autochangelog
