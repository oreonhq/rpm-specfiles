%global source0_hash a213fa8a7f230f7edb91b9169164935cd5f5d712d5c0ed083a46cd38663bf26d

Name:       perl-Config-ApacheFormat
Version:    1.2
Release:    38%{?dist}
Summary:    Use Apache format config files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Config-ApacheFormat
Source0:    https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/Config-ApacheFormat-%{version}.tar.gz
# Fix a Use of uninitialized value in lc warning, CPAN RT#132271
Patch0:     Config-ApacheFormat-1.2-Fix-a-Use-of-uninitialized-value-in-lc-warning.patch
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MethodMaker) >= 1.08
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Balanced) >= 1.89
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# (Data::Dumper is used only in runtime, not in tests)
Requires:   perl(Class::MethodMaker) >= 1.08
Requires:   perl(Data::Dumper)
Requires:   perl(File::Spec) >= 0.82
Requires:   perl(Text::Balanced) >= 1.89

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Class::MethodMaker|File::Spec|Text::Balanced)\\)$

%description
This Perl module is designed to parse a configuration file in the same syntax
used by the Apache web server (see <http://httpd.apache.org/> for details).
This enables you to build applications which can be easily managed by
experienced Apache administrators.  Also, by using this module, you'll benefit
from the support for nested blocks with built-in parameter inheritance. This
can greatly reduce the amount or repeated information in your configuration
files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-ApacheFormat-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
