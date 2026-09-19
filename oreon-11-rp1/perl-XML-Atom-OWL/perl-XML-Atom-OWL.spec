%global source0_hash 091869f4aa90d2123ae5fa98fb36cea31d7516a57b12efbf01e74e66cf7070b0

# Recommend RDF::Trine::Node::Literal::XML for RDFied XML literals
%bcond_without perl_XML_Atom_OWL_enables_literal

Name:           perl-XML-Atom-OWL
Version:        0.104
Release:        21%{?dist}
Summary:        Parse an Atom file into RDF
# CONTRIBUTING: CC-BY-SA
# COPYRIGHT:    Public Domain
# LICENSE:      GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA and Public Domain - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-Atom-OWL
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-Atom-OWL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Carp) >= 1.00
BuildRequires:  perl(common::sense)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Link::Parser) >= 0.100
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI) >= 1.30
BuildRequires:  perl(XML::LibXML) >= 1.70
# Optional run-time:
# RDF::Trine::Node::Literal::XML not used at tests
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
%if %{with perl_XML_Atom_OWL_enables_literal}
Recommends:     perl(RDF::Trine::Node::Literal::XML)
%endif

%description
This Perl module parses an Atom file into an RDF tree.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Atom-OWL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS examples README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
