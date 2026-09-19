%global source0_hash bf08d797d0532f7b78e74f0d816b630468e331159193c31d3fa221c09f8f5ddb

Name:           perl-Module-Install-DOAPChangeSets
Version:        0.206
Release:        27%{?dist}
Summary:        Write your distribution change log in RDF
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-DOAPChangeSets
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-DOAPChangeSets-%{version}.tar.gz
# To allow building without bundled modules
Patch0:         Module-Install-DOAPChangeSets-0.206-Bootstrap-without-Module-Package-RDF.patch
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
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::Version)
BuildRequires:  perl(RDF::Query) >= 2.906
BuildRequires:  perl(RDF::Trine) >= 0.112
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI::file) >= 4.0
# Optional run-time:
# Module::Install::Admin::RDF version from Module::Install::RDF in META
# Module::Install::Admin::RDF 0.006 not used at tests
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
# Module::Install::Admin::RDF version from Module::Install::RDF in META
Recommends:     perl(Module::Install::Admin::RDF) >= 0.006
Requires:       perl(RDF::Query) >= 2.906
Requires:       perl(RDF::Trine) >= 0.112
Requires:       perl(URI::file) >= 4.0

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((RDF::Query|RDF::Trine|URI::file)\\)$

%description
This package allows you to write your Changes file in Turtle or RDF/XML and
autogenerate a human-readable text file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Install-DOAPChangeSets-%{version}
# Remove bundled modules
%patch -P0 -p1
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
%doc Changes COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
