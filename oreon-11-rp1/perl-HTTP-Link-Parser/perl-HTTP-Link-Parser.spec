%global source0_hash b3dd12eba6033521e802839c04d0f15a09b0244b784469ff8870e3e431ae45d2
%bcond_without perl_HTTP_Link_Parser_enables_rdf
Name:           perl-HTTP-Link-Parser
Version:        0.200
Release:        21%{?dist}
Summary:        Parse HTTP Link headers
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/HTTP-Link-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTTP-Link-Parser-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_HTTP_Link_Parser_enables_rdf}
%endif
Requires:       perl(Exporter)
%if %{with perl_HTTP_Link_Parser_enables_rdf}
Requires:       perl(RDF::Trine) >= 0.135
%endif
Requires:       perl(warnings)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTTP::Link::Parser parses HTTP "Link" headers found in an HTTP::Response
object. Headers should conform to the format described in RFC 5988.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Link-Parser-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
