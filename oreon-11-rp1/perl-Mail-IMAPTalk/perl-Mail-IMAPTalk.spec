%global source0_hash 2be5594a6738f525a762ad4a8af1699d3c1b4f902d7e50615019ca1ed130b486
Name:           perl-Mail-IMAPTalk
Version:        4.07
Release:        1%{?dist}
Summary:        IMAP client interface with lots of features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-IMAPTalk
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBM/Mail-IMAPTalk-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Authen::SASL)
Requires:       perl(Encode)
Requires:       perl(Encode::IMAPUTF7)
Requires:       perl(MIME::Base64)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module communicates with an IMAP server. Each IMAP server command is
mapped to a method of this object.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mail-IMAPTalk-%{version}
chmod -x lib/Mail/IMAPTalk.pm

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

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.07-2
- Import
