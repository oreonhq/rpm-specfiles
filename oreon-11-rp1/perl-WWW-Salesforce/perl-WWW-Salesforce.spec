%global source0_hash 5019f9a4f272a57febe8064061319a0db59591a180d12fddda0fdb73228e4ede

Name:           perl-WWW-Salesforce
Version:        0.304
Release:        12%{?dist}
Summary:        Simple abstraction layer between SOAP::Lite and Salesforce.com
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Salesforce
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/WWW-Salesforce-%{version}.tar.gz
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
BuildRequires:  perl(DateTime)
BuildRequires:  perl(IO::Socket::SSL) >= 1.94
BuildRequires:  perl(LWP::Protocol::https) >= 6.00
BuildRequires:  perl(SOAP::Lite) >= 1.0
BuildRequires:  perl(URI)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
Requires:       perl(IO::Socket::SSL) >= 1.94
Requires:       perl(LWP::Protocol::https) >= 6.00
Requires:       perl(SOAP::Lite) >= 1.0

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(SOAP::Lite\\)$

%description
This class provides a simple abstraction layer between SOAP::Lite and
Salesforce.com. Because SOAP::Lite does not support complexTypes, and
document/literal encoding is limited, this module works around those
limitations and provides a more intuitive interface a developer can
interact with.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Salesforce-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
