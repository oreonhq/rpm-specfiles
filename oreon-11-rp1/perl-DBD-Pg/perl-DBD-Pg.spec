%global source0_hash d79179255ccb0c87b029db2eecaea56828e581255c48445d5fc0e79fa4e9245b
%bcond_without perl_DBD_Pg_enables_optional_test
Name:           perl-DBD-Pg
Summary:        A PostgreSQL interface for Perl
Version:        3.21.2
Release:        1%{?dist}
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/DBD-Pg-%{version}.tar.gz
URL:            https://metacpan.org/release/DBD-Pg
%if %{with perl_DBD_Pg_enables_optional_test}
%endif
Requires:       perl(DBI) >= 1.614
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DBD::Pg\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(App::Info.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(dbdpg_test_setup.pl\\)
Provides:       perl(DBD::Pg)
Provides:       perl(DBD::Pg)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  postgresql-server
# /oreon:deps
%description
DBD::Pg is a Perl module that works with the DBI module to provide access
to PostgreSQL databases.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Simple)
Requires:       postgresql-server
%if %{with perl_DBD_Pg_enables_optional_test}
Requires:       perl(Time::Piece)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DBD-Pg-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

unset AUTOMATED_TESTING DBDPG_GCCDEBUG PERL_MM_USE_DEFAULT \
    POSTGRES_HOME POSTGRES_INCLUDE POSTGRES_LIB
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset DBI_DSN DBI_USER DBI_PASS
unset DBDPG_DEBUG DBDPG_INITDB DBDPG_NOCLEANUP DBDPG_TEST_ALWAYS_ENV \
    DBDPG_TESTINITDB PGDATABASE PGINITDB POSTGRES_HOME POSTGRES_LIB \
    TEST_OUTPUT TEST_SIGNATURE
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
if [ `id -u` -eq 0 ]; then
    chown -hR postgres:postgres $DIR
fi
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset DBI_DSN DBI_USER DBI_PASS
unset DBDPG_DEBUG DBDPG_INITDB DBDPG_NOCLEANUP DBDPG_TEST_ALWAYS_ENV \
    DBDPG_TESTINITDB PGDATABASE PGINITDB POSTGRES_HOME POSTGRES_LIB \
    TEST_OUTPUT TEST_SIGNATURE
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-DBD-Pg-tests -f %{oreon_filedir}/perl-DBD-Pg-tests.list

%changelog

%autochangelog
