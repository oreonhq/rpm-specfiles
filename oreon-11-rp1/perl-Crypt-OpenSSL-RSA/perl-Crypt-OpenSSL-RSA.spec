Name:           perl-Crypt-OpenSSL-RSA
Version:        0.37
Release:        2%{?dist}
Summary:        Perl interface to OpenSSL for RSA
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-RSA
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Crypt-OpenSSL-RSA-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 917f7312532f8f4af4f3acbf6ba10e0151f8577d2ef1f38e1035229be86eb6f4
%global source0_file Crypt-OpenSSL-RSA-0.37.tar.gz
# oreon url source checksums end
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

%description
Crypt::OpenSSL::RSA - RSA encoding and decoding, using the openSSL libraries

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Crypt-OpenSSL-RSA-0.37.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "917f7312532f8f4af4f3acbf6ba10e0151f8577d2ef1f38e1035229be86eb6f4" || { echo "oreon: Source0 SHA256 mismatch for Crypt-OpenSSL-RSA-0.37.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37-2
- Prepare for Oreon 11 (RP1)
