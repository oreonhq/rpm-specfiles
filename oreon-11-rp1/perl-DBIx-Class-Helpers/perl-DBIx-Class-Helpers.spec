%global source0_hash a42b61c42865cbdb2e95b29c3951ef255c4d72c5c7332a402d7eedc09dcdeba1

Name:           perl-DBIx-Class-Helpers
Version:        2.037000
Release:        4%{?dist}
Summary:        A collection of various components for DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Class-Helpers
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/DBIx-Class-Helpers-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Carp::Clan) >= 6.04
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class) >= 0.0826
BuildRequires:  perl(DBIx::Class::Candy) >= 0.003001
BuildRequires:  perl(DBIx::Class::Candy::Exports)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Row)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Introspector) >= 0.001002
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased) >= 0.34
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::clean) >= 0.23
BuildRequires:  perl(parent)
# test requirements
BuildRequires:  perl(B)
BuildRequires:  perl(DBIx::Class::Candy::ResultSet)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Devel::Dwarn)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Roo) >= 1.003
BuildRequires:  perl(Text::Brew)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc Changes CONTRIBUTING.md README
%license LICENSE
%{perl_vendorlib}/DBIx*
%{_mandir}/man3/DBIx*

%changelog
%autochangelog
