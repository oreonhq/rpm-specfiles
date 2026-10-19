%global source0_hash bf08d797d0532f7b78e74f0d816b630468e331159193c31d3fa221c09f8f5ddb
Name:           perl-Module-Install-DOAPChangeSets
Version:        0.206
Release:        1%{?dist}
Summary:        Write your distribution change log in RDF
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-DOAPChangeSets
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-DOAPChangeSets-%{version}.tar.gz
Patch0:         Module-Install-DOAPChangeSets-0.206-Bootstrap-without-Module-Package-RDF.patch
BuildArch:      noarch
Recommends:     perl(Module::Install::Admin::RDF) >= 0.006
Requires:       perl(RDF::Query) >= 2.906
Requires:       perl(RDF::Trine) >= 0.112
Requires:       perl(URI::file) >= 4.0
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((RDF::Query|RDF::Trine|URI::file)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Perl::Version)
BuildRequires:  perl(RDF::Query)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
