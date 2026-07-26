%global source0_hash 5236f5f02a7cb22137c8bfb9c645fffea9eb4411f022e00338d6c2aa3e34e891

# Recommend RDF::Trine::Node::Literal::XML for RDFied XML literals
%bcond_without perl_XRD_Parser_enables_literal

Name:           perl-XRD-Parser
Version:        0.201
Release:        19%{?dist}
Summary:        Parse XRD and host-meta files into RDF::Trine models
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XRD-Parser
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XRD-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(Module::Package::RDF)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Link::Parser) >= 0.102
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Object::AUTHORITY)
BuildRequires:  perl(RDF::Trine) >= 0.135
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.70
# Optional run-time:
%if %{with perl_XRD_Parser_enables_literal}
# RDF::Trine::Node::Literal::XML not used at tests
%endif
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
%if %{with perl_XRD_Parser_enables_literal}
Recommends:     perl(RDF::Trine::Node::Literal::XML)
%endif

%description
While XRD has a rather different history, it turns out it can mostly be
thought of as a serialization format for a limited subset of RDF.

This parser ignores the order of Link elements, as RDF is a graph format with
no concept of statements coming in an "order". The XRD spec says that grokking
the order of Link elements is only a SHOULD. That said, if you're concerned
about the order of Link elements, the callback routines allowed by this
package may be of use.

This package aims to be roughly compatible with RDF::RDFa::Parser's interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XRD-Parser-%{version}
# Remove bundled modules
rm -rf inc
perl -i -lne 'print $_ unless m{^inc/}' MANIFEST

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
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
