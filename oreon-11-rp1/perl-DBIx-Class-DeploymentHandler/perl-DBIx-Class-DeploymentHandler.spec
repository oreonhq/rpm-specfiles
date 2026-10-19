%global source0_hash 141f3a8047af0b32fd804412557f7aabce79a6b1e6e4147e46dea735a839eb2c
Name:           perl-DBIx-Class-DeploymentHandler
Version:        0.002235
Release:        1%{?dist}
Summary:        Extensible DBIx::Class deployment
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-DeploymentHandler
Source0:        https://cpan.metacpan.org/authors/id/M/MM/MMCCLIMON/DBIx-Class-DeploymentHandler-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DBIx::Class::Schema::Loader)
Requires:       perl(Log::Contextual::Role::Router)
Requires:       perl(Type::Tiny)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Contextual)
BuildRequires:  perl(Log::Contextual::Role::Router)
BuildRequires:  perl(Log::Contextual::WarnLogger)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(SQL::SplitStatement)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(SQL::Translator::Diff)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Text::Brew)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(YAML)
BuildRequires:  perl(aliased)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx::Class::DeploymentHandler is, as its name suggests, a tool for deploying
and upgrading databases with DBIx::Class. It is designed to be much more
flexible than DBIx::Class::Schema::Versioned, hence the use of Moose and lots
of roles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-DeploymentHandler-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
