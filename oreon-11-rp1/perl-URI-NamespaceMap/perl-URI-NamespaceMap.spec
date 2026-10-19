%global source0_hash b05c3fb3cbcec9db925c039a0814ac4bcc2962e6b367d32fc339d79e9510e6b8
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_URI_NamespaceMap_enables_rdf
%bcond_without perl_URI_NamespaceMap_enables_optional_test
%if %{with perl_URI_NamespaceMap_enables_optional_test} && !%{defined perl_bootstrap}
%global optional_test 1
%else
%global optional_test 0
%endif
Name:           perl-URI-NamespaceMap
Version:        1.12
Release:        7%{?dist}
Summary:        Object-oriented collection of name spaces
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/URI-NamespaceMap
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/URI-NamespaceMap-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_URI_NamespaceMap_enables_rdf}
%endif
%if %{with perl_URI_NamespaceMap_enables_rdf}
Recommends:     perl(RDF::NS) >= 20130802
Recommends:     perl(RDF::NS::Curated)
Recommends:     perl(RDF::Prefixes)
%endif
Requires:       perl(URI) >= 1.52
Requires:       perl(XML::CommonNS)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CommonTest\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(CommonTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((Attean|Test::More|Types::Attean|URI)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IRI)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Moo)
BuildRequires:  perl(RDF::NS)
BuildRequires:  perl(RDF::NS::Curated)
BuildRequires:  perl(RDF::Prefixes)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::CommonNS)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%files -n perl-URI-NamespaceMap-tests -f %{oreon_filedir}/perl-URI-NamespaceMap-tests.list

%changelog

%autochangelog
