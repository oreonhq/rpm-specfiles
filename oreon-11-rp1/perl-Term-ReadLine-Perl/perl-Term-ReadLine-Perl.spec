%global source0_hash 314b9f8df7e89e77eaac200b9bbcbe28e01e0dab2646ada83c5b26584839095d

Name:           perl-Term-ReadLine-Perl
Version:        1.0303
Release:        41%{?dist}
Summary:        Readline implementation in Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ReadLine-Perl
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILYAZ/modules/Term-ReadLine-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Term::Cap is optional
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(SelfLoader)
BuildRequires:  perl(Term::ReadKey)
# Tests:
BuildRequires:  perl(Term::ReadLine)
Requires:       perl(Term::ReadKey)

%description
This is a quick implementation of the minimal interface to Readline libraries.
The implementation is made in Perl (mostly) by Jeffrey Friedl. The only thing
this library does is to make it conformant (and add some minimal changes, like
using Term::ReadKey if present, and correct work under xterm).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-ReadLine-Perl-%{version}
chmod -x ReadLine/*.pm CHANGES README

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Disable interractive tests
AUTOMATED_TESTING=1 make test

%files
%doc CHANGES README
%{perl_vendorlib}/*

%changelog
%autochangelog
