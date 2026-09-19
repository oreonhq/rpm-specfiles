%global source0_hash 3e2374788c292560911b3303a7b79ec169e5fca4946e9714ca139a8946fc9fbb

Name:           perl-SNMP-Info
%global cpan_version 3.975000
Version:        3.975.0
Release:        1%{?dist}
Summary:        Object Oriented Perl5 Interface to Network devices and MIBs through SNMP
License:        BSD-3-Clause
URL:            https://metacpan.org/release/SNMP-Info
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIVER/SNMP-Info-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Class::ISA not used at tests
# constant not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
# Module::Info not used at tests
# Module::Load not used at tests
# mro not used at tests
BuildRequires:  perl(NetAddr::IP) >= 4.068
BuildRequires:  perl(NetAddr::IP::Lite)
# PPI not used at tests
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SNMP)
BuildRequires:  perl(Socket)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
# File::Find not used
# Test::Distribution not used

Requires:       perl(mro)
Requires:       perl(NetAddr::IP) >= 4.068

%description
SNMP::Info gives an object oriented interface to information obtained
through SNMP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SNMP-Info-%{cpan_version}
find contrib -type f | xargs chmod -x 

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes contrib README
%{perl_vendorlib}/SNMP*
%{_mandir}/man3/SNMP::Info*

%changelog
%autochangelog
