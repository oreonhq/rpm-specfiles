%global source0_hash 541354fe361c56850cb11261f6ca089a14573fa764792447444ff736ae626206

Name:           perl-Class-DBI
Version:        3.0.17
Release:        53%{?dist}
Summary:        Simple Database Abstraction
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Class-DBI-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
%if ! 0%{?el8}
BuildRequires:  perl-doc
%endif
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Ima::DBI)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Piece::MySQL)
BuildRequires:  perl(UNIVERSAL::moniker)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
Requires:  perl(Scalar::Util)

Provides:       perl(Class::DBI)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-DBI-v%{version}
perldoc -t perlgpl > COPYING
perldoc -t perlartistic > Artistic

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# This test fails because no postgresql and mysql servers are running
# in the build environment.
# make test

%files
%doc Changes COPYING Artistic
%{perl_vendorlib}/Class/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
