%global source0_hash 94d2fa4a743885ca9cea9f7042d9e7a3a69f5bd7cc18aa630c7f7f5e8ae36944

Name:           perl-Lexical-Persistence
Version:        1.023
Release:        31%{?dist}
Summary:        Persistent lexical variable values for arbitrary calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lexical-Persistence
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/Lexical-Persistence-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(PadWalker)
# Tests only
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.94

%description
Lexical::Persistence does a few things, all related. Note that all the
behaviors listed here are the defaults. Subclasses can override nearly
every aspect of Lexical::Persistence's behavior.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lexical-Persistence-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc CHANGES README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
