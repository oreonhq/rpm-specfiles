%global source0_hash decb05e614d0f7f85281a55e03580a100cce80dac09dc9bd77a6f59e7ed8230d

Name:           perl-Text-WagnerFischer
Version:        0.04
Release:        %autorelease
Summary:        Perl implementation of the Wagner-Fischer edit distance

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-WagnerFischer
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDEBE/Text-WagnerFischer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
Perl implementation of the Wagner-Fischer edit distance algorithm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-WagnerFischer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Text/WagnerFischer.pm
%{_mandir}/man3/Text::WagnerFischer.3*

%changelog
%autochangelog
