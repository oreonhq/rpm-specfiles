%global source0_hash 353115b1987824117d86bef585898e0dfa122ccf1716f58ad6411bf872570ab9

Name:             perl-Mail-SPF-Iterator
Summary:          Iterative SPF lookup
Version:          1.121
Release:          4%{?dist}
License:          GPL-1.0-or-later OR Artistic-1.0-Perl
URL:              https://metacpan.org/release/Mail-SPF-Iterator
Source0:          https://cpan.metacpan.org/authors/id/S/SU/SULLR/Mail-SPF-Iterator-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    make
BuildRequires:    perl-generators
BuildRequires:    perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:    perl(base)
BuildRequires:    perl(constant)
BuildRequires:    perl(Data::Dumper)
BuildRequires:    perl(Exporter)
BuildRequires:    perl(fields)
BuildRequires:    perl(Net::DNS) >= 0.62
BuildRequires:    perl(Net::DNS::Resolver)
BuildRequires:    perl(Socket)
BuildRequires:    perl(Socket6)
BuildRequires:    perl(strict)
BuildRequires:    perl(URI)
BuildRequires:    perl(URI::Escape)
BuildRequires:    perl(warnings)

Requires:         perl(Net::DNS) >= 0.62
Requires:         perl(URI)

%{?perl_default_filter}

%description
This module provides an iterative resolving of SPF records. Contrary to
Mail::SPF, which does blocking DNS lookups, this module just returns the
DNS queries and later expects the responses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-SPF-Iterator-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README samples
%license COPYRIGHT
%{_mandir}/man3/Mail::SPF::Iterator*
%{perl_vendorlib}/Mail

%changelog
%autochangelog
