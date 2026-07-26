%global source0_hash 1f63ba72923992ba6015fe94d152b291e1f0f79e6f387f5345d5571a352a82b5

Name:           perl-XML-LibXML-Devel-SetLineNumber
Version:        0.002
Release:        32%{?dist}
Summary:        Set the line number for an XML::LibXML::Node
# README:       GPL+ or Artistic
# COPYRIGHT:    Public Domain
# CONTRIBUTING: (GPL+ or Artistic) or CC-BY-SA
# Automatically converted from old format: (GPL+ or Artistic) and ((GPL+ or Artistic) or CC-BY-SA) and Public Domain - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ((GPL-1.0-or-later OR Artistic-1.0-Perl) OR LicenseRef-Callaway-CC-BY-SA) AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-LibXML-Devel-SetLineNumber
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-Devel-SetLineNumber-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  pkgconfig(libxml-2.0)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.3
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.90
BuildRequires:  perl(XML::LibXML::Devel)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(XML::LibXML) >= 1.90

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::LibXML\\)$

%description
If you are, say, writing a parser for a non-XML format that happens to have an
XML-like data model, then you might wish to parse your format into an
XML::LibXML document with elements, attributes and so on. And you might want
all those nodes to return the correct line numbers when the "line_number"
method is called on them. This Perl module allows you to set the line number.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-LibXML-Devel-SetLineNumber-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/XML*
%{_mandir}/man3/*

%changelog
%autochangelog
