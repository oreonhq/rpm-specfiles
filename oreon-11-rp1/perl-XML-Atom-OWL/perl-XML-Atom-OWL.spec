%global source0_hash 091869f4aa90d2123ae5fa98fb36cea31d7516a57b12efbf01e74e66cf7070b0
%bcond_without perl_XML_Atom_OWL_enables_literal
Name:           perl-XML-Atom-OWL
Version:        0.104
Release:        1%{?dist}
Summary:        Parse an Atom file into RDF
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-Atom-OWL
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-Atom-OWL-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_XML_Atom_OWL_enables_literal}
Recommends:     perl(RDF::Trine::Node::Literal::XML)
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Link::Parser)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
