%global source0_hash 6bd5d1469e161e199a9bd7fdde957e04176c5707cb059597a23ca3e130fb1134
Name:           perl-lexical-underscore
Version:        0.004
Release:        1%{?dist}
Summary:        Access your caller's lexical underscore
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/lexical-underscore
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/lexical-underscore-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Starting with Perl 5.10, it is possible to create a lexical version of the
Perl default variable $_.

It is occasionally useful for a subroutine to be able to access its caller's
$_ variable regardless of whether it was lexical or not. The "(_)" sub
prototype is the official way to do so, however there are sometimes
disadvantages to this.

The "lexical::underscore" function returns a scalar reference to either
a lexical $_ variable somewhere up the call stack (using PadWalker magic), or
to the global $_ if there was no lexical version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lexical-underscore-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
