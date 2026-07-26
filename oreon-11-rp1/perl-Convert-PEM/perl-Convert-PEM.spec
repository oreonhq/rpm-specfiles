%global source0_hash 799fa32c270081f4e6292b0ddf5180952710a8a4be132e907bda3176a7bd1c23

Name:           perl-Convert-PEM
Version:        0.13
Release:        4%{?dist}
Summary:        Read/write encrypted ASN.1 PEM files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-PEM
Source0:        https://www.cpan.org/modules/by-module/Convert/Convert-PEM-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(Convert::ASN1) >= 0.34
BuildRequires:  perl(Crypt::DES_EDE3)
BuildRequires:  perl(Crypt::PRNG)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Optional tests
# Not available in Fedora: perl(Crypt::Camellia), perl(Crypt::Rijndael_PP), perl(Crypt::SEED)
BuildRequires:  openssl
BuildRequires:  perl(Crypt::IDEA)
BuildRequires:  perl(Crypt::OpenSSL::AES)
BuildRequires:  perl(Crypt::Rijndael)
# Dependencies
Requires:       perl(Convert::ASN1) >= 0.34
Requires:       perl(Crypt::DES_EDE3)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Convert::ASN1\\)$

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Convert/
%{_mandir}/man3/Convert::PEM.3*
%{_mandir}/man3/Convert::PEM::CBC.3*

%changelog
%autochangelog
