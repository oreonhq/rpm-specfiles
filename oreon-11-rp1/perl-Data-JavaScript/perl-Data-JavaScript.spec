%global source0_hash d017d453187e5b01b9e6d73b36acd1163c3acaa90ddc10cd836e471ab12c8899

Name:           perl-Data-JavaScript
Version:        1.16
Release:        2%{?dist}
Summary:        Dump perl data structures into JavaScript code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-JavaScript
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTEMLE/Data-JavaScript-%{version}.tar.gz
BuildArch:      noarch
# bnuild requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Encode)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
# test requirements
BuildRequires:  perl(Test2::Require::Perl)
BuildRequires:  perl(Test2::Tools::Subtest)
BuildRequires:  perl(Test2::Tools::PerlCritic)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc CHANGES CONTRIBUTING.md README.md TODO
%license LICENSE
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
