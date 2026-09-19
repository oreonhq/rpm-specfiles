%global source0_hash f787efaf9b8dcd1b51085f190acdaae155007a78ba668ffe40d56226f5f2b488

Name:           perl-XML-Smart
Version:        1.79
Release:        36%{?dist}
Summary:        Smart, easy and powerful way to access/create XML files/data
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/XML-Smart
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMHARISH/XML-Smart-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
# Devel::Cycle not used at tests
# Encode not used with current Perl
BuildRequires:  perl(Exporter)
# LWP not used at tests
# LWP::UserAgent not used at tests
BuildRequires:  perl(Object::MultiType) >= 0.03
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(open)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::Pod) >= 1.22
# Test::Pod::Coverage 1.08 not used
Requires:       perl(Data::Dumper)
Requires:       perl(Devel::Cycle)
Requires:       perl(LWP)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Object::MultiType) >= 0.03

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Object::MultiType\\)$

%description
This module provides an easy way to access/create XML data. It's based on a
HASH tree created from the XML data, and enables dynamic access to it
through the standard Perl syntax for Hash and Array, without necessarily
caring about which you are working with. In other words, each point in the
tree works as a Hash and an Array at the same time!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Smart-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/XML*
%{_mandir}/man3/XML*

%changelog
%autochangelog
