# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Test_CPAN_Meta_enables_optional_test
%else
%bcond_with perl_Test_CPAN_Meta_enables_optional_test
%endif

Name:           perl-Test-CPAN-Meta
Version:        0.25
Release:        40%{?dist}
Summary:        Validation of the META.yml file in a CPAN distribution
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-CPAN-Meta
Source0:        https://cpan.metacpan.org/authors/id/B/BA/BARBIE/Test-CPAN-Meta-0.25.tar.gz

Patch0:         Test-CPAN-Meta-0.25-utf8.patch
# oreon url source checksums begin
%global source0_sha256 f55b4f9cf6bc396d0fe8027267685cb2ac4affce897d0967a317fac6db5a8db5
%global source0_file Test-CPAN-Meta-0.25.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Parse::CPAN::Meta) >= 0.02
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More) >= 0.62
# Optional Tests
%if %{with perl_Test_CPAN_Meta_enables_optional_test} && !%{defined perl_bootstrap}
# Break build-cycle: perl-Test-CPAN-Meta → perl-Test-CPAN-Meta-JSON
# → perl-Test-CPAN-Meta
BuildRequires:  perl(Test::CPAN::Meta::JSON)
%endif
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
# Runtime

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as ExtUtils::MakeMaker, Module::Build and
Module::Install.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-CPAN-Meta-0.25.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f55b4f9cf6bc396d0fe8027267685cb2ac4affce897d0967a317fac6db5a8db5" || { echo "oreon: Source0 SHA256 mismatch for Test-CPAN-Meta-0.25.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Test-CPAN-Meta-%{version}

# Re-code documentation as UTF-8
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
%{_mandir}/man3/Test::CPAN::Meta.3*
%{_mandir}/man3/Test::CPAN::Meta::Version.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.25-40
- Prepare for Oreon 11 (RP1)
