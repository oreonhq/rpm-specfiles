%global source0_hash 82fa839897b88e9c245b6265f3be26d3bc879cae4c7a8151fad4a307c3366822

Name:           perl-Crypt-OpenSSL-RSA
Version:        0.41
Release:        1%{?dist}
Summary:        Perl interface to OpenSSL for RSA
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-RSA
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Crypt-OpenSSL-RSA-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::OpenSSL::Bignum)
BuildRequires:  perl(Crypt::OpenSSL::Random)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

Requires:       perl(Crypt::OpenSSL::Random)
Requires:	perl(Crypt::OpenSSL::Bignum)

Provides:       perl(Crypt::OpenSSL::RSA)
%description
Crypt::OpenSSL::RSA - RSA encoding and decoding, using the openSSL libraries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Crypt-OpenSSL-RSA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/*

%changelog
%autochangelog
