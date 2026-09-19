%global source0_hash 576892e6e720535911de6ff6055c8d16dea3d36008d02043c9867ea687beabea

Name:           perl-Crypt-JWT
Version:        0.037
Release:        3%{?dist}
Summary:        JSON Web Token (JWT, JWS, JWE) as defined by RFC7519, RFC7515, RFC7516
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Crypt-JWT
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/Crypt-JWT-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-libs
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::AuthEnc::GCM)
BuildRequires:  perl(Crypt::Digest)
BuildRequires:  perl(Crypt::KeyDerivation)
BuildRequires:  perl(Crypt::Mac::HMAC)
BuildRequires:  perl(Crypt::Misc)
BuildRequires:  perl(Crypt::Mode::ECB)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Crypt::PK::Ed25519)
BuildRequires:  perl(Crypt::PK::RSA)
BuildRequires:  perl(Crypt::PK::X25519)
BuildRequires:  perl(Crypt::PRNG)
BuildRequires:  perl(CryptX) >= 0.067
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Implements JSON Web Token (JWT) - https://tools.ietf.org/html/rfc7519. The
implementation covers not only JSON Web Signature (JWS) -
https://tools.ietf.org/html/rfc7515, but also JSON Web Encryption (JWE) -
https://tools.ietf.org/html/rfc7516.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-JWT-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%make_build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Crypt/
%{_mandir}/man3/Crypt::*.3pm*

%changelog
%autochangelog
