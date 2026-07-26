%global source0_hash 631e161c08ff7afbf9a3fc9b49d1d7946cc89730eb440fc8ed87c589d0e00aee

Name:           perl-DBIx-Class-Candy
Version:        0.005004
Release:        4%{?dist}
Summary:        Sugar for your favorite ORM, DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Class-Candy
Source0:        https://cpan.metacpan.org/authors/id/W/WE/WESM/DBIx-Class-Candy-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(MRO::Compat) >= 0.11
BuildRequires:  perl(Sub::Exporter) >= 0.982
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(namespace::clean) >= 0.18
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(DBIx::Class::Core) >= 0.08123
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
Requires:       perl(Lingua::EN::Inflect)
Requires:       perl(experimental)
Requires:       perl(feature)

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/DBIx*
%{_mandir}/man3/DBIx*

%changelog
%autochangelog
