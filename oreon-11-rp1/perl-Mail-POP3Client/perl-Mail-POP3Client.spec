%global source0_hash b16ef2149b6e3573873f1e590e4d51366c5994b8b5315df16925d17b89e24901

Name:           perl-Mail-POP3Client
Version:        2.21
Release:        12%{?dist}
Summary:        Perl 5 module to talk to a POP3 (RFC1939) server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-POP3Client
Source0:        https://cpan.metacpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# For the tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00

%description
This module implements an Object-Oriented interface to a POP3 server. It
implements RFC1939 (http://www.faqs.org/rfcs/rfc1939.html)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-POP3Client-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes FAQ README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
