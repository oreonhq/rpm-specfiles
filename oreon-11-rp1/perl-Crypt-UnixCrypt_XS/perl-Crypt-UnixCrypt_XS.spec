%global source0_hash 62eb3412c2c91bd4dc2b8a4d9ee26d5bde2eb11932703b6eeac4773e4d1f4faa

Name:           perl-Crypt-UnixCrypt_XS
Version:        0.11
Release:        28%{?dist}
Summary:        Perl xs interface for a portable traditional crypt function
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-UnixCrypt_XS
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BORISZ/Crypt-UnixCrypt_XS-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Algorithm::Loops)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(warnings)

%description
This module implements the DES-based Unix crypt function. For those who
need to construct non-standard variants of crypt, the various building
blocks used in crypt are also supplied separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Crypt-UnixCrypt_XS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"  NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
%autochangelog
