%global source0_hash 1bbc8893da69f2502483d9e5e2556494b2589d7595729a79c63689c6e1b17a87

Name:           perl-Data-Dumper-Names
Version:        0.03
Release:        49%{?dist}
Summary:        Data::Dumper like module for printing and eval data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Dumper-Names
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/Data-Dumper-Names-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(PadWalker) >= 0.13
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(PadWalker) >= 0.13

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PadWalker\\)$

Provides:       perl(Data::Dumper::Names)
%description
The essential module Data::Dumper is used for printing perl data structures or 
suitable for eval. Data::Dumper::Names dump variables with names and without
source filter. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Dumper-Names-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Avoid annoying noise from TAP::Parser::SourceHandler::Perl version 3.28 (CPAN RT#85106)
# (as found in EL-7 beta)
export PERL5LIB="$(pwd)/no-such-directory"

./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
