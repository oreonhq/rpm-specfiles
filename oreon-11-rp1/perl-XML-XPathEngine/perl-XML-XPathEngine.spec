%global source0_hash d2fe7bcbbd0beba1444f4a733401e7b8aa5282fad4266d42735dd74582b2e264
%bcond_without perl_XML_XPathEngine_enables_optional_test
Name:           perl-XML-XPathEngine
Version:        0.14
Release:        1%{?dist}
Summary:        Re-usable XPath engine for DOM-like trees
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-XPathEngine
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-XPathEngine-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_XML_XPathEngine_enables_optional_test}
%endif
Requires:       perl(POSIX)
Provides:       perl(XML::XPathEngine)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-XPathEngine-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-34
- Prepare for Oreon 11 (RP1)
