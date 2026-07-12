%global source0_hash d542d17d75ce93631de8ba2156da0e0b58a755c409cd4a0d27a3873a26712ce2

Name:           perl-Regexp-IPv6
Version:        0.03
Release:        43%{?dist}
Summary:        Regular expression for IPv6 addresses
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Regexp-IPv6
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Regexp-IPv6-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

Provides:       perl(Regexp::IPv6)
%description
This module exports the $IPv6_re regular expression that matches any valid
IPv6 address as described in "RFC 2373 - 2.2 Text Representation of
Addresses" but ::. Any string not compliant with such RFC will be rejected.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Regexp-IPv6-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
