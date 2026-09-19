%global source0_hash bb6d87c9094ccdc6ed426d2446e44a001328b0218f144a7b16bf6300b171cafd

Name:           perl-Icon-FamFamFam-Silk
%global cpan_version 0.002001003
# Normalized version
Version:        0.2.1.3
Release:        27%{?dist}
Summary:        Embed FamFamFam Silk icons in your code
# lib/Icon/FamFamFam/Silk.pm:   CC-BY and Public Domain
## Not in the binary package
# inc:                          GPL+ or Artistic
# Automatically converted from old format: CC-BY and Public Domain - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/Icon-FamFamFam-Silk
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Icon-FamFamFam-Silk-%{cpan_version}.tar.gz
# Break build cycle with Module::Package::RDF
Patch0:         Icon-FamFamFam-Silk-0.002001003-Build-without-Module-Package-RDF.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(URI)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61

%description
This is a collection of Silk icons from <http://famfamfam.com/lab/icons/silk/>
provided in form of a Perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Icon-FamFamFam-Silk-%{cpan_version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc
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
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
