%global source0_hash 4c159ff53c5c383eb8eedf93d6310b26bcc83ae0547560968e65c57926df0304

# Perform optional tests
%if 0%{?rhel}
%bcond_with perl_Types_URI_enables_optional_test
%else
%bcond_without perl_Types_URI_enables_optional_test
%endif

%define optional_test %[%{with perl_Types_URI_enables_optional_test} && !%{defined %perl_bootstrap}]

Name:           perl-Types-URI
Version:        0.007
Release:        22%{?dist}
Summary:        Type constraints and coercions for URIs
# COPYRIGHT:    LicenseRef-Fedora-Public-Domain
# other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Types-URI
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Types-URI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Type::Library) >= 1.000000
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::UUID)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::data)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::FromHash)
BuildRequires:  perl(URI::WithBase)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(if)
BuildRequires:  perl(Test::More) >= 0.96
# Test::Warnings not used
# Build cycle: perl-Attean → perl-Types-URI
%if %{optional_test}
# Optional tests:
BuildRequires:  perl(Attean)
BuildRequires:  perl(Attean::IRI)
BuildRequires:  perl(IRI) >= 0.004
BuildRequires:  perl(Moose) >= 2.0000
BuildRequires:  perl(RDF::Trine) >= 1.000
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Types::Attean) >= 0.024
BuildRequires:  perl(Types::Namespace) >= 1.10
%endif
Requires:       perl(Type::Library) >= 1.000000

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Moose|Test::More|Type::Library|Types::Attean|Types::Namespace)\\)$

%description
Types::URI is a type constraint Perl library suitable for use with Moo/Moose
attributes, Kavorka sub signatures, and so forth.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96
%if %{optional_test}
Requires:       perl(Attean)
Requires:       perl(IRI) >= 0.004
Requires:       perl(Moose) >= 2.0000
Requires:       perl(RDF::Trine) >= 1.000
Requires:       perl(Types::Attean) >= 0.024
Requires:       perl(Types::Namespace) >= 1.10
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Types-URI-%{version}
%if !%{optional_test}
for F in t/02attean.t t/02trine.t t/03iri.t t/50mxt-basic.t t/51mxt-fully-qualified.t; do
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
%if %{optional_test}
unset AUTHOR_TESTING
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
%if %{optional_test}
unset AUTHOR_TESTING
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS README
%dir %{perl_vendorlib}/Types
%{perl_vendorlib}/Types/URI.pm
%{_mandir}/man3/Types::URI.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
