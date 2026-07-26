%global source0_hash 6fd344111a0bf5a62e0b88409f096c669cbe0f14fd3fefdf2e385e6c97e9de7b

Name:           perl-Class-DBI-mysql
Version:        1.00
Release:        54%{?dist}
Summary:        Extensions to Class::DBI for MySQL
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-mysql
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Class-DBI-mysql-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-doc
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Piece::MySQL)
Requires:  perl(Class::DBI), perl(DBD::mysql), perl(Time::Piece::MySQL)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-mysql-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Needs a running mysql server.
#make test

%files
%doc Artistic COPYING Changes
%{perl_vendorlib}/Class/DBI
%{_mandir}/man3/*.3*

%changelog
%autochangelog
