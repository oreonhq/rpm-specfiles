%global source0_hash 12a2870de0774e5de17649c85b540ee6c00c9c5505010f2909b047e4b3e47b4a
%bcond_without perl_SQL_Shell_enables_optional_test
Name:       perl-SQL-Shell 
Version:    1.18
Release:        1%{?dist}
License:    GPL-2.0-or-later
Summary:        Command interpreter for DBI shells
Url:        https://metacpan.org/release/SQL-Shell
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGUALDRON/SQL-Shell-%{version}.tar.gz
BuildArch:  noarch
%if %{with perl_SQL_Shell_enables_optional_test}
%endif
%if %{with perl_SQL_Shell_enables_optional_test}
%endif
%if %{with perl_SQL_Shell_enables_optional_test}
%endif
Requires:   perl(CGI)
Requires:   perl(Locale::Recode)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::CaptureOutput)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Locale::Recode)
BuildRequires:  perl(Test::Assertions::TestScript)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
SQL::Shell is a command-interpreter API for building shells and batch
scripts. A command-line interface with readline support is included 
as part of the CPAN distribution. See SQL::Shell::Manual for a user
guide. SQL::Shell offers features similar to the mysql or sql*plus
client programs but is database independent.

This package provides the backend SQL::Shell libraries.  For the 
command-line interpreter (sqlsh), please also install the sqlsh package.

%package -n sqlsh
Summary:    Command interpreter for DBI shells
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   perl(IO::Scalar)
Requires:   perl(Pod::Select)
Requires:   perl(Term::ReadLine::Gnu)
%description -n sqlsh
sqlsh is a command-interpreter API for building shells and batch
scripts. sqlsh/SQL::Shell offers features similar to the mysql or 
sql*plus client programs but is database independent.

See the SQL::Shell::Manual manual page for a user guide.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Assertions::TestScript)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SQL-Shell-%{version}
# Correct shebangs
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
rm %{buildroot}%{_libexecdir}/%{name}/t/pod{,_coverage}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles sqlsh usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset ORACLE_HOME PERL_READLINE_MODE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
export UNIT_TEST_DSN='DBI:SQLite:dbname=test.db'
export UNIT_TEST_USER='anything'
export UNIT_TEST_PASS=''
make test
%files -f %{oreon_filedir}/main.list
%files -n sqlsh -f %{oreon_filedir}/sqlsh.list
%files -n perl-SQL-Shell-tests -f %{oreon_filedir}/perl-SQL-Shell-tests.list

%changelog

%autochangelog
