%global source0_hash 0452285a1629f3b5ccf43c5d2854413b1d441c1753d8c6e28b88b8b52d9b4136

Name:           perl-Encode-ISO2022
Version:        0.04
Release:        35%{?dist}
Summary:        ISO/IEC 2022 character encoding scheme
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-ISO2022
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Encode-ISO2022-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
# 2.10 from Encode requirement in META.json
BuildRequires:  perl-Encode-devel >= 2.10
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode::CN)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::JP)
BuildRequires:  perl(Encode::KR)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(Test::More)

%description
This module provides a character encoding scheme (CES) switching a set of
multiple coded character sets (CCS).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Encode-ISO2022-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Encode
%{_mandir}/man3/*

%changelog
%autochangelog
