# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ee91f8f7db894ee7c6ee003daac10a99056c4948a674ef46acdbb63c81a4abeb
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: perl-Digest-SHA
Version: 6.04
Release: 1%{?dist}
Summary: Perl interface to SHA-1/224/256/384/512
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/Digest-SHA
Source0: https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-macros
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl-interpreter
Provides: perl(Digest::SHA) = %{version}

%description
Perl module for SHA digests.

%prep
%oreon_sha256
%autosetup -n Digest-SHA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
  CC="%{__cc}" LD="%{__cc}" \
  OPTIMIZE="%{optflags}" \
  CCFLAGS="-D_REENTRANT -D_GNU_SOURCE -fwrapv -fno-strict-aliasing %{optflags}"
%make_build

%install
%make_install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%check
make test

%files
%license LICENSE
%{_bindir}/shasum
%{perl_vendorarch}/Digest/
%{perl_vendorarch}/auto/Digest/
%{_mandir}/man3/Digest::SHA.3*
