%global source0_hash 33f5c474fb7cb57a7bf0005b20fde901cf6b5813e306c9370ae4263d3ffabc60

Name:		perl-Test-CPAN-Meta-YAML
Version:	0.25
Release:	32%{?dist}
Summary:	Validate a META.yml file within a CPAN distribution
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-CPAN-Meta-YAML
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-CPAN-Meta-YAML-%{version}.tar.gz
Patch0:		Test-CPAN-Meta-YAML-0.25-utf8.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::YAML::Valid) >= 0.03
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(YAML::Syck)
# Test Suite
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
# Optional Tests
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 0.08
# Dependencies
# Explicitly requests the YAML::Syck backend for Test::YAML::Valid
Requires:	perl(YAML::Syck)

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of ExtUtils::MakeMaker,
Module::Build and Module::Install.

See CPAN::Meta for further details of the CPAN Meta Specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-CPAN-Meta-YAML-%{version}

# Recode documentation as UTF-8
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
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CPAN::Meta::YAML.3*
%{_mandir}/man3/Test::CPAN::Meta::YAML::Version.3*

%changelog
%autochangelog
