%global source0_hash 5ea6cc89992c2d3f3ab2e31eed97dcbad3e7ea53fcca017c528d1ca9212bb15a

Name:           perl-Class-DBI-Pager
Version:        0.08
Release:        53%{?dist}
Summary:        Pager utility for Class::DBI
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Pager
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Class-DBI-Pager-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-doc
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(Data::Page)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Pager-%{version}
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
