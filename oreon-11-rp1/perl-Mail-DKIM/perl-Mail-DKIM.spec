%global source0_hash 45de46f5dc4d23bcb6ad6401759881dd43968eab20e73f6f79d9557467de20ee
Name:           perl-Mail-DKIM
Version:        1.20240923
Release:        4%{?dist}
Summary:        Sign and verify Internet mail with DKIM/DomainKey signatures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://dkimproxy.sourceforge.net/
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/Mail-DKIM-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(Crypt::PK::Ed25519)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Mail::AuthenticationResults::Header::AuthServID)
BuildRequires:  perl(Mail::AuthenticationResults::Parser)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::Resolver::Mock)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements the various components of the DKIM and DomainKeys
message-signing and verifying standards for Internet mail. It currently
tries to implement RFC4871 (for DKIM) and RFC4870 (DomainKeys).

It is required if you wish to enable DKIM checking in SpamAssassin via the
Mail::SpamAssassin::Plugin::DKIM plugin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mail-DKIM-%{version}
# Make the example scripts non-executable
chmod -x scripts/*.pl
# Use the real path in the shebang
/usr/bin/perl -pi -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' scripts/arcverify.pl
# Remove dos-type line endings
/usr/bin/perl -pi -e 's/\r//' doc/qp1.txt

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20240923-4
- Prepare for Oreon 11 (RP1)
