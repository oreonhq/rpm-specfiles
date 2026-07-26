%global source0_hash f3ffa911f9d59181f1717910ea26620905c298b74dc30f7d4e5139ee3020b8d3

Name:           perl-LWP-Protocol-http10
Version:        6.03
Release:        41%{?dist}
Summary:        Legacy HTTP/1.0 support for LWP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Protocol-http10
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/LWP-Protocol-http10-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6
BuildRequires:  perl(LWP::Protocol) >= 6

Requires:       perl(HTTP::Response) >= 6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Response\\)
Requires:       perl(HTTP::Status) >= 6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Status\\)
Requires:       perl(LWP::Protocol) >= 6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(LWP::Protocol\\)
# Make optional dependency mandatory
Requires:       perl(URI::Escape)

%description
The LWP::Protocol::http10 module provides support for using HTTP/1.0
protocol with LWP. To use it you need to call LWP::Protocol::implementor()
to override the standard handler for http URLs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-Protocol-http10-%{version}

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
