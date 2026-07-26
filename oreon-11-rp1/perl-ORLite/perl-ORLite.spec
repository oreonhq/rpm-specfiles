%global source0_hash dd4bc23ab4c87c5096a406aaa03c75e2f9e48f858c7283d84cff8af24b82defa

Name:           perl-ORLite
Summary:        Extremely light weight SQLite-specific ORM
Version:        2.00
Release:        7%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/ORLite-%{version}.tar.gz
# Normalize shebangs, not suitable for the upstream
Patch0:         ORLite-1.99-Normalize-shebangs.patch
URL:            https://metacpan.org/release/ORLite
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite) >= 1.27
BuildRequires:  perl(DBI) >= 1.607
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Params::Util) >= 1.00
# Optional run-time, test it while building
BuildRequires:  perl(Class::XSAccessor) >= 1.05
BuildRequires:  perl(Class::XSAccessor::Array) >= 1.05
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional tests
# CPAN::Meta and CPAN::Meta::Prereqs are not helpful
Requires:       perl(File::Remove)
Requires:       perl(File::Temp)

%{?perl_default_filter}
# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(LocalTest\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((LocalTest|MyDB::TableOne)\\)

%description
SQLite is a light weight single file SQL database that provides
an excellent platform for embedded storage of structured data.
However, while it is superficially similar to a regular server-side
SQL database, SQLite has some significant attributes that make using
it like a traditional database difficult. For example, SQLite is
extremely fast to connect to compared to server databases 
(1000 connections per second is not unknown) and is particularly bad
at concurrency, as it can only lock transactions at a database-wide level.
This role as a super-fast internal data store can clash with the roles and
designs of traditional object-relational modules like Class::DBI or 
DBIx::Class. What this situation would seem to need is an object-relation
system that is designed specifically for SQLite and is aligned with its
idiosyncrasies. ORLite is an object-relation system specifically
for SQLite that follows many of the same principles as the ::Tiny
series of modules and has a design that aligns directly to the capabilities
of SQLite.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Class::XSAccessor) >= 1.05
Requires:       perl(Class::XSAccessor::Array) >= 1.05

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ORLite-%{version}
# Correct permissions
chmod a+x t/*.t t/08_prune.pl
# Correct end of lines
perl -i -pe 's/\r\n$/\n/' t/08_prune.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Many tests write into CWD, or just open an existing database read-write.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset AUTHOR_TESTING
prove
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
# Not parallel safe
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/ORLite.pm
%{_mandir}/man3/ORLite.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
