%global source0_hash 8e3bc2530b01216188c3aa65acdbd2f59c4e631f3ae085dfc439abd89f8f0acf

Name:           perl-DBICx-TestDatabase 
Summary:        Create a temporary database from a DBIx::Class::Schema 
Version:        0.05
Release:        33%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JROCKWAY/DBICx-TestDatabase-%{version}.tar.gz 
URL:            https://metacpan.org/release/DBICx-TestDatabase
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Runtime
BuildRequires:  perl(DBD::SQLite) >= 1.29
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(DBD::SQLite) >= 1.29
Requires:       perl(SQL::Translator)

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MySchema.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestDatabase\\)

%description
This module creates a temporary SQLite database, deploys your DBIC
schema, and then connects to it. This lets you easily test your DBIC
schema. Since you have a fresh database for every test, you don't have
to worry about cleaning up after your tests, ordering of tests affecting
failure, etc.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBICx-TestDatabase-%{version}
# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

# Help generators to recognize Perl scripts
for F in t/*.t; do
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
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/author
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
