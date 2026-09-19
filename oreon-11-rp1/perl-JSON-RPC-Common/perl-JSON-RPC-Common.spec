%global source0_hash 22062213fdae302159d012c055b7e2006eb527234088d2f216b34eec36167c62

Name:           perl-JSON-RPC-Common
Version:        0.11
Release:        32%{?dist}
Summary:        Perl module for handling JSON-RPC objects
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-RPC-Common
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMCBRIDE/JSON-RPC-Common-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(JSON)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(URI)

%description
This module provides abstractions for JSON-RPC 1.0, 1.1 (both variations) and
2.0 (formerly 1.2) Procedure Call and Procedure Return objects (formerly known
as request and result), along with error objects.
It also provides marshaling objects to convert the model objects into JSON
text and HTTP requests/responses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-RPC-Common-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/JSON/RPC/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
