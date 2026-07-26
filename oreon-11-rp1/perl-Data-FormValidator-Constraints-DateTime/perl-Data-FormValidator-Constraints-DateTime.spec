%global source0_hash c3653fddfdfb457cce5f9fdf81309a6a54b32aeb5ff343856f6f32044ac88170

Name:           perl-Data-FormValidator-Constraints-DateTime
Version:        1.11
Release:        44%{?dist}
Summary:        Data::FormValidator constraints for dates and times
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-FormValidator-Constraints-DateTime
Source0:        https://cpan.metacpan.org/authors/id/W/WO/WONKO/Data-FormValidator-Constraints-DateTime-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.36
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 0.23
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::Pg)
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.00
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(CGI)
BuildRequires:  perl(Data::FormValidator) >= 3.61
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(DateTime) >= 0.23
Requires:       perl(DateTime::Format::MySQL)
Requires:       perl(DateTime::Format::Pg)
Requires:       perl(DateTime::Format::Strptime) >= 1.00

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DateTime::Format::Strptime\\)$

%description
This package provides constraint routines for Data::FormValidator for
dealing with dates and times. It provides an easy mechanism for validating
dates of any format (using strptime(3)) and transforming those dates (as
long as you 'untaint' the fields) into valid DateTime objects, or into
strings that would be properly formatted for various database engines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-FormValidator-Constraints-DateTime-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
