%global source0_hash 58bcc6925daa78d80b40f436d9219aadce201dcfeb9c71e933bcda30c47d597c

Name:           perl-Template-Toolkit-Simple
Version:        0.31
Release:        41%{?dist}
Summary:        Simple interface to Template Toolkit
# inc/Text/Diff.pm (not in binary package):     GPLv2+ or Artistic
# rest:     GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Toolkit-Simple
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Template-Toolkit-Simple-%{version}.tar.gz
# Old TestML API moved to TestML1 name space, bug #1650156
Patch0:         Template-Toolkit-Simple-0.31-Old-TestML-API-moved-to-TestML1-name-space.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Template) >= 2.22
BuildRequires:  perl(Template::Constants)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::XS) >= 0.37
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
# Break dependency cycle: perl-Template-Toolkit-Simple → perl-TestML1
# → perl-Template-Toolkit-Simple
BuildRequires:  perl(lib)
BuildRequires:  perl(TestML1)
BuildRequires:  perl(TestML1::Bridge)
BuildRequires:  perl(TestML1::Util)
%endif
Requires:       perl(Carp)
Requires:       perl(JSON::XS)
Requires:       perl(Template) >= 2.22
Requires:       perl(warnings)
Requires:       perl(XML::Simple)
Requires:       perl(YAML::XS) >= 0.37

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Template|YAML::XS)\\)$

%description
This Perl module is a simple wrapper around Template Toolkit. It exports
a function called `tt' which returns a new Template::Toolkit::Simple object.
The object supports method calls for setting all the Template Toolkit options.

This module also installs a program called `tt-render' which you can use from
the command line to render templates with all the power of the Perl object.
All of the object methods become command line arguments in the command line
version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Toolkit-Simple-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST
# Fix shellbang
sed -i -e '1 s,^#!/usr/bin/env perl,#!perl,' bin/tt-render

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
%if %{defined perl_bootstrap}
# Break dependency cycle: perl-Template-Toolkit-Simple → perl-TestML1
# → perl-Template-Toolkit-Simple
make test TEST_FILES="$(find t -name '*.t' \
    \! -exec grep -q -e 'use TestML1' {} \; -print | tr \"\\n\" ' ')"
%else
make test
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/tt-render

%changelog
%autochangelog
