%global source0_hash bc4865d29525940a5cf571cb7f38e8430316e47d4c10085f227d20fbf41d904c

Name:       perl-Check-ISA
Version:    0.09
Release:    27%{?dist}
# see lib/Check/ISA.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    DWIM, correct checking of an object's class
Source:     https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Check-ISA-%{version}.tar.gz
Url:        https://metacpan.org/release/Check-ISA
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time
BuildRequires: perl(constant)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(warnings::register)
# Tests
BuildRequires: perl(base)
BuildRequires: perl(ok)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::use::ok)
# Optional tests
BuildRequires: perl(asa)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
Requires:      perl(IO::Handle)

%description
This module provides several functions to assist in testing whether a value
is an object, and if so, ask about its class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Check-ISA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
