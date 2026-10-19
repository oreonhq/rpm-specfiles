%global source0_hash bb6d87c9094ccdc6ed426d2446e44a001328b0218f144a7b16bf6300b171cafd
Name:           perl-Icon-FamFamFam-Silk
%global cpan_version 0.002001003
Version:        0.2.1.3
Release:        27%{?dist}
Summary:        Embed FamFamFam Silk icons in your code
License:        LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/Icon-FamFamFam-Silk
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Icon-FamFamFam-Silk-%{cpan_version}.tar.gz
Patch0:         Icon-FamFamFam-Silk-0.002001003-Build-without-Module-Package-RDF.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
