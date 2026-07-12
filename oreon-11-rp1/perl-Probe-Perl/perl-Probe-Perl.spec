%global source0_hash d9e4d21e2e77638559045fa09046b1b6fff6c403b949929db213e30abe8a3c31

Name:           perl-Probe-Perl
Version:        0.03
Release:        34%{?dist}
Summary:        Information about the currently running perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Probe-Perl
Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Probe-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
# Tests:
# English not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

Provides:       perl(Probe::Perl)
Provides:       perl(Probe::Perl)
%description
This module provides methods for obtaining information about the currently
running perl interpreter. It originally began life as code in the
Module::Build project, but has been externalized here for general use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Probe-Perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
