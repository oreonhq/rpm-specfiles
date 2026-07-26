%global source0_hash a9fffa8e4fde1d643ab67c08da5529167b716907ebf56ca2ef4899b9a43fd0f0

Name:           perl-Net-SMTPS
Version:        0.10
Release:        18%{?dist}
Summary:        SSL/STARTTLS support for Net::SMTP
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SMTPS
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOMO/src/Net-SMTPS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Authen::SASL) >= 2
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL) >= 1
BuildRequires:  perl(Net::Cmd)
BuildRequires:  perl(Net::Config)
BuildRequires:  perl(Net::SMTP) >= 2
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Authen::SASL) >= 2
Requires:       perl(IO::Socket::IP)
Requires:       perl(IO::Socket::SSL) >= 1
Requires:       perl(MIME::Base64)
Requires:       perl(Net::SMTP) >= 2

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Authen::SASL\\)$
%global __requires_exclude %__requires_exclude|^perl\\(IO::Socket::SSL\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::SMTP\\)$
%description
This module implements a wrapper for Net::SMTP, enabling over-SSL/STARTTLS
support. This module inherits all the methods from Net::SMTP. You may use
all the friendly options that came bundled with Net::SMTP. You can control
the SSL usage with the options of new() constructor method. 'doSSL' option
is the switch, and, If you would like to control detailed SSL settings, you
can set SSL_* options that are brought from IO::Socket::SSL. Please see the
document of IO::Socket::SSL about these options detail.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SMTPS-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
