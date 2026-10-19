%global source0_hash 5019f9a4f272a57febe8064061319a0db59591a180d12fddda0fdb73228e4ede
Name:           perl-WWW-Salesforce
Version:        0.304
Release:        1%{?dist}
Summary:        Simple abstraction layer between SOAP::Lite and Salesforce.com
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Salesforce
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/WWW-Salesforce-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IO::Socket::SSL) >= 1.94
Requires:       perl(LWP::Protocol::https) >= 6.00
Requires:       perl(SOAP::Lite) >= 1.0
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(SOAP::Lite\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
