%global source0_hash 1db21989d805f1476e8064ecc4b9314b86d9062d37620d48c50ecaa7718dd5e5
Name:           perl-RDF-RDFa-Generator
Version:        0.204
Release:        6%{?dist}
Summary:        Generate data in RDFa
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/RDF-RDFa-Generator
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-RDFa-Generator-%{version}.tar.gz
Patch0:         done_testing-conflict.patch
BuildArch:      noarch
Requires:       perl(XML::LibXML) >= 1.60
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Attean|Test::More|XML::LibXML)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Attean)
BuildRequires:  perl(Attean::RDF)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Icon::FamFamFam::Silk)
BuildRequires:  perl(RDF::NS::Curated)
BuildRequires:  perl(RDF::Prefixes)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(URI::NamespaceMap)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-RDF-RDFa-Generator-tests -f %{oreon_filedir}/perl-RDF-RDFa-Generator-tests.list

%changelog

%autochangelog
