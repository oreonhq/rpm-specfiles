%global source0_hash 21ef24256842ca43c6942c63bba692f288c0a173c1fd3beeb4b30f037439839b

Name:           perl-SQL-Interp
Version:        1.28
Release:        3%{?dist}
Summary:        Interpolate Perl variables into SQL statements
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Interp
Source0:        https://cpan.metacpan.org/authors/id/Y/YO/YORHEL/SQL-Interp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI) >= 1
BuildRequires:  perl(Exporter)
# perl(Filter::Simple)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# perl(Text::Balanced) >= 1.87
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(DBI) >= 1

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(DBI::db)\s*$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(DBD::Mock)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(t::lib.pl\\)

%description
SQL::Interp converts a list of intermixed SQL fragments and variable
references into a conventional SQL string and list of bind values suitable
for passing onto DBI. This simple technique creates database calls that are
simpler to create and easier to read, while still giving you full access to
custom SQL.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Interp-%{version}

%build
perl Build.PL installdirs=vendor
# Help file to recognise the Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Remove author/release tests
rm t/pod.t

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
./Build test

%files
%doc Changes ex README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
