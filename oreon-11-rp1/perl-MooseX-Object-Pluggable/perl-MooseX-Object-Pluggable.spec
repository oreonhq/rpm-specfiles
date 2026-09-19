%global source0_hash f3bf7cbbe83f59c2111463e0c7dc8e69fa53fb3a8903f36f36d3f886cc3e64e0

Name:           perl-MooseX-Object-Pluggable
Version:        0.0014
Release:        33%{?dist}
Summary:        Make your Moose classes pluggable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Object-Pluggable
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Object-Pluggable-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module::Build::Tiny is not helpful
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Try::Tiny)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose) >= 0.35
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)

%{?perl_default_filter}

%description
This module aids in the development and deployment of plugin-enabled
Moose-based classes. It extends the Moose framework via roles to enable
this behavior.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Object-Pluggable-%{version}
perl -MConfig -pi -e 's|^#!perl|$Config{startperl}|' t/00-report-prereqs.t

%build
PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 </dev/null
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
