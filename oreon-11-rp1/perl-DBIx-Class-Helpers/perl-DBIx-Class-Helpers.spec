%global source0_hash a42b61c42865cbdb2e95b29c3951ef255c4d72c5c7332a402d7eedc09dcdeba1
Name:           perl-DBIx-Class-Helpers
Version:        2.037000
Release:        1%{?dist}
Summary:        A collection of various components for DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-Helpers
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/DBIx-Class-Helpers-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Candy)
BuildRequires:  perl(DBIx::Class::Candy::Exports)
BuildRequires:  perl(DBIx::Class::Candy::ResultSet)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Row)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Introspector)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(Devel::Dwarn)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Roo)
BuildRequires:  perl(Text::Brew)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This perl distribution contains a collection of various helper components
for DBIx::Class.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-Helpers-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
