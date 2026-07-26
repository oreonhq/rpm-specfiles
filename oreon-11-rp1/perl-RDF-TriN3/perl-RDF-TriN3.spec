%global source0_hash e3c633d88fbba47433e39e1788f0034aee7b6f244adf1eeb0155d4180c2fe6d1

Name:           perl-RDF-TriN3
Version:        0.206
Release:        28%{?dist}
Summary:        Notation 3 extensions for RDF::Trine
# CONTRIBUTING: CC-BY-SA
# other fiels:  GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA
URL:            https://metacpan.org/release/RDF-TriN3
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/RDF-TriN3-%{version}.tar.gz
# To boostrap this package without bundling
Patch0:         RDF-TriN3-0.206-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
BuildRequires:  perl(RDF::NS::Trine)
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(RDF::Trine::Error)
BuildRequires:  perl(RDF::Trine::Namespace)
BuildRequires:  perl(RDF::Trine::Node)
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(RDF::Trine::Parser)
BuildRequires:  perl(RDF::Trine::Pattern)
BuildRequires:  perl(RDF::Trine::Serializer::NTriples)
BuildRequires:  perl(RDF::Trine::Statement)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
# Require at least one database storage. Otherwise a t/02dbi.t test fails
# because Memory storage does not provide clear_restrictions() method.
BuildRequires:  perl(RDF::Trine::Store::DBI::SQLite)
Requires:       perl(RDF::Trine) >= 0.135

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(RDF::Trine\\)$

%description
This Perl module extends RDF::Trine. It adds Notation 3 parser, serializer and
it provides subclass for representing Notation 3 formulae literals.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RDF-TriN3-%{version}
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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
