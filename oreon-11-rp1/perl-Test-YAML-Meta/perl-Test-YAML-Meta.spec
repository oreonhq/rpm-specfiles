%global source0_hash 0e7a3ba51d87596a97e389edc4b1a0685d0dac52d859ef3825244015462d80d7

Name:           perl-Test-YAML-Meta
Version:        0.22
Release:        33%{?dist}
Summary:        Validation of the META.yml file in a distribution
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-YAML-Meta
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-YAML-Meta-%{version}.tar.gz
Patch0:         Test-YAML-Meta-0.21-utf8.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::CPAN::Meta::YAML) >= 0.17
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
# Runtime

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of
ExtUtils::MakeMaker, Module::Build and Module::Install.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-YAML-Meta-%{version}

# Re-code LICENSE as UTF-8
%patch -P0

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
%{_mandir}/man3/Test::YAML::Meta.3*

%changelog
%autochangelog
