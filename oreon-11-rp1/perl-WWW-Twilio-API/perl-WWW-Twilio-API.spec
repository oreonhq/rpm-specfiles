%global source0_hash 582db53a091f8da3670c037733314f2510af5e8ee0ba42a0e391e2f2e3ca7734

Name:           perl-WWW-Twilio-API
Version:        0.21
Release:        28%{?dist}
Summary:        Accessing Twilio's REST API with Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Twilio-API

Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCOTTW/WWW-Twilio-API-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(LWP::UserAgent) >= 2.03
BuildRequires:  perl(URI::Escape) >= 3.28

# Testing
BuildRequires:  perl(Test::More)

Requires:       perl(List::Util) >= 1.29
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent) >= 2.03
Requires:       perl(URI::Escape) >= 3.28

%{?perl_default_filter}
%global __requires_exclude perl\\(LWP::UserAgent\\)|perl\\(URI::Escape\\)

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

# remove examples
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/WWW/Twilio/examples.pl

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md examples.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
