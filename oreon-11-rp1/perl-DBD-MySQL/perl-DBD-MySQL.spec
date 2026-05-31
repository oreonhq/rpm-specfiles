%global source0_hash aeb0a6e1c26fc28a5cf6de1161e0f056ddcbb739f87954dba7cb1c5acb4e1c33

%if 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

%global cpan_name DBD-mysql

# Disable leak tests
%bcond_with perl_DBD_MySQL_enables_leak_test

%if 0%{?rhel} >= 10
%global mysqlname mysql8.4
%else
%global mysqlname mysql
%endif

Name:           perl-DBD-MySQL
Version:        5.013
Release:        3%{?dist}
Summary:        A MySQL interface for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DV/DVEEDEN/%{cpan_name}-%{version}.tar.gz
Source1:        test-setup.t
Source2:        test-clean.t
Source3:        testrules.yml
Source4:        test-env.sh

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
# DBD::mysql v5.x requires MySQL 8.x client libraries for building
BuildRequires:  %{mysqlname}-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(Devel::CheckLib) >= 1.09
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  zlib-devel
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI) >= 1.609
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(DynaLoader)
# Tests
BuildRequires:  %{mysqlname}
BuildRequires:  %{mysqlname}-server
BuildRequires:  perl(B)
BuildRequires:  perl(bigint)
# Required to process t/testrules.yml
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Encode)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Optional tests
%if %{with perl_DBD_MySQL_enables_leak_test}
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Storable)
%endif

Provides:       perl-DBD-mysql = %{version}-%{release}

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(.*lib.pl\\)

%description 
DBD::mysql is the Perl5 Database Interface driver for the MySQL database. In
other words: DBD::mysql is an interface between the Perl programming language
and the MySQL programming API that comes with the MySQL relational database
management system.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       coreutils
Requires:       shadow-utils
Requires:       %{mysqlname}
Requires:       %{mysqlname}-server
# Required to process t/testrules.yml
Requires:       perl(CPAN::Meta::YAML)
# Optional tests
%if %{with perl_DBD_MariaDB_enables_leak_test}
Requires:       perl(Proc::ProcessTable)
Requires:       perl(Storable)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{cpan_name}-%{version}

# Correct file permissions
find . -type f | xargs chmod -x

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} t/
cp %{SOURCE4} .

# Help file to recognise the Perl scripts and normalize shebangs
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
. %{SOURCE4}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1 \
  --testdb=$DBD_MYSQL_TESTDB \
  --testuser=$DBD_MYSQL_TESTUSER \
  --testpassword=$DBD_MYSQL_TESTPASSWORD \
  --testhost=$DBD_MYSQL_TESTHOST \
  --testsocket=$DBD_MYSQL_TESTSOCKET
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp %{SOURCE4} %{buildroot}%{_libexecdir}/%{name}
# Replace build dir by template
perl -i -pe 's{%{_builddir}/.*mysql.sock}{_TEST_SOCKET_}' %{buildroot}%{_libexecdir}/%{name}/t/mysql.mtest
# Remove release tests
rm %{buildroot}%{_libexecdir}/%{name}/t/manifest.t
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t

cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/usr/bin/bash
set -e
# The tests write to temporary database which is placed in $DIR/t/testdb
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
. $DIR/$(basename %{SOURCE4})
%{!?with_perl_DBD_MySQL_enables_leak_test:unset EXTENDED_TESTING}
perl -i -pe "s{_TEST_SOCKET_}{$DBD_MYSQL_TESTSOCKET}" $DIR/t/mysql.mtest

# Test setup and tests have to be executed by non-root user
if [ `id -u` -ne 0 ]; then
    prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
else
    getent group $DBD_MYSQL_TESTUSER >/dev/null || \
        groupadd -r $DBD_MYSQL_TESTUSER
    getent passwd $DBD_MYSQL_TESTUSER >/dev/null || \
        useradd -g $DBD_MYSQL_TESTUSER $DBD_MYSQL_TESTUSER
    chown -hR $DBD_MYSQL_TESTUSER:$DBD_MYSQL_TESTUSER $DIR
    su $DBD_MYSQL_TESTUSER -c "prove -I . -j \"$(getconf _NPROCESSORS_ONLN)\""
    chown -hR root:root $DIR
    getent passwd $DBD_MYSQL_TESTUSER &>/dev/null && userdel -r $DBD_MYSQL_TESTUSER
    getent group $DBD_MYSQL_TESTUSER &>/dev/null && groupdel $DBD_MYSQL_TESTUSER
fi

popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Set MySQL and DBD::mysql test environment
. %{SOURCE4}
unset RELEASE_TESTING
make test %{?with_perl_DBD_MySQL_enables_leak_test:EXTENDED_TESTING=1}

%files
%license LICENSE
%doc Changes README.md  SECURITY.md
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{_mandir}/man3/DBD::mysql*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.013-3
- Prepare for Oreon 11 (RP1)
