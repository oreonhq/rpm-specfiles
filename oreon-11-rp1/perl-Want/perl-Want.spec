%global source0_hash b4e4740b8d4cb783591273c636bd68304892e28d89e88abf9273b1de17f552f7
Name:		perl-Want
Version:	0.29
Release:        1%{?dist}
Summary:        Perl module implementing a generalisation of wantarray
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Want
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBIN/Want-%{version}.tar.gz
Provides:       perl(Want)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module generalises the mechanism of the wantarray
function, allowing a function to determine in some detail
how its return value is going to be immediately used.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Want-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="${RPM_OPT_FLAGS}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} "$RPM_BUILD_ROOT"/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
