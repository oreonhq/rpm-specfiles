%global source0_hash d0ea851c02eb27003d8242547837552539ff61d4f087028cdead0076fbbd463a
Name:           perl-Module-CPANTS-Analyse
Version:        1.03
Release:        1%{?dist}
Summary:        Generate Kwalitee ratings for a distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-CPANTS-Analyse
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Module-CPANTS-Analyse-%{version}.tar.gz
BuildArch:      noarch
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
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Archive::Any::Lite\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Array::Diff\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::Accessor\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::Validator\\)$
%global __requires_exclude %__requires_exclude|^perl\\(CPAN::Meta::YAML\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Find::Object\\)$
%global __requires_exclude %__requires_exclude|^perl\\(version\\)$
Provides:       perl(Module::CPANTS::Analyse)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Archive::Any::Lite)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Array::Diff)
BuildRequires:  perl(CPAN::Meta::Converter)
BuildRequires:  perl(CPAN::Meta::Validator)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Binary)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Object)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Parse::Distname)
BuildRequires:  perl(Perl::PrereqScanner::NotQuiteLite)
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
