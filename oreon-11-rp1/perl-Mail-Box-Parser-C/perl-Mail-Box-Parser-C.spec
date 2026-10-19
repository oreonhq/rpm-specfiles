%global source0_hash 43e60d05578af0cb946a40db15b544591febf846c2943f3bf93638544382dd2d
Name:           perl-Mail-Box-Parser-C
Version:        4.00
Release:        1%{?dist}
Summary:        Parsing folders for MailBox with C routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box-Parser-C
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-Parser-C-%{version}.tar.gz
Requires:       perl(Mail::Message) >= 4.0
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Mail::Box::Parser)
BuildRequires:  perl(Mail::Message)
BuildRequires:  perl(Mail::Message::Field)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module enables faster folder parsing by using compiled C routines.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Box-Parser-C-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
