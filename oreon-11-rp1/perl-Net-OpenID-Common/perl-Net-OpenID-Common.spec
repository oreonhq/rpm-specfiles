%global source0_hash ab4e97d74a47710e0db4ac0c822f7fdf622af86a60a52ba72255a889c29dabc9

Name:           perl-Net-OpenID-Common
Version:        1.20
Release:        29%{?dist}
Summary:        Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-OpenID-Common
Source0:        https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Common-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::DH::GMP) >= 0.00011
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(fields)
BuildRequires:  perl(HTML::Parser) >= 3.40
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Simple)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(CGI)
Requires:       perl(Crypt::DH::GMP) >= 0.00011
Requires:       perl(HTML::Parser) >= 3.40
Requires:       perl(HTTP::Message) >= 5.814
Requires:       perl(Storable)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Crypt::DH::GMP\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(HTML::Parser\\)$

%description
The Consumer and Server implementations share a few libraries which live
with this module. This module is here largely to hold the version number
and this documentation, though it also incorporates some utility functions
inherited from previous versions of Net::OpenID::Consumer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-OpenID-Common-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
