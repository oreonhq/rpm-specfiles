# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ba022a05b1adbec73712c46f233d8489fe13a1b9fc40a1fcceed9b52f90defc1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-Digest-CRC
Version:        0.24
Release:        1%{?dist}
Summary:        Generic CRC functions
License:        LicenseRef-Oreon-Public-Domain
URL:            https://metacpan.org/release/Digest-CRC
Source0:        https://cpan.metacpan.org/modules/by-module/Digest/Digest-CRC-%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  clang
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(Fcntl)
Requires:       perl(DynaLoader)
Requires:       perl(Symbol)

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains wrapper
functions with the correct parameters for CRC-SAE-J1850, CRC-CCITT, CRC-16 and
CRC-32.

%prep
%oreon_sha256
%setup -qn Digest-CRC-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test TEST_VERBOSE=1

%files
%doc Changes README
%{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/Digest/
%{_mandir}/man3/Digest::CRC.3*

%changelog
%autochangelog
