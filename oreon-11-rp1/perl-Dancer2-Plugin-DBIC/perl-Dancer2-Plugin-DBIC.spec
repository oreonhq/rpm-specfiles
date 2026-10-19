%global source0_hash 521166565f8ca2e4e816cb192c764cf268104b3389278f7651229b6d9bdfa6f9
Name:           perl-Dancer2-Plugin-DBIC
Version:        0.0100
Release:        25%{?dist}
Summary:        DBIx::Class interface for Dancer2 applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dancer2-Plugin-DBIC
Source0:        https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/Dancer2-Plugin-DBIC-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBICx::Sugar)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(Dancer2)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This plugin makes it very easy to create Dancer2 applications that
interface with databases. It automatically exports the keyword schema which
returns a DBIx::Class::Schema object. You just need to configure your
database connection information. For performance, schema objects are cached
in memory and are lazy loaded the first time they are accessed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer2-Plugin-DBIC-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
