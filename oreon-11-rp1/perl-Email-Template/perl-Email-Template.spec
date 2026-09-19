%global source0_hash f1a68fe08c36e37c2c454239ea1f3ee3131bc36161ae43080c6aeccd5d379d3e

Name:           perl-Email-Template
Version:        0.02
Release:        30%{?dist}
Summary:        Send "multipart/alternative" (text & html) e-mail from a Template
# lib/Email/Template.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Template
Source0:        https://cpan.metacpan.org/authors/id/S/SF/SFRYER/Email-Template-%{version}.tar.gz
# This module's tests currently try to send e-mails, which fails in mock/koji.
# This patch fixes this by sending the e-mail to a sub which verifies that the
# e-mail looks right.
# https://github.com/wchristian/Email-Template/commit/cefe961606f4bea2bd2373e0a5856c53dbcb33e2
Patch0:         Email-Template-send-disabling.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::FormatText::WithLinks::AndTables)
BuildRequires:  perl(MIME::Lite) >= 3.020
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(MIME::Lite) >= 3.020

%{?perl_default_filter}
%global __requires_exclude %__requires_exclude|^perl\\(MIME::Lite\\)$

%description
This is a fairly simple interface to generate "multipart/alternative"
e-mails with both "text/html" and "text/plain" components using a single
HTML based Template Toolkit template.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Template-%{version}
%patch -P0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Email*
%{_mandir}/man3/Email*

%changelog
%autochangelog
