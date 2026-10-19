%global source0_hash 631e161c08ff7afbf9a3fc9b49d1d7946cc89730eb440fc8ed87c589d0e00aee
Name:           perl-DBIx-Class-Candy
Version:        0.005004
Release:        1%{?dist}
Summary:        Sugar for your favorite ORM, DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-Candy
Source0:        https://cpan.metacpan.org/authors/id/W/WE/WESM/DBIx-Class-Candy-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Lingua::EN::Inflect)
Requires:       perl(experimental)
Requires:       perl(feature)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx::Class::Candy is a simple sugar layer for definition of DBIx::Class
results. Note that it may later be expanded to add sugar for more
DBIx::Class related things.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-Candy-%{version}

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
