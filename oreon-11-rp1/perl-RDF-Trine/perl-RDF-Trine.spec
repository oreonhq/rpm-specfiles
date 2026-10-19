%global source0_hash 1bb07daa10781738aeedd8e70156868c9a70fbd310f05f2ec1f6ea02d8697060
%bcond_without perl_RDF_Trine_enables_mysql
%bcond_without perl_RDF_Trine_enables_postgresql
%bcond_without perl_RDF_Trine_enables_redis
%bcond_with perl_RDF_Trine_enables_redland
%bcond_without perl_RDF_Trine_enables_sqlite
Name:           perl-RDF-Trine
Version:        1.019
Release:        1%{?dist}
Summary:        RDF Framework for Perl
SourceLicense:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause AND W3C-20150513
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-Trine
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/RDF-Trine-%{version}.tar.gz
Patch0:         RDF-Trine-1.016-Disable-release-code.patch
Patch1:         RDF-Trine-1.014-Make-database-backends-optional.patch
BuildArch:      noarch
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
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((JSON|List::Util|Module::Load::Conditional|Moose|Scalar::Util|Test::More|URI|XML::SAX)\\)$ 
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IRI)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::JSON)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(XML::CommonNS)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::Namespace)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perl-Test-RDF-Trine-Store usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-RDF-Trine-postgresql -f %{oreon_filedir}/perl-RDF-Trine-postgresql.list
%files -n perl-RDF-Trine-mysql -f %{oreon_filedir}/perl-RDF-Trine-mysql.list
%files -n perl-RDF-Trine-sqlite -f %{oreon_filedir}/perl-RDF-Trine-sqlite.list
%files -n perl-RDF-Trine-redis -f %{oreon_filedir}/perl-RDF-Trine-redis.list
%files -n perl-Test-RDF-Trine-Store -f %{oreon_filedir}/perl-Test-RDF-Trine-Store.list
%files -n perl-RDF-Trine-tests -f %{oreon_filedir}/perl-RDF-Trine-tests.list

%changelog

%autochangelog
