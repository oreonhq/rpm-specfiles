%global source0_hash e2735b99e7449bae1550774dc405925b7df50d3a1a29a5ba4c7af1f92cd0fce7
Name:           perl-Module-Install-TrustMetaYml
Version:        0.003
Release:        1%{?dist}
Summary:        Trusts META.yml list of dependencies
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA
URL:            https://metacpan.org/release/Module-Install-TrustMetaYml
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-TrustMetaYml-%{version}.tar.gz
Patch0:         Module-Install-TrustMetaYml-0.003-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
Requires:       perl(YAML::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
