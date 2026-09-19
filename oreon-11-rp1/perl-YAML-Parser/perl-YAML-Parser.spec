%global source0_hash 12185d993c958e0cc509bf04145490722d8e3cce5a0b938e1bb24694e279a003

Name:           perl-YAML-Parser
Version:        0.0.5
Release:        11%{?dist}
Summary:        Generated Reference Parser for YAML 1.2
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML-Parser
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/YAML-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(boolean) >= 0.46
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON::PP) >= 4.05
BuildRequires:  perl(overload)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XXX) >= 0.35
BuildRequires:  perl(YAML::PP::Perl)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::More)

%description
YAML::Parser is the first 100% YAML 1.2 spec compliant parser for Perl. The
Perl code is generated directly from the YAML 1.2 specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n YAML-Parser-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
