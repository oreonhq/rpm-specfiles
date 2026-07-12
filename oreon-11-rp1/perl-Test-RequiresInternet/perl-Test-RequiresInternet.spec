%global source0_hash bba7b32a1cc0d58ce2ec20b200a7347c69631641e8cae8ff4567ad24ef1e833e

Name:		perl-Test-RequiresInternet
Version:	0.05
Release:	32%{?dist}
Summary:	Easily test network connectivity
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-RequiresInternet
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-RequiresInternet-%{version}.tar.gz



BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Socket)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
# (none)

Provides:       perl(Test::RequiresInternet)
%description
This module is intended to easily test network connectivity before functional
tests begin to non-local Internet resources. It does not require any modules
beyond those supplied in core Perl.

If you do not specify a host/port pair, then the module defaults to using
www.google.com on port 80. You may optionally specify the port by its name, as
in http or ldap. If you do this, the test module will attempt to look up the
port number using getservbyname. If you do specify a host and port, they must
be specified in pairs. It is a fatal error to omit one or the other.

If the environment variable NO_NETWORK_TESTING is set, then the tests will be
skipped without attempting any socket connections.

If the sockets cannot connect to the specified hosts and ports, the exception
is caught, reported and the tests skipped.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-RequiresInternet-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::RequiresInternet.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.05-32
- Prepare for Oreon 11 (RP1)
