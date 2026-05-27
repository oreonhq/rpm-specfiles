%global source0_hash 67ac509adffb1d2b256a8f8c0523e00761d960166192c6070298f7088a9ae9c9

Name:		perl-Test-CPAN-Meta-JSON
Version:	0.16
Release:	32%{?dist}
Summary:	Validate a META.json file within a CPAN distribution
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-CPAN-Meta-YAML
Source0:	https://cpan.metacpan.org/authors/id/B/BA/BARBIE/Test-CPAN-Meta-JSON-0.16.tar.gz

Patch0:		Test-CPAN-Meta-JSON-0.16-utf8.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(IO::File)
BuildRequires:	perl(JSON) >= 2.15
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 0.08
# Dependencies
# (none)

%description
This module was written to ensure that a META.json file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of ExtUtils::MakeMaker,
Module::Build and Module::Install.

See CPAN::Meta for further details of the CPAN Meta Specification.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test-CPAN-Meta-JSON-%{version}

# Recode LICENSE as UTF-8
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test AUTOMATED_TESTING=1

%files
%license LICENSE
%doc Changes README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CPAN::Meta::JSON.3*
%{_mandir}/man3/Test::CPAN::Meta::JSON::Version.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-32
- Prepare for Oreon 11 (RP1)
