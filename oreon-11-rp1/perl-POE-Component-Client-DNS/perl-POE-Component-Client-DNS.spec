%global source0_hash b19a06920a69b74c2712bb5a48b719ce58965309d9beb3e2a35d8ff783625c31
Name:           perl-POE-Component-Client-DNS
Version:        1.054
Release:        30%{?dist}
Summary:        Non-blocking/concurrent DNS queries using Net::DNS and POE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-DNS
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-DNS-%{version}.tar.gz
BuildArch:      noarch
%{?_with_network_tests:
}
Requires:       perl(Net::DNS) >= 0.65
Requires:       perl(POE) >= 1.294
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(POE)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POE::Component::Client::DNS provides a facility for non-blocking, concurrent
DNS requests. Using POE, it allows other tasks to run while waiting for name
servers to respond.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-DNS-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
cp t/01_resolve.t example_resolve
%oreon_autofiles main

%check

%{?!_with_network_tests: rm t/0[1356]*.t }
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
