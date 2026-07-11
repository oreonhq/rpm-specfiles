%global source0_hash e3813cec9f108fa5c0be66e08c1986bfba4d242151b0f9f4ec5e0c5e17108c4c

Name:           perl-Any-URI-Escape
Version:        0.01
Release:        38%{?dist}
Summary:        Load URI::Escape::XS preferentially over URI::Escape
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Any-URI-Escape
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/Any-URI-Escape-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Exporter)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)
Requires:       perl(URI::Escape)

%{?perl_default_filter}

%description
URI::Escape is great, but URI::Escape::XS is faster. This module loads
URI::Escape::XS and imports the two most common methods if XS is installed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Any-URI-Escape-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Any*
%{_mandir}/man3/*

%changelog
%autochangelog
