%global source0_hash 47057fd9d2b9b0a9aed3f191d8eb38a761b78276e3a33cb5b51a980627af086b

Name:           perl-XML-LibXML-Debugging
Version:        0.103
Release:        21%{?dist}
Summary:        Get debugging information from XML::LibXML nodes
# COPYRIGHT:    Public Domain
# CONTRIBUTING: CC-BY-SA
# LICENSE:      GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and CC-BY-SA and Public Domain - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-Public-Domain
URL:            https://metacpan.org/release/XML-LibXML-Debugging
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-Debugging-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(HTML::HTML5::Entities)
BuildRequires:  perl(parent)
BuildRequires:  perl(XML::LibXML)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61

%description
This Perl module adds a couple of additional methods to XML::LibXML::Node
objects which are mostly aimed at helping figure out what's going on with
the DOM's name spaces and structure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-LibXML-Debugging-%{version}

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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
