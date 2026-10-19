%global source0_hash 1f63ba72923992ba6015fe94d152b291e1f0f79e6f387f5345d5571a352a82b5
Name:           perl-XML-LibXML-Devel-SetLineNumber
Version:        0.002
Release:        1%{?dist}
Summary:        Set the line number for an XML::LibXML::Node
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ((GPL-1.0-or-later OR Artistic-1.0-Perl) OR LicenseRef-Callaway-CC-BY-SA) AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-LibXML-Devel-SetLineNumber
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-Devel-SetLineNumber-%{version}.tar.gz
Requires:       perl(XML::LibXML) >= 1.90
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::LibXML\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Devel)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
