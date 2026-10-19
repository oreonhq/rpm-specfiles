%global source0_hash f55b4f9cf6bc396d0fe8027267685cb2ac4affce897d0967a317fac6db5a8db5
%bcond_with perl_Test_CPAN_Meta_enables_optional_test
Name:           perl-Test-CPAN-Meta
Version:        0.25
Release:        1%{?dist}
Summary:        Validation of the META.yml file in a CPAN distribution
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-CPAN-Meta
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-CPAN-Meta-%{version}.tar.gz
Patch0:         Test-CPAN-Meta-0.25-utf8.patch
BuildArch:      noarch
%if %{with perl_Test_CPAN_Meta_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Provides:       perl(Test::CPAN::Meta)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as ExtUtils::MakeMaker, Module::Build and
Module::Install.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.25-40
- Prepare for Oreon 11 (RP1)
