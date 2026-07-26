%global source0_hash 402d4db8300b3d271632f4995e0ade329d89280a7e47f2badf8b38af6e5569af

Name:       perl-IO-TieCombine 
Version:    1.005
Release:    30%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Produce tied (and other) separate but combined variables 
Url:        https://metacpan.org/release/IO-TieCombine
Source:     https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IO-TieCombine-%{version}.tar.gz 
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Symbol)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96

%description
This package allows you to tie separate variables into a combined whole, using
ties and other magic.  This can be very useful when, say, you want a unified
output from various different things that return data in different ways
(STDIN/ERR, scalars, handles, etc).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-TieCombine-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
