%global source0_hash ab4e97d74a47710e0db4ac0c822f7fdf622af86a60a52ba72255a889c29dabc9
Name:           perl-Net-OpenID-Common
Version:        1.20
Release:        29%{?dist}
Summary:        Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-OpenID-Common
Source0:        https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Common-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI)
Requires:       perl(Crypt::DH::GMP) >= 0.00011
Requires:       perl(HTML::Parser) >= 3.40
Requires:       perl(HTTP::Message) >= 5.814
Requires:       perl(Storable)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Crypt::DH::GMP\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(HTML::Parser\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::DH::GMP)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
