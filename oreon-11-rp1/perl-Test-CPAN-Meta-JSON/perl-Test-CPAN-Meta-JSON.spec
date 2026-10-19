%global source0_hash 67ac509adffb1d2b256a8f8c0523e00761d960166192c6070298f7088a9ae9c9
Name:		perl-Test-CPAN-Meta-JSON
Version:	0.16
Release:        1%{?dist}
Summary:        Validate a META.json file within a CPAN distribution
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test-CPAN-Meta-YAML
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-CPAN-Meta-JSON-%{version}.tar.gz
Patch0:		Test-CPAN-Meta-JSON-0.16-utf8.patch
BuildArch:	noarch
Provides:       perl(Test::CPAN::Meta::JSON)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::CPAN::Meta)
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
This module was written to ensure that a META.json file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of ExtUtils::MakeMaker,
Module::Build and Module::Install.

See CPAN::Meta for further details of the CPAN Meta Specification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-32
- Prepare for Oreon 11 (RP1)
