# Perform optional tests
%bcond_without perl_XML_XPathEngine_enables_optional_test

Name:           perl-XML-XPathEngine
Version:        0.14
Release:        34%{?dist}
Summary:        Re-usable XPath engine for DOM-like trees
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-XPathEngine
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/XML-XPathEngine-0.14.tar.gz
# oreon url source checksums begin
%global source0_sha256 d2fe7bcbbd0beba1444f4a733401e7b8aa5282fad4266d42735dd74582b2e264
%global source0_file XML-XPathEngine-0.14.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
# POSIX not used in tests
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
%if %{with perl_XML_XPathEngine_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(POSIX)

%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/XML-XPathEngine-0.14.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d2fe7bcbbd0beba1444f4a733401e7b8aa5282fad4266d42735dd74582b2e264" || { echo "oreon: Source0 SHA256 mismatch for XML-XPathEngine-0.14.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n XML-XPathEngine-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-34
- Prepare for Oreon 11 (RP1)
