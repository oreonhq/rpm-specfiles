%global source0_hash abdd1d3eec4ca4fcae5f152b40bcaa862e3c806e07e4aa9123757f6aa48b9dd6

Name:           perl-ExtUtils-F77
Version:        1.26
Release:        15%{?dist}
Summary:        Simple interface to F77 libs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-F77
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/ExtUtils-F77-1.26.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  gcc-gfortran

%description
This module tries to figure out how to link C programs with Fortran
subroutines on your system. Basically one must add a list of Fortran
runtime libraries. The problem is their location and name varies with each
OS/compiler combination!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-F77-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
