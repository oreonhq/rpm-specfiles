%global source0_hash 8ba24b0b459b01d6c5e5b0408829c7d5dfe47ff79b3548c813759048099b175e
Name:           perl-XML-DOM
Version:        1.46
Release:        28%{?dist}
Summary:        DOM extension to XML::Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-DOM
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-DOM-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(XML::Parser) >= 2.30
Obsoletes:      perl-libxml-enno <= 1.02
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(XML::XQL::Node\\)
Provides:       perl(XML::DOM)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Parser::PerlSAX)
BuildRequires:  perl(XML::RegExp)
BuildRequires:  perl(bytes)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'DOM', that allows XML::Parser to build an Object
Oriented data structure with a DOM Level 1 compliant interface. For a
description of the DOM (Document Object Model), see
<http://www.w3.org/DOM/>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-DOM-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.46-28
- Prepare for Oreon 11 (RP1)
