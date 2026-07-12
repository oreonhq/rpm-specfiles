%global source0_hash 6540085e3804b82a6f0752c1122cf78cadd221990136dd6fd4c097d056c84d40

Name:           perl-Crypt-Rijndael
Version:        1.16
Release:        18%{?dist}
Summary:        Crypt::CBC compliant Rijndael encryption module
# Rijndael.{h,xs}, _rijndael.c: LGPL-2.0-or-later
# Rijndael.pm, COPYING:         LGPL-3.0-only
# ppport.h:                     GPL-1.0-or-later OR Artistic-1.0-Perl
# See <https://github.com/Leont/crypt-rijndael/issues/10>.
License:        LGPL-3.0-only AND LGPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Crypt-Rijndael
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

Provides:       perl(Crypt::Rijndael)
Provides:       perl(Crypt::Rijndael)
%description
This module implements the Rijndael cipher, which has just been selected as
the Advanced Encryption Standard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-Rijndael-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING LICENSE
%doc Changes NEWS README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
%autochangelog
