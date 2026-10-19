%global source0_hash 18acf7e589ca4cca9cde47609b536c9d823c8562d1aa5210c168e5eb1b8e4f9e
Name:           perl-Test-PostgreSQL
Version:        1.29
Release:        12%{?dist}
Summary:        PostgreSQL runner for Perl tests
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-PostgreSQL
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJC/Test-PostgreSQL-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DBD::Pg)
Requires:       postgresql-server
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::SharedFork\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Tie::Hash::Method)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(User::pwent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  postgresql-server
# /oreon:deps
%description
The Test::PostgreSQL Perl module automatically setups a PostgreSQL instance in
a temporary directory, and destroys it when the Perl script exits.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::SharedFork) >= 0.06
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-PostgreSQL-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset POSTGRES_HOME TEST_POSTGRESQL_PRESERVE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset POSTGRES_HOME TEST_POSTGRESQL_PRESERVE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-PostgreSQL-tests -f %{oreon_filedir}/perl-Test-PostgreSQL-tests.list

%changelog

%autochangelog
