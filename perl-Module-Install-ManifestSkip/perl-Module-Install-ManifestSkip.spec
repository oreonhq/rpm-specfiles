Name:           perl-Module-Install-ManifestSkip
Version:        0.24
Release:        33%{?dist}
Summary:        Generate a MANIFEST.SKIP file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-ManifestSkip
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Install-ManifestSkip-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Base)
# Module::Manifest::Skip 0.18 not used at test-time
# Tests:
# inc::Module::Install not used, the t/sample1 is used by xt tests only
BuildRequires:  perl(Test::More)
Requires:       perl(Module::Manifest::Skip) >= 0.18
Requires:       perl(warnings)

%description
This module generates a MANIFEST.SKIP file for you (using
Module::Manifest::Skip) that contains the common files that people do not
want in their MANIFEST files. The SKIP file is generated each time that you
(the module author) run Makefile.PL.

%prep
%setup -q -n Module-Install-ManifestSkip-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24-33
- Prepare for Oreon 11 (RP1)
