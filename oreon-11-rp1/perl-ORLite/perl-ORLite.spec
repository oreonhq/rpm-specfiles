%global source0_hash dd4bc23ab4c87c5096a406aaa03c75e2f9e48f858c7283d84cff8af24b82defa
Name:           perl-ORLite
Summary:        Extremely light weight SQLite-specific ORM
Version:        2.00
Release:        7%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/ORLite-%{version}.tar.gz
Patch0:         ORLite-1.99-Normalize-shebangs.patch
URL:            https://metacpan.org/release/ORLite
BuildArch:      noarch
Requires:       perl(File::Remove)
Requires:       perl(File::Temp)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(LocalTest\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((LocalTest|MyDB::TableOne)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Class::XSAccessor::Array)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset AUTHOR_TESTING
prove
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-ORLite-tests -f %{oreon_filedir}/perl-ORLite-tests.list

%changelog

%autochangelog
