%global source0_hash 536e07755ce5948acfe3d1982d76a1c10f0fc593ce8b607a3137406a42789d7b
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_Attean_enables_optional_test
Name:           perl-Attean
Version:        0.035
Release:        4%{?dist}
Summary:        Semantic web framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Attean
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/Attean-%{version}.tar.gz
Patch0:         Attean-0.017-Canonize-shebangs.patch
Patch1:         Attean-0.034-Disable-unwanted-build-time-dependecies.patch
Patch2:         Attean-0.035-Copy-missing-modules-from-a-git-tree.patch
BuildArch:      noarch
%if %{with perl_Attean_enables_optional_test}
%endif
Requires:       perl(Exporter::Tiny) >= 1
Requires:       perl(IRI) >= 0.005
Requires:       perl(Math::Cartesian::Product) >= 1.008
Requires:       perl(Moo) >= 2.000002
Requires:       perl(MooX::Log::Any)
Requires:       perl(Role::Tiny) >= 2.000003
Requires:       perl(sort)
Requires:       perl(Sub::Util) >= 1.4
Requires:       perl(URI::Escape) >= 1.36
Requires:       perl(URI::NamespaceMap) >= 0.12
Provides:       perl(Attean::Algebra) = %{version}
Provides:       perl(Attean::API::Query) = %{version}
Provides:       perl(Attean::Expression) = %{version}
Provides:       perl(Attean::Plan) = %{version}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter::Tiny|IRI|Math::Cartesian::Product|Moo|Role::Tiny|Sub::Util|Test::Modern|Test::More|URI::Escape|URI::NamespaceMap)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(I18N::LangTags)
BuildRequires:  perl(IRI)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Cartesian::Product)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Log::Any)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO::Layers)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Roo)
BuildRequires:  perl(Test::Roo::Role)
BuildRequires:  perl(Test::TypeTiny)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Type::Tiny::Role)
BuildRequires:  perl(Types::Common::String)
BuildRequires:  perl(Types::Namespace)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(Types::UUID)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::Namespace)
BuildRequires:  perl(URI::NamespaceMap)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(UUID::Tiny)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(open)
BuildRequires:  perl(sort)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Attean provides APIs for parsing, storing, querying, and serializing semantic
web (RDF and SPARQL) data.

%package -n perl-Test-Attean
Summary:        Modules for testing Attean semantic web framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Modern) >= 0.012
%description -n perl-Test-Attean
These are helper Perl modules for testing Attean, a semantic web framework.

%package tests
Summary:        Tests for %{name}
Requires:       perl-Test-Attean = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Attean::API::CostPlanner)
Requires:       perl(Attean::API::NaiveJoinPlanner)
Requires:       perl(Attean::API::NullaryQueryTree)
Requires:       perl(Attean::API::SimpleCostPlanner)
Requires:       perl(Attean::API::UnionScopeVariablesPlan)
Requires:       perl(Attean::Plan::Exists)
Requires:       perl(Attean::QueryPlanner)
Requires:       perl(AtteanX::API::JoinRotatingPlanner)
Requires:       perl(Moo)
%if %{with perl_Attean_enables_optional_test}
Requires:       perl(RDF::Trine)
%endif
Requires:       perl(Test::Attean::MutableETagCacheableQuadStore)
Requires:       perl(Test::Attean::MutableQuadStore)
Requires:       perl(Test::Attean::MutableTimeCacheableQuadStore)
Requires:       perl(Test::Attean::QuadStore)
Requires:       perl(Test::Attean::TripleStore)
Requires:       perl(Test::Modern) >= 0.012
Requires:       perl(Test::More) >= 0.88
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Attean-%{version}
# Remove bundled modules
rm -r inc/*
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST
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
%oreon_autofiles perl-Test-Attean usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Attean -f %{oreon_filedir}/perl-Test-Attean.list
%files -n perl-Attean-tests -f %{oreon_filedir}/perl-Attean-tests.list

%changelog

%autochangelog
