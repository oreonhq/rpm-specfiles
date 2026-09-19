%global source0_hash e2735b99e7449bae1550774dc405925b7df50d3a1a29a5ba4c7af1f92cd0fce7

Name:           perl-Module-Install-TrustMetaYml
Version:        0.003
Release:        28%{?dist}
Summary:        Trusts META.yml list of dependencies
# HACKING:      CC-BY-SA
# other files:  GPL+ Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA
URL:            https://metacpan.org/release/Module-Install-TrustMetaYml
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-TrustMetaYml-%{version}.tar.gz
# To boostrap this package without bundling
Patch0:         Module-Install-TrustMetaYml-0.003-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(strict)
# YAML::Tiny not used at tests
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(YAML::Tiny)

%description
This module is a Module::Install plugin that generates MYMETA.yml by simply
passing through the dependencies from META.yml. It does nothing when run from
the module author's development copy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-TrustMetaYml-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf ./inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS HACKING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
