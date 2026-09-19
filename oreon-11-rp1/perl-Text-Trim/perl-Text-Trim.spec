%global source0_hash d5878a9079d33cd1766cf6abc44cd625bd00a0213d2ce8e3143fe6944abaaa11

Name:           perl-Text-Trim
Version:        1.04
Release:        4%{?dist}
Summary:        Remove leading and/or trailing whitespace from strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Trim
Source0:        https://www.cpan.org/modules/by-module/Text/Text-Trim-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)

%description
This module provides functions for removing leading and/or trailing
whitespace from strings. It is basically a wrapper around some simple
regexes with a flexible context-based interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Trim-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README README.md
%license LICENSE
%{perl_vendorlib}/Text/*
%{_mandir}/man3/Text::Trim.3pm*

%changelog
%autochangelog
