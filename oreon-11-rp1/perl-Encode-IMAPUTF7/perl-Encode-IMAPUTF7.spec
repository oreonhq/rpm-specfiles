%global source0_hash 52352b8ac0843b932f2a3c4abf817d3ce5a1b71274e1ad9d4e4eb094eb0f1d1c

%global remove_lf() for i in %*; do tr -d '\\r' < $i > $i. && touch -r $i $i. && mv -f $i. $i; done

Name:           perl-Encode-IMAPUTF7
Version:        1.07
Release:        31%{?dist}
Summary:        Process the special UTF-7 variant required by IMAP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-IMAPUTF7
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Encode-IMAPUTF7-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(warnings)


Provides:       perl(Encode::IMAPUTF7)
%description
This module is able to encode and decode IMAP mailbox names using the UTF-7
modification specified in RFC2060 section 5.1.3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Encode-IMAPUTF7-%{version}
%remove_lf README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%_fixperms %buildroot/*

%check
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Encode
%{perl_vendorlib}/Encode/IMAPUTF7.pm
%_mandir/man3/Encode::IMAPUTF7.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.07-31
- Import
