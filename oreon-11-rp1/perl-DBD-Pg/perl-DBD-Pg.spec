%global source0_hash 6d30efeb119838ca22ae882b4183fe7fade42fb1ed99d6d1c84ce1625d86c9bd

# Perform optional tests
%bcond_without perl_DBD_Pg_enables_optional_test

Name:           perl-DBD-Pg
Summary:        A PostgreSQL interface for Perl
Version:        3.19.0
Release:        1%{?dist}
# Pg.pm, README:    Points to directory which contains GPL-2.0-or-later and Artistic-1.0-Perl
# other files:      Same as Perl (GPL-1.0-or-later OR Artistic-1.0-Perl)
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/DBD-Pg-%{version}.tar.gz
URL:            https://metacpan.org/release/DBD-Pg

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.64
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  libpq-devel
# Run-time:
BuildRequires:  perl(constant)
# Prevent bug #443495
BuildRequires:  perl(DBI) >= 1.614
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(version)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(charnames)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(open)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  postgresql-server
%if %{with perl_DBD_Pg_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Time::Piece)
%endif

Requires:       perl(DBI) >= 1.614

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DBD::Pg\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBI\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(App::Info.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(dbdpg_test_setup.pl\\)

Provides:       perl(DBD::Pg)
Provides:       perl(DBD::Pg)
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
# Optional tests:
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# If variables undefined, package test will create it's own database.
unset DBI_DSN DBI_USER DBI_PASS
unset DBDPG_DEBUG DBDPG_INITDB DBDPG_NOCLEANUP DBDPG_TEST_ALWAYS_ENV \
    DBDPG_TESTINITDB PGDATABASE PGINITDB POSTGRES_HOME POSTGRES_LIB \
    TEST_OUTPUT TEST_SIGNATURE
# The tests write to temporary database which is placed in $DIR
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
# When tests are run by root, 'postgres' is used as DBI_USER
# DBI_USER has to be able to write to the $DIR
if [ `id -u` -eq 0 ]; then
    chown -hR postgres:postgres $DIR
fi
# Jobs can't be run in parallel
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Full test coverage requires a live PostgreSQL database (see the README file)
#export DBI_DSN=dbi:Pg:dbname=<database>
#export DBI_USER=<username>
#export DBI_PASS=<password>
# If variables undefined, package test will create it's own database.
unset DBI_DSN DBI_USER DBI_PASS
unset DBDPG_DEBUG DBDPG_INITDB DBDPG_NOCLEANUP DBDPG_TEST_ALWAYS_ENV \
    DBDPG_TESTINITDB PGDATABASE PGINITDB POSTGRES_HOME POSTGRES_LIB \
    TEST_OUTPUT TEST_SIGNATURE
make test

%files
%license LICENSES/*
%doc Changes README README.dev TODO
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/Bundle/DBD/Pg.pm
%{_mandir}/man3/*DBD*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.19.0-1
- Prepare for Oreon 11 (RP1)
