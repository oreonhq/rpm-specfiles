%global source0_hash 8af38ed90d69469f0a28c2e9f2f34fe2d03b00654c1819aa4cbc7af215d68390

Name:           perl-Class-DBI-FromCGI
Version:        1.00
Release:        53%{?dist}
Summary:        Update Class::DBI data using CGI::Untaint
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-FromCGI
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMTM/Class-DBI-FromCGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-doc
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(CGI::Untaint)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Pod::Perldoc)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
Requires:  perl(Class::DBI), perl(CGI::Untaint)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-FromCGI-%{version}
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
