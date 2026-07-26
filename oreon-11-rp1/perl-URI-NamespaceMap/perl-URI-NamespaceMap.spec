%global source0_hash b05c3fb3cbcec9db925c039a0814ac4bcc2962e6b367d32fc339d79e9510e6b8

# Recomend modules for RDF prefixes support
%bcond_without perl_URI_NamespaceMap_enables_rdf
# Perform optional tests
%bcond_without perl_URI_NamespaceMap_enables_optional_test

# Build cycle: perl-Attean → perl-URI-NamespaceMap
%if %{with perl_URI_NamespaceMap_enables_optional_test} && !%{defined perl_bootstrap}
%global optional_test 1
%else
%global optional_test 0
%endif

Name:           perl-URI-NamespaceMap
Version:        1.12
Release:        7%{?dist}
Summary:        Object-oriented collection of name spaces
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/URI-NamespaceMap
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/URI-NamespaceMap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(IRI) >= 0.004
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Moo) >= 1.006000
BuildRequires:  perl(namespace::autoclean) >= 0.20
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library) >= 1.000000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI) >= 0.004
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(warnings)
# Optional run-time:
# We need at least one of them
%if %{with perl_URI_NamespaceMap_enables_rdf}
BuildRequires:  perl(RDF::NS) >= 20130802
BuildRequires:  perl(RDF::NS::Curated)
BuildRequires:  perl(RDF::Prefixes)
%endif
BuildRequires:  perl(XML::CommonNS)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
# Build cycle: perl-Attean → perl-URI-NamespaceMap
%if %{optional_test}
# Optional tests:
BuildRequires:  perl(Attean) >= 0.025
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(RDF::Trine::NamespaceMap)
BuildRequires:  perl(Types::Attean) >= 0.024
%endif
# We need at least one of them, we choose XML::CommonNS
%if %{with perl_URI_NamespaceMap_enables_rdf}
Recommends:     perl(RDF::NS) >= 20130802
Recommends:     perl(RDF::NS::Curated)
Recommends:     perl(RDF::Prefixes)
%endif
Requires:       perl(URI) >= 1.52
Requires:       perl(XML::CommonNS)

# Hide private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CommonTest\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(CommonTest\\)
# Remove under-specified dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\((Attean|Test::More|Types::Attean|URI)\\)$

%description
These Perl modules provide a database system for managing URI name spaces in
an object-oriented manner.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
Requires:       perl(URI) >= 1.52
%if %{optional_test}
Requires:       perl(Attean) >= 0.025
Requires:       perl(RDF::Trine::NamespaceMap)
Requires:       perl(Types::Attean) >= 0.024
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n URI-NamespaceMap-%{version}
%if !%{optional_test}
for F in t/types-attean.t t/types-trine.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
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
%doc Changes COPYRIGHT CREDITS README
%dir %{perl_vendorlib}/Types
%{perl_vendorlib}/Types/Namespace.pm
%dir %{perl_vendorlib}/URI
%{perl_vendorlib}/URI/Namespace.pm
%{perl_vendorlib}/URI/NamespaceMap
%{perl_vendorlib}/URI/NamespaceMap.pm
%{_mandir}/man3/Types::Namespace.*
%{_mandir}/man3/URI::Namespace.*
%{_mandir}/man3/URI::NamespaceMap.*
%{_mandir}/man3/URI::NamespaceMap::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
