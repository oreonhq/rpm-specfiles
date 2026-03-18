Name:           perl-Mail-IMAPTalk
Version:        4.07
Release:        2%{?dist}
Summary:        IMAP client interface with lots of features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-IMAPTalk
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Mail-IMAPTalk-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# No tests exist, run-time modules are not needed
# Authen::SASL
# constant
# Data::Dumper
# Digest
# Encode
# Encode::IMAPUTF7
# Exporter
# Fcntl
# IO::Handle
# IO::Select
# IO::Socket
# MIME::Base64
# Socket
Requires:       perl(Authen::SASL)
Requires:       perl(Encode)
Requires:       perl(Encode::IMAPUTF7)
Requires:       perl(MIME::Base64)

%description
This Perl module communicates with an IMAP server. Each IMAP server command is
mapped to a method of this object.

%prep
%setup -q -n Mail-IMAPTalk-%{version}
chmod -x lib/Mail/IMAPTalk.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.07-2
- Prepare for Oreon 11 (RP1)
