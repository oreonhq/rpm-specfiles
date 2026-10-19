%global source0_hash cd3762cd76803729fd42022d382bc93b26f9b14aed9732eef85b44a9576d2d1e
Name:           perl-Digest-Nilsimsa
Version:        0.06
Release:        64%{?dist}
Summary:        Perl interface to the Nilsima Algorithm
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Digest-Nilsimsa
Source0:        https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Digest-Nilsimsa-%{version}.tar.gz
Patch0:         perl-Digest-Nilsimsa-c99.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A nilsimsa signature is a statistic of n-gram occurance in a piece of
text. It is a 256 bit value usually represented in hex. This module is a
wrapper around nilsimsa implementation in C by cmeclax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Digest-Nilsimsa-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
