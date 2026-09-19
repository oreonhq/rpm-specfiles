%global source0_hash e0784e3861a197ad5aa17396f18901f0aaa8bab04a4330cb50038337ec30ca7f

Name:           perl-DBIx-Class
Summary:        Extensible and flexible object <-> relational mapper
Version:        0.082844
Release:        3%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-%{version}.tar.gz
URL:            https://metacpan.org/release/DBIx-Class
# Do not use /usr/bin/env in shell bangs, upstream does not agree
# (see Changes)
Patch0:         DBIx-Class-0.082840-Do-not-use-usr-bin-env-in-shell-bangs.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Class::C3::Componentised)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(constant)
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.2
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::Const::GetInfoReturn)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(DBIx::ContextualFetch)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.081
BuildRequires:  perl(Getopt::Long::Descriptive::Usage)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON::Any) >= 1.23
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Base36) >= 0.07
BuildRequires:  perl(Math::BigInt) >= 1.80
BuildRequires:  perl(Method::Generate::Accessor)
BuildRequires:  perl(Method::Generate::Constructor)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Object)
BuildRequires:  perl(Moose) >= 0.98
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types) >= 0.21
BuildRequires:  perl(MooseX::Types::JSON) >= 0.02
BuildRequires:  perl(MooseX::Types::LoadableClass) > 0.011
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class) >= 0.05
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(SQL::Abstract::Classic) >= 1.91
BuildRequires:  perl(SQL::Abstract::Tree)
BuildRequires:  perl(SQL::Abstract::Util)
BuildRequires:  perl(SQL::Translator::Diff)
BuildRequires:  perl(SQL::Translator::Schema::Constants)
BuildRequires:  perl(SQL::Translator::Utils)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Defer)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
# Tests only
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Class::DBI::Column)
BuildRequires:  perl(Class::DBI::Plugin::DeepAbstractSearch)
BuildRequires:  perl(Class::Unload)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::GUID)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::Pg)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
# Optional for TEST_VERBOSE: BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON)
#BuildRequires:  perl(JSON::DWIW)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(SQL::Abstract::Test)
BuildRequires:  perl(SQL::Translator) >= 0.11018
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::CSV) >= 1.16
BuildRequires:  perl(threads)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Piece::MySQL)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML)
Requires:       perl(B::Deparse)
Requires:       perl(Config::Any)
Requires:       perl(DateTime::Format::Strptime) >= 1.2
Requires:       perl(DBI::Const::GetInfoReturn)
Requires:       perl(DBI::Const::GetInfoType)
Requires:       perl(Digest::MD5)
Requires:       perl(File::Spec)
Requires:       perl(Getopt::Long::Descriptive) >= 0.081
Requires:       perl(JSON::Any) >= 1.23
Requires:       perl(Math::Base36) >= 0.07
Requires:       perl(Math::BigInt) >= 1.80
Requires:       perl(Module::Find)
Requires:       perl(Moose) >= 0.98
Requires:       perl(MooseX::Types) >= 0.21
Requires:       perl(MooseX::Types::JSON) >= 0.02
Requires:       perl(MooseX::Types::LoadableClass) > 0.011
Requires:       perl(MooseX::Types::Path::Class) >= 0.05
Requires:       perl(POSIX)
Requires:       perl(SQL::Translator::Diff)
Requires:       perl(Sub::Quote)
Requires:       perl(Text::Balanced)
# hidden from PAUSE
Provides:       perl(DBIx::Class::Admin::Descriptive) = %{version}
Provides:       perl(DBIx::Class::Admin::Types) = %{version}
Provides:       perl(DBIx::Class::Admin::Usage) = %{version}
Provides:       perl(DBIx::Class::Carp) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AbstractSearch) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AccessorMapping) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AttributeAPI) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::AutoUpdate) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnCase) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnGroups) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnGroups::GrouperShim) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ColumnsAsHash) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Constraints) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Constructor) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Copy) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::DestroyWarning) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::GetSet) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ImaDBI) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Iterator::ResultSet) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::LazyLoading) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::LiveObjectIndex) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::NoObjectIndex) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Pager) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::ReadOnly) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Relationship) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Relationships) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Retrieve) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Stringify) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::TempColumns) = %{version}
Provides:       perl(DBIx::Class::CDBICompat::Triggers) = %{version}
Provides:       perl(DBIx::Class::ClassResolver::PassThrough) = %{version}
Provides:       perl(DBIx::Class::Componentised) = %{version}
Provides:       perl(DBIx::Class::_ENV_) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::DB2) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::MSSQL) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::MySQL) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::Oracle) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::Pg) = %{version}
Provides:       perl(DBIx::Class::PK::Auto::SQLite) = %{version}
Provides:       perl(DBIx::Class::Relationship::Accessor) = %{version}
Provides:       perl(DBIx::Class::Relationship::BelongsTo) = %{version}
Provides:       perl(DBIx::Class::Relationship::CascadeActions) = %{version}
Provides:       perl(DBIx::Class::Relationship::HasMany) = %{version}
Provides:       perl(DBIx::Class::Relationship::HasOne) = %{version}
Provides:       perl(DBIx::Class::Relationship::Helpers) = %{version}
Provides:       perl(DBIx::Class::Relationship::ManyToMany) = %{version}
Provides:       perl(DBIx::Class::Relationship::ProxyMethods) = %{version}
Provides:       perl(DBIx::Class::ResultSetProxy) = %{version}
Provides:       perl(DBIx::Class::ResultSourceProxy) = %{version}
Provides:       perl(DBIx::Class::ResultSource::RowParser::Util) = %{version}
Provides:       perl(DBIx::Class::ResultSource::RowParser) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::MSSQL) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::MySQL) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::OracleJoins) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::Oracle) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks::SQLite) = %{version}
Provides:       perl(DBIx::Class::SQLAHacks) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::ACCESS) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::MSSQL) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::MySQL) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::Oracle) = %{version}
Provides:       perl(DBIx::Class::SQLMaker::SQLite) = %{version}
Provides:       perl(DBIx::Class::Storage::BlockRunner) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ADO::CursorUtils) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ADO::Microsoft_SQL_Server::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ADO::MS_Jet::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBIHacks) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Informix::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::InterBase::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::MSSQL::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::ODBC::ACCESS::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Replicated::Types) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Sybase::ASE::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::DBI::Sybase::Microsoft_SQL_Server::DateTime::Format) = %{version}
Provides:       perl(DBIx::Class::Storage::NESTED_ROLLBACK_EXCEPTION) = %{version}
Provides:       perl(DBIx::Class::_Util) = %{version}
Provides:       perl(DBIx::Class::_Util::ScopeGuard) = %{version}
Provides:       perl(DBIx::Class::VersionCompat) = %{version}
Provides:       perl(DBIx::Class::Version::TableCompat) = %{version}
Provides:       perl(DBIx::Class::Version::Table) = %{version}
Provides:       perl(DBIx::Class::Version) = %{version}
Provides:       perl(DBIx::ContextualFetch::st) = %{version}

%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Getopt::Long::Descriptive\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(JSON::Any\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types::JSON\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types::LoadableClass\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MooseX::Types::Path::Class\\)$

%description
This is an SQL to OO mapper with an object API inspired by Class::DBI
(and a compatibility layer as a springboard for porting) and a
result-set API that allows abstract encapsulation of database
operations. It aims to make representing queries in your code as perlish
as possible while still providing access to as many of the
capabilities of the database as possible, including retrieving related
records from multiple tables in a single query, JOIN, LEFT JOIN, COUNT,
DISTINCT, GROUP BY and HAVING support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-%{version}
%patch -P0 -p1
chmod -c +x script/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# note this test suite is noisy!
export DBICTEST_THREAD_STRESS=1
export DBICTEST_FORK_STRESS=1
export DBICTEST_STORAGE_STRESS=1
export DATA_DUMPER_TEST=1
make test

%files
%license LICENSE
%doc AUTHORS Changes README examples/ t/
%{_bindir}/dbicadmin*
%dir %{perl_vendorlib}/DBIx
%{perl_vendorlib}/DBIx/Class*
%dir %{perl_vendorlib}/SQL
%{perl_vendorlib}/SQL/Translator*
%{_mandir}/man1/dbicadmin*
%{_mandir}/man3/DBIx::Class*
%{_mandir}/man3/SQL::Translator*

%changelog
%autochangelog
