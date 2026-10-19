%global source0_hash eb54cc23cdec860d3ad8ac8a697cbf038d0dec95229912d975c301890ca83ee2
Name:		perl-Test-XML
Version:	0.08
Release:        1%{?dist}
Summary:        Compare XML in perl tests
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-XML
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-XML-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(XML::LibXML)
Requires:	perl(XML::XPath)
Provides:       perl(Test::XML)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::SAX::Writer)
BuildRequires:  perl(XML::SemanticDiff)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module contains generic XML testing tools. Functions include:

is_xml(GOT, EXPECTED [, TESTNAME ])

  This function compares GOT and EXPECTED, both of which are strings of XML.
  The comparison works semantically and will ignore differences in syntax
  that are meaningless in xml, such as different quote characters for
  attributes, order of attributes or empty tag styles. It returns true or
  false, depending upon test success.

isnt_xml(GOT, MUST_NOT_BE [, TESTNAME ])

  This function is similar to is_xml(), except that it will fail if GOT and
  MUST_NOT_BE are identical.

is_well_formed_xml(XML [, TESTNAME ])

  This function determines whether or not a given XML string is parsable as
  XML.

is_good_xml(XML [, TESTNAME ])

    This is an alias for is_well_formed_xml().

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-XML-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.08-33
- Prepare for Oreon 11 (RP1)
