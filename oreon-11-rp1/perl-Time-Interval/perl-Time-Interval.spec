%global source0_hash 2acbb108a82fe0793d3470bf9918c4d326b6da28bdae5558f95182bee58e53d0

Name:       perl-Time-Interval
Version:    1.234
Release:    26%{?dist}
Summary:    Perl module that converts time intervals of days, hours, minutes, and seconds
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Time-Interval
Source0:    https://cpan.metacpan.org/authors/id/A/AH/AHICOX/Time-Interval-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Date::Parse) >= 2.20
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test)
Requires:   perl(Date::Parse) >= 2.20

%description
This is a rather simple Perl module for dealing with time intervals. Among
other things, this module can tell you the number of hours, minutes, and
seconds elapsed between two dates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Interval-%{version}
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
