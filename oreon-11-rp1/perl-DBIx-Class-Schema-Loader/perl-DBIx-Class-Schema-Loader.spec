%global source0_hash c9f8cbebfcadc19b6407a1598fd8f9a7a81bcaf67b7ae4e877906af85ba44b14

Name:           perl-DBIx-Class-Schema-Loader
Summary:        Dynamic definition of a DBIx::Class::Schema
Version:        0.07053
Release:        3%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/V/VE/VEESH/DBIx-Class-Schema-Loader-%{version}.tar.gz
URL:            https://metacpan.org/release/DBIx-Class-Schema-Loader
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Class::C3::Componentised)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Class::Unload)
BuildRequires:  perl(curry)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(Lingua::EN::Inflect::Number)
BuildRequires:  perl(Lingua::EN::Inflect::Phrase)
BuildRequires:  perl(Lingua::EN::Tagger)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(mro)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::CamelCase)
BuildRequires:  perl(String::ToIdentifier::EN)
BuildRequires:  perl(String::ToIdentifier::EN::Unicode)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
# Tests only
BuildRequires:  perl(Config)
# Unused BuildRequires:  perl(DBD::Interbase)
# Unused BuildRequires:  perl(DBD::Interbase::GetInfo)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Optional::Dependencies)
BuildRequires:  perl(DBIx::Class::Storage)
# Unused BuildRequires:  perl(DBIx::Class::Storage::DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
# hidden from PAUSE
Provides:       perl(DBIx::Class::Schema::Loader::Utils)
Requires:       perl(Hash::Merge)
Requires:       perl(Test::More)

%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(dbixcsl_.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(make_dbictest_db.*\\)

%description
DBIx::Class::Schema::Loader automates the definition of a
DBIx::Class::Schema by scanning database table definitions
and setting up the columns, primary keys, and relationships.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-Schema-Loader-%{version}
# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl` t/bin/simple_filter; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}/script
ln -s %{_bindir}/dbicdump %{buildroot}%{_libexecdir}/%{name}/script
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export SCHEMA_LOADER_TESTS_BACKCOMPAT=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%{perl_vendorlib}/DBIx*
%{_mandir}/man1/dbicdump*
%{_mandir}/man3/DBIx::Class::Schema::Loader*
%{_bindir}/dbicdump*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
