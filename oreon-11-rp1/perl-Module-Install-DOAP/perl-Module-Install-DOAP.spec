%global source0_hash aa32aba8f0e1c5b83f41d16ab58057e50e1a70380f01547bf7fb7082fdb3430e

Name:           perl-Module-Install-DOAP
Version:        0.006
Release:        27%{?dist}
Summary:        Generate META.yml data from DOAP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-DOAP
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-DOAP-%{version}.tar.gz
# Break build cycle
Patch0:         Module-Install-DOAP-0.006-Break-build-cycle-with-Module-Package-RDF.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Admin::RDF) >= 0.004
# Module::Install::Base version from Module::Install in META
BuildRequires:  perl(Module::Install::Base) >= 1.00
BuildRequires:  perl(RDF::Trine) >= 0.133
BuildRequires:  perl(RDF::Trine::Namespace)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Module::Install::Admin::RDF) >= 0.004
# Module::Install::Base version from Module::Install in META
Requires:       perl(Module::Install::Base) >= 1.00
Requires:       perl(RDF::Trine) >= 0.133

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Admin::RDF|Module::Install::Base|RDF::Trine)\\)

%description
This Module::Install plugin generates your META.yml file from RDF data
(especially DOAP) in your distribution's "meta" directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-DOAP-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r ./inc
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
%doc Changes COPYRIGHT CREDITS README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
