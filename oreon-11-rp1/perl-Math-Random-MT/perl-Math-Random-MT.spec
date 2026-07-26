%global source0_hash 069a1d98a619cba1f1ab91fbd6edceb642e84e7d162c4f0e2442139037b5b0da

Name:       perl-Math-Random-MT
Version:    1.17
Release:    16%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
Summary:    The Mersenne Twister PRNG
Source:     https://cpan.metacpan.org/authors/id/F/FA/FANGLY/Math-Random-MT-%{version}.tar.gz
Url:        http://metacpan.org/release/Math-Random-MT

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl(Benchmark)
BuildRequires: perl(Carp)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Number::Delta)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
The Mersenne Twister is a pseudorandom number generator developed by Makoto
Matsumoto and Takuji Nishimura. It is described in their paper at
<URL:http://www.math.keio.ac.jp/~nisimura/random/doc/mt.ps>. This algorithm
has a very uniform distribution and is good for modelling purposes but do
not use it for cryptography.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Random-MT-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
%autochangelog
