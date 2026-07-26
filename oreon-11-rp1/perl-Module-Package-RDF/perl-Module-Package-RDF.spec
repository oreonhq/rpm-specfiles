%global source0_hash 174609487b14f8db96baf1bbd06ad9454bae40e2f41a3a5113f83e722ebda916

Name:           perl-Module-Package-RDF
Version:        0.014
Release:        19%{?dist}
Summary:        Drive your distribution with RDF
# CONTRIBUTING: CC-BY-SA
# other files:  GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA
URL:            https://metacpan.org/release/Module-Package-RDF
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Package-RDF-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Package)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Getopt::ArgvFile)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::AutoLicense) >= 0.08
BuildRequires:  perl(Module::Install::AutoManifest)
# 1.04 version from Module::Install in META.yml
BuildRequires:  perl(Module::Install::Base) >= 1.04
BuildRequires:  perl(Module::Install::Copyright) >= 0.009
BuildRequires:  perl(Module::Install::Credits) >= 0.009
BuildRequires:  perl(Module::Install::DOAP) >= 0.006
BuildRequires:  perl(Module::Install::DOAPChangeSets) >= 0.206
BuildRequires:  perl(Module::Install::RDF) >= 0.009
BuildRequires:  perl(Module::Install::ReadmeFromPod) >= 0.12
BuildRequires:  perl(Module::Install::TrustMetaYml) >= 0.003
BuildRequires:  perl(Module::Package) >= 0.30
BuildRequires:  perl(Module::Package::Plugin)
BuildRequires:  perl(Moo)
BuildRequires:  perl(RDF::TriN3) >= 0.201
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(Software::License)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
# 1.04 version from Module::Install in META.yml
Requires:       perl(Module::Install::Base) >= 1.04
Requires:       perl(Module::Package::Plugin)
Requires:       perl(RDF::TriN3) >= 0.201
Requires:       perl(warnings)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Base|RDF::TriN3)\\)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(:VERSION\\) >= 5\\.(5|8)\\.

%description
This is a build system for Perl modules defined by RDF.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Package-RDF-%{version}
rm -rf inc
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

%build
# bootstrap dies on CPAN RT#71565 because it cannot normalize '5.010' string.
perl -Ilib Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    --skipdeps # avoid installing unused dependencies from CPAN
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README TODO
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*

%changelog
%autochangelog
