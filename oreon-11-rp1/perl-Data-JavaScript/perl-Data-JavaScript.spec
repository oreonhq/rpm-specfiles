%global source0_hash d017d453187e5b01b9e6d73b36acd1163c3acaa90ddc10cd836e471ab12c8899
Name:           perl-Data-JavaScript
Version:        1.16
Release:        1%{?dist}
Summary:        Dump perl data structures into JavaScript code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-JavaScript
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTEMLE/Data-JavaScript-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::Require::Perl)
BuildRequires:  perl(Test2::Tools::PerlCritic)
BuildRequires:  perl(Test2::Tools::Subtest)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is mainly intended for CGI programming, when a perl script
generates a page with client side JavaScript code that needs access to
structures created on the server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-JavaScript-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
