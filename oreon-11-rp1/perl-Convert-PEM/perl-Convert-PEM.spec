%global source0_hash 799fa32c270081f4e6292b0ddf5180952710a8a4be132e907bda3176a7bd1c23
Name:           perl-Convert-PEM
Version:        0.13
Release:        1%{?dist}
Summary:        Read/write encrypted ASN.1 PEM files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-PEM
Source0:        https://www.cpan.org/modules/by-module/Convert/Convert-PEM-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Convert::ASN1) >= 0.34
Requires:       perl(Crypt::DES_EDE3)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Convert::ASN1\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Crypt::DES_EDE3)
BuildRequires:  perl(Crypt::IDEA)
BuildRequires:  perl(Crypt::OpenSSL::AES)
BuildRequires:  perl(Crypt::PRNG)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is Convert::PEM, a module implementing read/write access
to ASN.1-encoded PEM files (with optional encryption).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-PEM-%{version}

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
