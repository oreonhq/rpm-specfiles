%global source0_hash d0ea851c02eb27003d8242547837552539ff61d4f087028cdead0076fbbd463a

Name:           perl-Module-CPANTS-Analyse
Version:        1.03
Release:        1%{?dist}
Summary:        Generate Kwalitee ratings for a distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-CPANTS-Analyse
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-CPANTS-Analyse-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.08
# Module Runtime
BuildRequires:  perl(Archive::Any::Lite) >= 0.06
BuildRequires:  perl(Archive::Tar) >= 1.76
BuildRequires:  perl(Array::Diff) >= 0.04
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor) >= 0.19
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(CPAN::Meta::Converter)
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.133380
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.008
BuildRequires:  perl(Data::Binary)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Object) >= 0.2.1
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Perl::PrereqScanner::NotQuiteLite) >= 0.9901
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Parse::Distname)
BuildRequires:  perl(Software::License) >= 0.103012
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(version) >= 0.73
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:  perl(Test::File) >= 1.993
# Dependencies
Requires:       perl(Archive::Any::Lite) >= 0.06
Requires:       perl(Archive::Tar) >= 1.76
Requires:       perl(Array::Diff) >= 0.04
Requires:       perl(Class::Accessor) >= 0.19
Requires:       perl(CPAN::Meta::Validator) >= 2.133380
Requires:       perl(CPAN::Meta::YAML) >= 0.008
Requires:       perl(Exporter)
Requires:       perl(File::Find::Object) >= 0.2.1
Requires:       perl(JSON::PP)
Requires:       perl(Module::CPANfile)
Requires:       perl(Software::License) >= 0.103012
Requires:       perl(version) >= 0.73

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Archive::Any::Lite\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Array::Diff\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::Accessor\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::Validator\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::YAML\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Find::Object\\)$
%global __requires_exclude %__requires_exclude|^perl\\(version\\)$

Provides:       perl(Module::CPANTS::Analyse)
%description
CPANTS is an acronym for CPAN Testing Service. The goals of the CPANTS project
are to provide some sort of quality measure (called "Kwalitee") and lots of
metadata for all distributions on CPAN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-CPANTS-Analyse-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc AUTHORS Changes README.md TODO
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/CPANTS/
%{perl_vendorlib}/Module/CPANTS/Analyse.pm
%{perl_vendorlib}/Module/CPANTS/Kwalitee.pm
%dir %{perl_vendorlib}/Module/CPANTS/Kwalitee/
%{perl_vendorlib}/Module/CPANTS/Kwalitee/*.pm
%{_mandir}/man3/Module::CPANTS::Analyse.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::BrokenInstaller.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::CpantsErrors.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Distname.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Distros.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Files.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::FindModules.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::License.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Manifest.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::MetaYML.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::NeedsCompiler.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Pod.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Prereq.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Repackageable.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Signature.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Uses.3*
%{_mandir}/man3/Module::CPANTS::Kwalitee::Version.3*

%changelog
%autochangelog
