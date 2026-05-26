Name:           perl-Module-Install-ManifestSkip
Version:        0.24
Release:        33%{?dist}
Summary:        Generate a MANIFEST.SKIP file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-ManifestSkip
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Install-ManifestSkip-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 32320ee5e2841322a20905cde82288d582703726f95b3ee0957c0862f937ee7d
%global source0_file Module-Install-ManifestSkip-0.24.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-Install-ManifestSkip-0.24.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "32320ee5e2841322a20905cde82288d582703726f95b3ee0957c0862f937ee7d" || { echo "oreon: Source0 SHA256 mismatch for Module-Install-ManifestSkip-0.24.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
