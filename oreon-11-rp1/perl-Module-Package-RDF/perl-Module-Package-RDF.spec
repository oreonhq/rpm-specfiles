%global source0_hash 174609487b14f8db96baf1bbd06ad9454bae40e2f41a3a5113f83e722ebda916
Name:           perl-Module-Package-RDF
Version:        0.014
Release:        19%{?dist}
Summary:        Drive your distribution with RDF
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA
URL:            https://metacpan.org/release/Module-Package-RDF
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Package-RDF-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Module::Install::Base) >= 1.04
Requires:       perl(Module::Package::Plugin)
Requires:       perl(RDF::TriN3) >= 0.201
Requires:       perl(warnings)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Base|RDF::TriN3)\\)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(:VERSION\\) >= 5\\.(5|8)\\.
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Getopt::ArgvFile)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::AutoLicense)
BuildRequires:  perl(Module::Install::AutoManifest)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::Copyright)
BuildRequires:  perl(Module::Install::Credits)
BuildRequires:  perl(Module::Install::DOAP)
BuildRequires:  perl(Module::Install::DOAPChangeSets)
BuildRequires:  perl(Module::Install::RDF)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::TrustMetaYml)
BuildRequires:  perl(Module::Package)
BuildRequires:  perl(Module::Package::Plugin)
BuildRequires:  perl(Moo)
BuildRequires:  perl(RDF::TriN3)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a build system for Perl modules defined by RDF.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Package-RDF-%{version}
rm -rf inc
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

%build

perl -Ilib Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    --skipdeps # avoid installing unused dependencies from CPAN
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
