%global source0_hash 33f025e9b10956b9a58ef01774b92b790aacca5fb00b1c755ada77ad4e5c7d3b

Name:           perl-Mail-MboxParser
Version:        0.55
Release:        45%{?dist}
Summary:        Read-only access to UNIX-mailboxes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-MboxParser
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Mail-MboxParser-%{version}.tar.gz
# Bug #715505, submitted to upstream
Patch0:         %{name}-0.55-Fix-garbled-attachment-name-RT-66576.patch
# Define POD encoding, CPAN RT#85805
Patch1:         %{name}-0.55-pod-encoding.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(MIME::Tools) >= 5
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(vars)
# Optional test
BuildRequires:  perl(Encode)
BuildRequires:  perl(Mail::Mbox::MessageParser)
BuildRequires:  perl(MIME::Words)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(utf8)
Requires:       perl(MIME::Tools) >= 5
Requires:       perl(Mail::Mbox::MessageParser)

%{?perl_default_filter}

%description
This module attempts to provide a simplified access to standard UNIX-
mailboxes. It offers only a subset of methods to get 'straight to the
point'. More sophisticated things can still be done by invoking any method
from MIME::Tools on the appropriate return values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-MboxParser-%{version}
%patch -P0 -p1 -b .attachment_name
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changelog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
