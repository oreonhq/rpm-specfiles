%global source0_hash f977a25b4116a0a95a7c8a894fd37097abe19af9a6a9ed4d800604ec17873fe4
%bcond_with perl_DBD_MariaDB_enables_leak_test
%bcond_without perl_DBD_MariaDB_enables_net_ssleay_test
Name:           perl-DBD-MariaDB
Version:        1.24
Release:        1%{?dist}
Summary:        MariaDB and MySQL driver for the Perl5 Database Interface (DBI)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBD-MariaDB/
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALI/DBD-MariaDB-%{version}.tar.gz
Source1:        test-setup.t
Source2:        test-clean.t
Source3:        test-env.sh
Patch0:         DBD-MariaDB-1.23-Run-test-setup-and-clean.patch
%if %{with perl_DBD_MariaDB_enables_net_ssleay_test}
%endif
%if %{with perl_DBD_MariaDB_enables_leak_test}
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(lib.pl\\)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  mariadb
BuildRequires:  mariadb-connector-c
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mariadb-server
BuildRequires:  openssl-devel
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(bigint)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sscg
# /oreon:deps
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
Requires:       perl(CPAN::Meta::YAML)
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp %{SOURCE3} %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset RELEASE_TESTING
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
. $DIR/$(basename %{SOURCE3})
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

. %{SOURCE3}
unset RELEASE_TESTING
make test %{?with_perl_DBD_MariaDB_enables_leak_test:EXTENDED_TESTING=1}
%files -f %{oreon_filedir}/main.list
%files -n perl-DBD-MariaDB-tests -f %{oreon_filedir}/perl-DBD-MariaDB-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.24-4
- Prepare for Oreon 11 (RP1)
