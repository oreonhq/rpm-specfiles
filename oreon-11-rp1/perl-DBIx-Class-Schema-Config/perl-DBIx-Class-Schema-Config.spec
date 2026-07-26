%global source0_hash 83dd6d5f08cf8b708f43341c89d8af0c04b64688cd3df4fa884b71635d1bf30a

Name:           perl-DBIx-Class-Schema-Config
Version:        0.001014
Release:        13%{?dist}
Summary:        Credential Management for DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-Schema-Config
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYMKAT/DBIx-Class-Schema-Config-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Config::Any) >= 0.23
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(URI)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class) >= 0.08100
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Config::Any) >= 0.23
Requires:       perl(DBIx::Class) >= 0.08100

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Config::Any\\)\s*$

# Filter modules bundled for tests
%global __requires_exclude %{__requires_exclude}|perl\\(DBIx::Class::Schema::Config::.*\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
DBIx::Class::Schema::Config is a subclass of DBIx::Class::Schema that
allows the loading of credentials & configuration from a file. The actual
code itself would only need to know about the name used in the
configuration file. This aims to make it simpler for operations teams to
manage database credentials.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)
Requires:       perl(DBI)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-Schema-Config-%{version}

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
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
