%global source0_hash 33f025e9b10956b9a58ef01774b92b790aacca5fb00b1c755ada77ad4e5c7d3b
Name:           perl-Mail-MboxParser
Version:        0.55
Release:        45%{?dist}
Summary:        Read-only access to UNIX-mailboxes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-MboxParser
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPARSEVAL/Mail-MboxParser-%{version}.tar.gz
Patch0:         %{name}-0.55-Fix-garbled-attachment-name-RT-66576.patch
Patch1:         %{name}-0.55-pod-encoding.patch
BuildArch:      noarch
Requires:       perl(MIME::Tools) >= 5
Requires:       perl(Mail::Mbox::MessageParser)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(MIME::Tools)
BuildRequires:  perl(MIME::Words)
BuildRequires:  perl(Mail::Mbox::MessageParser)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
