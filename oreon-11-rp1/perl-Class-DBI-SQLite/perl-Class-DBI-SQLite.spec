%global source0_hash c4661b00afb7e53c97ac36e13f34dde43c1a93540a2f4ff97e6182b0c731e4e7

Name:           perl-Class-DBI-SQLite
Version:        0.11
Release:        54%{?dist}
Summary:        Extension to Class::DBI for sqlite
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-SQLite
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Class-DBI-SQLite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-doc
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(lib)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
Requires:  perl(DBD::SQLite)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-SQLite-%{version}
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
