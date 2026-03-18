# Disable leak tests
%bcond_with perl_DBD_MariaDB_enables_leak_test
# Perform optional net_ssleay tests
%if 0%{?rhel}
%bcond_with perl_DBD_MariaDB_enables_net_ssleay_test
%else
%bcond_without perl_DBD_MariaDB_enables_net_ssleay_test
%endif

Name:           perl-DBD-MariaDB
Version:        1.24
Release:        4%{?dist}
Summary:        MariaDB and MySQL driver for the Perl5 Database Interface (DBI)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBD-MariaDB/
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALI/DBD-MariaDB-%{version}.tar.gz
Source1:        test-setup.t
Source2:        test-clean.t
Source3:        test-env.sh
Patch0:         DBD-MariaDB-1.23-Run-test-setup-and-clean.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mariadb-connector-c
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.608
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(Devel::CheckLib) >= 1.12
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sscg
# Tests
BuildRequires:  hostname
BuildRequires:  mariadb
BuildRequires:  mariadb-server
BuildRequires:  perl(B)
BuildRequires:  perl(bigint)
BuildRequires:  perl(constant)
# Required to process t/testrules.yml
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Optional tests
%if %{with perl_DBD_MariaDB_enables_net_ssleay_test}
BuildRequires:  perl(Net::SSLeay)
%endif
%if %{with perl_DBD_MariaDB_enables_leak_test}
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Storable)
%endif


# Filter private modules for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(lib.pl\\)

%description
DBD::MariaDB is the Perl5 Database Interface driver for MariaDB and MySQL
databases. In other words: DBD::MariaDB is an interface between the Perl
programming language and the MariaDB/MySQL programming API that comes with
the MariaDB/MySQL relational database management system. Most functions
provided by this programming API are supported. Some rarely used functions
are missing, mainly because no-one ever requested them.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       hostname
Requires:       mariadb
Requires:       mariadb-server
# Required to process t/testrules.yml
Requires:       perl(CPAN::Meta::YAML)
# Optional tests
%if %{with perl_DBD_MariaDB_enables_net_ssleay_test}
Requires:       perl(Net::SSLeay)
%endif
%if %{with perl_DBD_MariaDB_enables_leak_test}
Requires:       perl(Proc::ProcessTable)
Requires:       perl(Storable)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n DBD-MariaDB-%{version}
%patch -P0 -p1
cp %{SOURCE1} %{SOURCE2} t/

# Create certificates for tests
mkdir t/certs
sscg --hostname=localhost --ca-mode=0644 --ca-key-mode=0640 --cert-key-mode=0640 --no-dhparams-file
mv ca.crt service-key.pem service.pem t/certs

# Help file to recognise the Perl scripts and normalize shebangs
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

# Remove release tests
for F in t/pod.t t/manifest.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' t/testrules.yml
done

%if %{without perl_DBD_MariaDB_enables_leak_test}
# Remove unused tests
for F in t/60leaks.t t/rt86153-reconnect-fail-memory.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' t/testrules.yml
done
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp %{SOURCE3} %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/usr/bin/bash
set -e
unset RELEASE_TESTING

# The tests write to temporary database which is placed in $DIR/t/testdb
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./

# Load the variables
. $DIR/$(basename %{SOURCE3})

# Run tests
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Set MariaDB and DBD::MariaDB test environment
. %{SOURCE3}

unset RELEASE_TESTING
make test %{?with_perl_DBD_MariaDB_enables_leak_test:EXTENDED_TESTING=1}

%files
%license LICENSE
%doc Changes Changes.historic
%{perl_vendorarch}/auto/DBD*
%{perl_vendorarch}/DBD*
%{_mandir}/man3/DBD::MariaDB*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.24-4
- Prepare for Oreon 11 (RP1)
