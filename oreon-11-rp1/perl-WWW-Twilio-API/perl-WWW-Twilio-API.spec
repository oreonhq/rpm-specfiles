%global source0_hash 582db53a091f8da3670c037733314f2510af5e8ee0ba42a0e391e2f2e3ca7734
Name:           perl-WWW-Twilio-API
Version:        0.21
Release:        28%{?dist}
Summary:        Accessing Twilio's REST API with Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Twilio-API
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCOTTW/WWW-Twilio-API-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(List::Util) >= 1.29
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent) >= 2.03
Requires:       perl(URI::Escape) >= 3.28
%{?perl_default_filter}
%global __requires_exclude perl\\(LWP::UserAgent\\)|perl\\(URI::Escape\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
WWW::Twilio::API aims to make connecting to and making REST calls on the
Twilio API easy, reliable, and enjoyable.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Twilio-API-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/WWW/Twilio/examples.pl
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
