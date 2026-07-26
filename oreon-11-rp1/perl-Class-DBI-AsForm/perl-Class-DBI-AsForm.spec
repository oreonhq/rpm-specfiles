%global source0_hash 5998564bebc02735892fc1751ee14760d1d1719617f931579c9cc18ebd6d8c09

Name:           perl-Class-DBI-AsForm
Version:        2.42
Release:        58%{?dist}
Summary:        Produce HTML form elements for database columns
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-AsForm
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Class-DBI-AsForm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-doc
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(Class::DBI::Plugin::Type)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Element)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(warnings)
Requires:       perl(Class::DBI)
Patch0:		perl-Class-DBI-AsForm-fix01test.patch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-AsForm-%{version}
%patch -P0 -p1
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
make test

%files
%doc Artistic COPYING Changes
%{perl_vendorlib}/Class/DBI
%{_mandir}/man3/*.3*

%changelog
%autochangelog
