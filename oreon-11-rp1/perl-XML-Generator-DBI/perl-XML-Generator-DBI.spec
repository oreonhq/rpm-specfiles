%global source0_hash fd04a6e43d59dfbfc2b6d2e5819d0031117d7e97dc52775f861430a5f9e62443

Name:           perl-XML-Generator-DBI
Version:        1.00    
Release:        54%{?dist}
Summary:        Generate SAX events from SQL queries

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Generator-DBI
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-Generator-DBI-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::SAX::Base)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(DBD::SQLite) >= 0.27
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Writer)

%description
This module generates SAX events from SQL queries against a DBI connection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Generator-DBI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::Generator::DBI.3pm*

%changelog
%autochangelog
