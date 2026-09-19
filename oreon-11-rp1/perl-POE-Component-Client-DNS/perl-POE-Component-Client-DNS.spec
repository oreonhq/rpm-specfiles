%global source0_hash b19a06920a69b74c2712bb5a48b719ce58965309d9beb3e2a35d8ff783625c31

Name:           perl-POE-Component-Client-DNS
Version:        1.054
Release:        30%{?dist}
Summary:        Non-blocking/concurrent DNS queries using Net::DNS and POE
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-DNS
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-DNS-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Net::DNS) >= 0.65
BuildRequires:  perl(POE) >= 1.294
BuildRequires:  perl(Socket)
# Tests only
BuildRequires:  perl(Data::Dumper)
%{?_with_network_tests:
BuildRequires:  perl(lib)
}
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings) >= 1.02
Requires:       perl(Net::DNS) >= 0.65
Requires:       perl(POE) >= 1.294

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
# the perldoc/pod documentation is nice, but I really found this much more
# useful.
cp t/01_resolve.t example_resolve

%check
%{?!_with_network_tests: rm t/0[1356]*.t }
make test

%files
%license LICENSE
%doc CHANGES README example_resolve
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
