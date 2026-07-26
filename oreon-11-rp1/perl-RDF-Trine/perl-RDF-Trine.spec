%global source0_hash 1bb07daa10781738aeedd8e70156868c9a70fbd310f05f2ec1f6ea02d8697060

# Add support for a MySQL database
%bcond_without perl_RDF_Trine_enables_mysql
# Add support for a PostgreSQL database
%bcond_without perl_RDF_Trine_enables_postgresql
# Add support for a Redis database
%bcond_without perl_RDF_Trine_enables_redis
# Add support for a Redland database
%bcond_with perl_RDF_Trine_enables_redland
# Add support for a SQLite database
%bcond_without perl_RDF_Trine_enables_sqlite

Name:           perl-RDF-Trine
Version:        1.019
Release:        29%{?dist}
Summary:        RDF Framework for Perl
# README:           GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/RDF/Trine.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# t/data/turtle-2013/LICENSE:               BSD-3-Clause OR "W3C Test Suite License"
# t/data/rdfxml-w3c/xmlsch-02/test003.rdf:  W3C-20150513
SourceLicense:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause AND W3C-20150513
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-Trine
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/RDF-Trine-%{version}.tar.gz
# Remove unwanted build script features
Patch0:         RDF-Trine-1.016-Disable-release-code.patch
# Load only installed database backends. Otherwise we would have to require
# all of them.
Patch1:         RDF-Trine-1.014-Make-database-backends-optional.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(base)
# Cache::LRU not used at tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
# DBD::mysql not used at tests
# DBD::Pg not used at tests
BuildRequires:  perl(DBD::SQLite) >= 1.14
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
# GraphViz not used at tests
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IRI)
BuildRequires:  perl(JSON) >= 2.0
# List::MoreUtils not used at tests
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Load::Conditional) >= 0.38
BuildRequires:  perl(Moose) >= 2
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(overload)
# RDF::Redland 1.00 not used at tests
# Redis not used at tests because it requires configured and running server
BuildRequires:  perl(Scalar::Util) >= 1.24
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(XML::CommonNS) >= 0.04
# XML::LibXML not used directly, but XML::Namespace is unversioned
BuildRequires:  perl(XML::LibXML) >= 1.7
BuildRequires:  perl(XML::Namespace)
BuildRequires:  perl(XML::SAX) >= 0.96
BuildRequires:  perl(XML::SAX::Base)
# Optional run-time:
# Data::UUID and UUID::Tiny
# Term::ANSIColor
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::JSON)
BuildRequires:  perl(URI::file)
Recommends:     perl(Data::UUID)
Requires:       perl(GraphViz)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Load::Conditional) >= 0.38
Requires:       perl(Moose) >= 2
Requires:       perl(Scalar::Util) >= 1.24
Recommends:     perl(Term::ANSIColor)
Recommends:     perl(UUID::Tiny)
Requires:       perl(XML::LibXML) >= 1.7
Requires:       perl(XML::SAX) >= 0.96

# Remove dependencies from documentation
%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((JSON|List::Util|Module::Load::Conditional|Moose|Scalar::Util|Test::More|URI|XML::SAX)\\)$ 

%description
RDF::Trine provides an Resource Descriptive Framework (RDF) with an
emphasis on extensibility, API stability, and the presence of a test suite.

Support for MySQL, PosgreSQL, Redland, Redis, and SQLite is delivered by
separate packages (e.g. %{name}-mysql).

%if %{with perl_RDF_Trine_enables_redland}
%package redland
Summary:        Redland support for RDF::Trine
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Scalar::Util) >= 1.24

%description redland
This provides Redland parser and storage for RDF::Trine Perl framework.
%endif

%if %{with perl_RDF_Trine_enables_postgresql}
%package postgresql
Summary:        RDF::Trine store in PostgreSQL
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(DBD::Pg)
Requires:       perl(Scalar::Util) >= 1.24

%description postgresql
This provides an RDF::Trine::Store API to interact with PostgreSQL server. 
%endif

%if %{with perl_RDF_Trine_enables_mysql}
%package mysql
Summary:        RDF::Trine store in MySQL
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(DBD::mysql)
Requires:       perl(Scalar::Util) >= 1.24

%description mysql
This provides an RDF::Trine::Store API to interact with MySQL server. 
%endif

%if %{with perl_RDF_Trine_enables_sqlite}
%package sqlite
Summary:        RDF::Trine store in SQLite
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(DBD::SQLite) >= 1.14
Requires:       perl(Scalar::Util) >= 1.24

%description sqlite
This provides an RDF::Trine::Store API to interact with MySQL server. 
%endif

%if %{with perl_RDF_Trine_enables_redis}
%package redis
Summary:        RDF::Trine store in Redis
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(JSON) >= 2.0
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Scalar::Util) >= 1.24

%description redis
This provides an RDF::Trine::Store API to interact with a Redis server.
%endif

%package -n perl-Test-RDF-Trine-Store
Summary:        Collection of functions to test RDF::Trine stores
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::More) >= 0.88

%description -n perl-Test-RDF-Trine-Store
This Perl module packages a few functions that you can call to test a
RDF::Trine::Store.

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause AND W3C-20150513
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with perl_RDF_Trine_enables_redland}
Requires:       %{name}-redland = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%if %{with perl_RDF_Trine_enables_postgresql}
Requires:       %{name}-postgresql = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%if %{with perl_RDF_Trine_enables_mysql}
Requires:       %{name}-mysql = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%if %{with perl_RDF_Trine_enables_sqlite}
Requires:       %{name}-sqlite = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%if %{with perl_RDF_Trine_enables_redis}
Requires:       %{name}-redis = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n RDF-Trine-%{version}
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Removed tests for disabled features
%if !%{with perl_RDF_Trine_enables_redland}
rm t/parser-redland.t
perl -i -ne 'print $_ unless m{^t/parser-redland\.t}' MANIFEST
%endif
# Fix shellbangs
for F in bin/srx2csv bin/srx2table examples/foaf_labels.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
done
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
%doc Changes.ttl examples README
%{_bindir}/srx2csv
%{_bindir}/srx2table
%dir %{perl_vendorlib}/RDF
%{perl_vendorlib}/RDF/Trine
%{perl_vendorlib}/RDF/Trine.pm
%exclude %{perl_vendorlib}/RDF/Trine/Parser/Redland.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/DBI/Pg.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/DBI/mysql.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/DBI/SQLite.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/Redland.pm
%exclude %{perl_vendorlib}/RDF/Trine/Store/Redis.pm
%exclude %{perl_vendorlib}/Test
%{_mandir}/man3/RDF::Trine.*
%{_mandir}/man3/RDF::Trine::*
%exclude %{_mandir}/man3/RDF::Trine::Parser::Redland.*
%exclude %{_mandir}/man3/RDF::Trine::Store::DBI::Pg.*
%exclude %{_mandir}/man3/RDF::Trine::Store::DBI::mysql.*
%exclude %{_mandir}/man3/RDF::Trine::Store::DBI::SQLite.*
%exclude %{_mandir}/man3/RDF::Trine::Store::Redland.*
%exclude %{_mandir}/man3/RDF::Trine::Store::Redis.*
%exclude %{_mandir}/man3/Test::RDF::Trine::Store.*

%if %{with perl_RDF_Trine_enables_redland}
%files redland
%{perl_vendorlib}/RDF/Trine/Parser/Redland.pm
%{perl_vendorlib}/RDF/Trine/Store/Redland.pm
%{_mandir}/man3/RDF::Trine::Parser::Redland.*
%{_mandir}/man3/RDF::Trine::Store::Redland.*
%endif

%if %{with perl_RDF_Trine_enables_postgresql}
%files postgresql
%{perl_vendorlib}/RDF/Trine/Store/DBI/Pg.pm
%{_mandir}/man3/RDF::Trine::Store::DBI::Pg.*
%endif

%if %{with perl_RDF_Trine_enables_mysql}
%files mysql
%{perl_vendorlib}/RDF/Trine/Store/DBI/mysql.pm
%{_mandir}/man3/RDF::Trine::Store::DBI::mysql.*
%endif

%if %{with perl_RDF_Trine_enables_sqlite}
%files sqlite
%{perl_vendorlib}/RDF/Trine/Store/DBI/SQLite.pm
%{_mandir}/man3/RDF::Trine::Store::DBI::SQLite.*
%endif

%if %{with perl_RDF_Trine_enables_redis}
%files redis
%{perl_vendorlib}/RDF/Trine/Store/Redis.pm
%{_mandir}/man3/RDF::Trine::Store::Redis.*
%endif

%files -n perl-Test-RDF-Trine-Store
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::RDF::Trine::Store.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
