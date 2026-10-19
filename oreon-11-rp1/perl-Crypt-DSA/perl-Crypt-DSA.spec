%global source0_hash 1d192241b587f0a41b9f1a38bb90c2e10dcf31104eaaaf35d4803b68ff6cda9c
Summary:        Perl module for DSA signatures and key generation
Name:		perl-Crypt-DSA
Version:	1.19
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Url:		https://metacpan.org/release/Crypt-DSA
Source0:        https://www.cpan.org/modules/by-module/Crypt/Crypt-DSA-%{version}.tar.gz
BuildArch:	noarch
Requires:	openssl
Requires:	perl(Convert::ASN1)
Requires:	perl(Math::BigInt::GMP)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::DES_EDE3)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Data::Buffer)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. This package provides DSA signing, signature
verification, and key generation.

DSA (Digital Signature Algorithm) signatures are no longer considered to be
adequate for security. This module should only be used for verifying old
signatures and should not be used for new signatures. That being said, some
technologies still require DSA signatures even now. Consider using other
solutions or explicitly not using DSA signatures.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-DSA-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
