%global source0_hash 2acbb108a82fe0793d3470bf9918c4d326b6da28bdae5558f95182bee58e53d0
Name:       perl-Time-Interval
Version:    1.234
Release:        26%{?dist}
Summary:        Perl module that converts time intervals of days, hours, minutes, and seconds
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Time-Interval
Source0:        https://cpan.metacpan.org/authors/id/A/AH/AHICOX/Time-Interval-%{version}.tar.gz
BuildArch:  noarch
Requires:   perl(Date::Parse) >= 2.20
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
