%global source0_hash 1db21989d805f1476e8064ecc4b9314b86d9062d37620d48c50ecaa7718dd5e5

Name:           perl-RDF-RDFa-Generator
Version:        0.204
Release:        6%{?dist}
Summary:        Generate data in RDFa
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/RDF-RDFa-Generator
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-RDFa-Generator-%{version}.tar.gz
# Adjust tests to perl-Test-Warnings ≥ 0.034, bug #2341034, proposed upstream,
# <https://github.com/perlrdf/p5-rdf-rdfa-generator/issues/7>,
# Copied from Debian <https://salsa.debian.org/perl-team/modules/packages/librdf-rdfa-generator-perl/-/raw/66f400fda5cc281ed7b8131fbd983a8eb30cc10d/debian/patches/done_testing-conflict.patch>
Patch0:         done_testing-conflict.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Icon::FamFamFam::Silk)
BuildRequires:  perl(RDF::NS::Curated) >= 0.006
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI::NamespaceMap) >= 1.05
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.60
# Tests:
BuildRequires:  perl(Attean) >= 0.019
BuildRequires:  perl(Attean::RDF)
# Additional prefixes are tested and they are provided by RDF::Prefixes that
# is an optional dependency of perl-URI-NamespaceMap
BuildRequires:  perl(RDF::Prefixes)
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Output)
Requires:       perl(XML::LibXML) >= 1.60

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Attean|Test::More|XML::LibXML)\\)$

%description
These Perl modules allow you to generate RDFa (Resource Description Framework
in Attributes) trees.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Attean) >= 0.019
Requires:       perl(RDF::Prefixes)
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n RDF-RDFa-Generator-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS examples README TODO
%dir %{perl_vendorlib}/RDF
%dir %{perl_vendorlib}/RDF/RDFa
%{perl_vendorlib}/RDF/RDFa/Generator.pm
%{perl_vendorlib}/RDF/RDFa/Generator
%{_mandir}/man3/RDF::RDFa::Generator.*
%{_mandir}/man3/RDF::RDFa::Generator::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
